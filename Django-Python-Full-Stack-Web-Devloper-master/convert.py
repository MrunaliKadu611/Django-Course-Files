from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import Select
import time
import csv
from datetime import datetime

driver = webdriver.Firefox(executable_path='C:\\Users\\Lenovo\\Downloads\\geckodriver\\geckodriver.exe')
driver.get('http://54.169.182.163/standardedition/index.php')
driver.maximize_window()

# login
driver.find_element_by_id('user_name').send_keys('admin')
driver.find_element_by_id('user_password').send_keys('SyM!@pE5#')
driver.find_element_by_name('Login').click()
time.sleep(3)

# cases in navigation

navDropdown = driver.find_element_by_xpath('/html/body/div[2]/nav/div[4]/ul/li[8]/a/i')
navDropdown.click()
navCases = driver.find_element_by_xpath('/html/body/div[2]/nav/div[4]/ul/li[8]/ul/div/li[2]/a/span[2]')
navCases.click()

# today's date
today = datetime.now().strftime("%d-%m-%Y-%H.%M.%S")


# # open file and write test cases
# with open('Ticket'+ today +'.csv', 'w') as t:
#     columnTitle = "Feature, Actual result\n"
#     t.write(columnTitle)
time.sleep(3)
# create FCR
# casesModuleTab = driver.find_element_by_xpath('//*[@id="moduleTab_Cases"]')
# createCase = driver.find_element_by_xpath('/html/body/div[1]/nav/div[4]/ul/li[7]/ul/li[1]/a/span')
# ActionChains(driver).move_to_element(casesModuleTab).move_to_element(createCase).click()


cases = driver.find_element_by_xpath('//*[@id="moduleTab_Cases"]')
hover = ActionChains(driver).move_to_element(cases)
hover.build().perform()
Createcase = driver.find_element_by_link_text('index.php?module=Cases&action=EditView&return_module=Cases&return_action=DetailView')
Createcase.click()
