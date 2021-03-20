import os
import selenium
from selenium import webdriver
import time
import io
import requests
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import airtel.airtel_model as model
import utilities.db_query as db_query

packs = []
packs_model = []


def scrap_airtel_plans(connection, driver):
    driver.get("https://www.airtel.in/recharge-online")

    search_result = driver.find_elements_by_class_name('pack-detail-row')

    for result in search_result:
        landingPagePacks = result.find_elements_by_tag_name('p')
        packInformation = {}
        packInformation['LandingPagePacks'] = list(result.text.split('\n'))  # packDetails

        try:
            time.sleep(2)
            viewMorePageButton = result.find_elements_by_tag_name('button')
            viewMorePageButton[1].click();
            time.sleep(2)

            planType = driver.find_elements_by_class_name('left-sidebar')
            packInformation['Tag'] = planType[1].find_elements_by_tag_name('section')[0].find_element_by_tag_name(
                'h3').text
            time.sleep(1)
            try:
                additonalBenefits = driver.find_elements_by_class_name('benifit-block')
                benefitsList = []
                for benefits in additonalBenefits:
                    benefit = benefits.find_elements_by_tag_name('p')
                    for b in benefit:
                        benefitsList.append(b.text)
                packInformation['additionalBenefits'] = benefitsList
            except:
                packInformation['additionalBenefits'] = []

            try:
                otherDetailsSection = driver.find_elements_by_class_name('other-details')
                otherDetailsSection[0].find_element_by_class_name('icon-outlined-chevron-down').click()
                time.sleep(1)
                otherDetails = driver.find_elements_by_class_name('detail-content')
                details = otherDetails[0].find_elements_by_tag_name('p')
                otherDetailsList = []
                for d in details:
                    otherDetailsList.append(d.text)
                packInformation['otherDetails'] = otherDetailsList
            except:
                packInformation['otherDetails'] = []

            try:
                morePlanDetails = driver.find_elements_by_class_name('plan-top')
                moreDetailsList = list(morePlanDetails[0].text.split('\n'))
                moreDetailsList[2:] = moreDetailsList[2:][::-1]
                packInformation['morePlanDetails'] = moreDetailsList
            except:
                print('dont know')

            returnToLandingPage = driver.find_elements_by_class_name('icon-outlined-cross')[0]
            returnToLandingPage.click()
        except:
            print('plan missed')
        time.sleep(1)

        driver.execute_script("window.scrollTo(0, window.scrollY + 180)")

        time.sleep(2)
        print(packInformation)
        packs.append(packInformation)
        # break
    display(packs, connection)


def display(packsInfo, connection):
    for packInfo in packsInfo:
        try:
            plan = {
                'amount': 'NA',
                'data': 'NA',
                'validity': 'NA',
                'sms': 'NA',
                'tag': 'Others',
                'additionalInfo': 'NA',
                'otherInfo': 'NA'
            }

            plan['amount'] = packInfo['LandingPagePacks'][0]
            if 'Tag' in packInfo.keys():
                plan['tag'] = packInfo['Tag']

            if 'validity' in packInfo['LandingPagePacks']:
                indexOfAddValidity = packInfo['LandingPagePacks'].index('validity')
                plan['validity'] = packInfo['LandingPagePacks'][indexOfAddValidity - 1]

            if packInfo['LandingPagePacks'][1] == 'Truly Unlimited Calls':
                plan['data'] = ' '.join(packInfo['LandingPagePacks'][2:4])

            if packInfo['LandingPagePacks'][2] == 'talktime':
                plan['data'] = packInfo['LandingPagePacks'][1]
                plan['tag'] = 'Talktime'

            # if 'morePlanDetails' in packInfo.keys():
            #     details = '\n'.join(packInfo['morePlanDetails'])
            #     print(details)
            #     plan['otherInfo'] = details
            #     print('----')

            if 'additionalBenefits' in packInfo.keys():
                if packInfo['additionalBenefits']:
                    benefits = '\n'.join(packInfo['additionalBenefits'])

                    plan['additionalInfo'] = benefits

            if 'otherDetails' in packInfo.keys():
                if packInfo['otherDetails']:
                    details = '\n'.join(packInfo['otherDetails'][:-1])

                    plan['otherInfo'] = details

            if len(packInfo.keys()) == 1:
                if 'Additional Benefit(s)' in packInfo['LandingPagePacks']:
                    indexOfAddInfo = packInfo['LandingPagePacks'].index('Additional Benefit(s)')
                    plan['additionalInfo'] = '\n'.join(packInfo['LandingPagePacks'][indexOfAddInfo:-1])

                    if packInfo['LandingPagePacks'][1] == 'Truly Unlimited Calls':
                        plan['data'] = ' '.join(packInfo['LandingPagePacks'][2:4])

                    if 'data' in packInfo['LandingPagePacks']:
                        indexOfData = packInfo['LandingPagePacks'].index('data')
                        plan['data'] = packInfo['LandingPagePacks'][indexOfData - 1]

            airtelPlan = model.AirtelModel(plan['amount'], plan['data'], plan['validity'], plan['sms'], plan['tag'],
                                           plan['additionalInfo'], plan['otherInfo']);
            packs_model.append(airtelPlan)
        except Exception:
            print('')
    db_query.insert_airtel_plans(packs_model, connection)
    # print(airtelPlan)
    # print('--------------------------')

    time.sleep(2)

# if __name__ == '__main__':
#     print_hi('airtel')
#     # display(packs)
