from selenium import webdriver
import time
import constants.bsnl_constants as constants
import utilities.db_query as db_query
from selenium.webdriver.support.select import Select

from bsnl import model_plan


def scrap_plans(db_connection, driver):
    driver.get(constants.BSNL_PREPAID_URL)
    circles = Select(driver.find_element_by_id('circle'))
    plan_list = []
    for circle in circles.options:
        try:
            print(circle.text)
            if circle.text == 'Select State/Circle':
                continue
            circles.select_by_visible_text(circle.text)
            time.sleep(1)
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            vouchers = driver.find_element_by_xpath("//*[@id='vouchers']").find_elements_by_class_name("panel")
            for voucher in vouchers:
                try:
                    if voucher.text == 'PLAN Extension' or voucher.text == 'PLAN Migration':
                        continue
                    # print(voucher.text)
                    plan_type = voucher.text
                    # print("----------------")
                    voucher.click()
                    time.sleep(2)
                    items = voucher.find_elements_by_class_name("voucher")
                    for li in items:
                        plan_model = model_plan.BsnlPlan("", "", "", "", "", "")
                        plan_model.circle = circle.text  # CIRCLE
                        plan_model.plan_type = plan_type  # TYPE
                        # print(li.text)
                        y = li.text
                        m = y.split('\n')
                        if len(m) >= 4:
                            plan_model.amount = m[0]  # AMOUNT
                            plan_model.plan_name = m[1]  # NAME
                            plan_model.benefit = m[2]  # BENIFIT
                            plan_model.description = m[3]  # DESCRIPTION
                        plan_list.append(plan_model)
                except Exception:
                    print("")
            time.sleep(2)
            #break
        except Exception:
            print("")

    db_query.insert_bsnl_plans(plan_list, db_connection)
    # for plan in plan_list:
    #     print(str(plan))

# Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     scrap_plans()
