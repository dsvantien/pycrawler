import os
from selenium import webdriver
from time import sleep
from bs4 import BeautifulSoup
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36"
options = webdriver.ChromeOptions()
options.headless = True

options.add_argument(f'user-agent={user_agent}')
options.add_argument("--window-size=1536,824")
options.add_argument('--ignore-certificate-errors')
options.add_argument('--allow-running-insecure-content')
options.add_argument("--disable-extensions")
options.add_argument("--proxy-server='direct://'")
options.add_argument("--proxy-bypass-list=*")
options.add_argument("--start-maximized")
options.add_argument('--disable-gpu')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--no-sandbox')

driver = webdriver.Chrome(os.getcwd()+"\\chromedriver.exe", options=options)
# driver = webdriver.Chrome(os.getcwd()+"\\chromedriver.exe")
url = 'https://www.barclays.co.uk/mortgages/mortgage-calculator/cost-calculator/#/cost'
driver.get(url)
sleep(2)
reason_select = Select(driver.find_element_by_xpath('/html/body/main/div[3]/section[1]/div/div/div/div/div/div[2]/form/div[2]/div/fieldset/div/div/div/div/select'))
reason_select.select_by_value('FTBP')
estimate_inp = driver.find_element_by_xpath('/html/body/main/div[3]/section[1]/div/div/div/div/div/div[2]/form/div[3]/div/fieldset/div/div/div/input')
estimate_inp.send_keys('40000')
repayment_select = Select(driver.find_element_by_xpath('/html/body/main/div[3]/section[1]/div/div/div/div/div/div[2]/form/div[4]/div/fieldset/div/div/div/div/select'))
repayment_select.select_by_value('repayment')
borrow_inp = driver.find_element_by_xpath('/html/body/main/div[3]/section[1]/div/div/div/div/div/div[2]/form/div[8]/div/fieldset/div/div/div/input')
borrow_inp.send_keys('20000')
year_select = Select(driver.find_element_by_xpath('/html/body/main/div[3]/section[1]/div/div/div/div/div/div[2]/form/div[12]/div/fieldset/div/div/div/div[1]/div/div/select'))
year_select.select_by_value('7')
month_select = Select(driver.find_element_by_xpath('/html/body/main/div[3]/section[1]/div/div/div/div/div/div[2]/form/div[12]/div/fieldset/div/div/div/div[2]/div/div/select'))
month_select.select_by_value('8')
submit = driver.find_element_by_xpath('/html/body/main/div[3]/section[1]/div/div/div/div/div/div[2]/form/div[13]/div/ul/li/button')
# submit.click() # cant click because not visibale have to scroll down
action_chain = ActionChains(driver)
action_chain.move_to_element(submit).click()
sleep(1)
action_chain.perform()
sleep(10)
# driver.get_screenshot_as_file('screen.png')
ele = driver.find_element_by_xpath('/html/body/main/div[3]/section[1]/div/div/div/div/div/div[3]/div[2]/form/div[1]/table/tbody/tr[1]/td/span')
print(ele.text)
# print(driver.get_cookies())
sleep(1)
res = driver.page_source
soup = BeautifulSoup(res, 'lxml')
print(soup.prettify())
# print(soup.prettify())
driver.quit()

