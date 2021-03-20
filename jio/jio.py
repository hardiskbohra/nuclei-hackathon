import os
import selenium
from selenium import webdriver
import time
import io
import requests
from selenium.common.exceptions import ElementClickInterceptedException
import jio.jio_plan_model as model
import utilities.db_query as db_query
import utilities.db_connection as db
import constants.common_constants as constants

# Install Driver
# driver = webdriver.Chrome(constants.CROME_DRIVER_PATH)
list_of_plans = []


def scrap_jio_plans(db_connection, driver):
    # Use a breakpoint in the code line below to debug your script.

    print('------Starting Jio------')

    time.sleep(1)
    print('Popular Plans')
    get_plans("https://www.jio.com/en-in/4g-plans", 'Popular Plans', db_connection, driver)

    time.sleep(1)
    print('Jio Phone')
    get_plans("https://www.jio.com/jiophone-recharge-plans", 'Jio Phone', db_connection, driver)

    time.sleep(1)
    print('4G Data Voucher')
    get_plans("https://www.jio.com/jio-4g-prepaid-data-voucher", '4G Data Voucher', db_connection, driver)

    time.sleep(1)
    print('Jio Phone Data Add On')
    get_plans("https://www.jio.com/jiophone-data-add-on-plans", 'Jio Phone Data Add On', db_connection, driver)

    time.sleep(1)
    print('Disney + Hotstar VIP')
    get_plans("https://www.jio.com/en-in/hotstar-prepaid-plans", 'Disney + Hotstar VIP', db_connection, driver)

    time.sleep(1)
    print('In-Flight Packs')
    get_plans("https://www.jio.com/in-flight-internet-prepaid-recharge-plans", 'In-Flight Packs', db_connection, driver)

    time.sleep(1)
    print('Top-Up')
    get_plans("https://www.jio.com/jio-top-up-recharge-plans", 'Top-Up', db_connection, driver)

    time.sleep(1)
    print('Jio Link')
    get_plans("https://www.jio.com/jio-link-recharge-plans", 'Jio Link', db_connection, driver)

    time.sleep(1)
    print('Jio Saavan Pro')
    get_plans("https://www.jio.com/en-in/jio-saavn-subscription-plans", 'Jio Saavan Pro', db_connection, driver)

    time.sleep(2)
    print('Others')
    get_plans("https://www.jio.com/jio-other-recharge-plans", 'Others', db_connection, driver)


def get_plans(url, category, db_connection, driver):
    driver.get(url)

    time.sleep(3)

    plans_list = driver.find_elements_by_class_name("pkv-card-plans")
    # print(f'list : {plans_list}')

    # selected_tab = driver.find_element_by_class_name("scrollmenu-wrapper")
    # print(f'Plans for : ')

    for plan in plans_list:
        try:

            amount = plan.find_elements_by_class_name("txt_amt")[0].text
            amount_str = "₹ " + amount[1:]

            validity_and_data = plan.find_elements_by_class_name("pkv_txt_info")

            try:
                validity = validity_and_data[0].text
                # print(f'Validity : {validity}')
            except:
                validity = 'NA'

            try:
                data = validity_and_data[1].text
                # print(f'Data : {data}')
            except:
                data = 'NA'

            dto = model.JioPlanModel(amount_str, data, validity, category)

            # try:
            #     extra_data = plan.find_elements_by_class_name("txt-small-info")
            #     # print(f'Extra Data : {extra_data[0].text}')
            # except:
            #     print('Error in Extra Data')

            plan.find_element_by_class_name("pkv-link").click()

            time.sleep(2)

            # reading popup
            # print('-----extra info-----')
            # header = driver.find_element_by_class_name("top-head-section")
            # amount = header.find_element_by_class_name("amt-plan").text
            # info = header.find_element_by_class_name("info_txt").text
            # print(f'Amount : {amount}')
            # dto.amount = amount
            # print(f'Information Text : {info}')

            detail_section = driver.find_element_by_class_name("detail_section")
            details = detail_section.find_elements_by_class_name("details-row")

            for detail in details:
                try:
                    key = detail.find_element_by_class_name("detail_title").text
                    value = detail.find_element_by_class_name("detail_list").text
                    # print(f'{key} : {value}')
                    if "data" in key.lower():
                        dto.data = value
                    elif "validity" in key.lower():
                        dto.validity = value
                    elif "sms" in key.lower():
                        dto.sms = value
                    elif "voice" in key.lower():
                        dto.voice = value
                except:
                    print('')

            try:
                # key = driver.find_element_by_class_name("details-notes-title")
                values = driver.find_element_by_class_name("details-notes-list").find_elements_by_tag_name("li")

                # print('Note : ')
                description = ''

                for value in values:
                    description = description + value.text
                    # print(f'{value.text}')
                dto.description = description
            except:
                dto.description = 'NA'
            # print('--------------------')

            driver.find_element_by_class_name("close_plan_detail").click()

            time.sleep(1)
            # print(dto)
        except:
            print('')

        list_of_plans.append(dto)
        # break
    # print(list_of_plans)
    db_query.insert_jio_plans(list_of_plans, db_connection)

# Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     scrap_jio_plans('Jio')