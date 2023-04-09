# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.chrome.options import Options
#
# from pages.cart_page import Cart_page
# from pages.client_information_page import Client_information_page
# from pages.finish_button_page import Finish_page
# from pages.login_page import Login_page
# from pages.main_page import Main_page
# from pages.payment_page import Payment_page
#
#
# def test_about_link(set_up):
#     options = Options()
#     options.add_experimental_option('excludeSwitches', ['enable-logging'])
#     driver = webdriver.Chrome(executable_path="C:\\Users\\user\\Desktop\\Selenium_Framework\\chromedriver.exe", chrome_options=options)
#     print("Start test")
#
#     login = Login_page(driver)
#     login.authorization()
#
#     mp = Main_page(driver)
#     mp.select_menu_about()
#
#     time.sleep(10)
#
#
#
#
#
#
#
#
#
#
