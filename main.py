# This is a sample Python script.
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import constants.common_constants as constants
# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import bsnl.bsnl as bsnl
import jio.jio as jio
import airtel.airtel as airtel
import utilities.db_connection as db

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    options = Options()
    options.headless = True
    driver = webdriver.Chrome(constants.CROME_DRIVER_PATH, chrome_options=options)
    connection = db.DbInstance().get_connection()
    #bsnl.scrap_plans(connection, driver)
    #jio.scrap_jio_plans(connection, driver)
    airtel.scrap_airtel_plans(connection, driver)
    connection.close()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
