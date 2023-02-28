
# selenium 4
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import Chrome, ChromeOptions
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys, ActionChains
import info
from info import *
import time
from EasyApply import *

def terminalLogger(sleepTime=0.5, message=''):
    print(message)
    time.sleep(sleepTime)
    print('\n')

chrome_options = ChromeOptions()
# chrome_options.add_argument("--remote-debugging-port=9222")
driver = Chrome(options=chrome_options)

# switch to the first window (assuming it exists)
# driver.switch_to.window(driver.window_handles[0])

driver.get("https://www.indeed.com")
driver.maximize_window()



######### Input job search params
terminalLogger(message='typing search inputs')
what_input = driver.find_element(by=By.ID, value='text-input-what')
where_input = driver.find_element(by=By.ID, value='label-text-input-where')

what_input.click()
ActionChains(driver) \
    .send_keys_to_element(what_input, info.position) \
    .perform()

search_button = driver.find_element(by=By.CLASS_NAME, value='yosegi-InlineWhatWhere-primaryButton')
search_button.click()

posts_list = driver.find_element(by=By.CLASS_NAME, value='jobsearch-ResultsList')
posts = posts_list.find_elements(by=By.CLASS_NAME, value='jcs-JobTitle')
print(len(posts))

def rightPaneFunction(driver=driver):
    rightPane = driver.find_element(by=By.CSS_SELECTOR, value='div.jobsearch-RightPane')
    terminalLogger(message='right pane found')
    return rightPane

def checkEasyApply(driver=driver):
    driver.implicitly_wait(10)
    time.sleep(5)

    try:
        print('finding apply button..')
        iframe = rightPaneFunction(driver).find_element(by=By.TAG_NAME, value='iframe')
        terminalLogger(message='iframe found')
        driver.switch_to.frame(iframe)
        terminalLogger(message='switched to iframe')
        application_btn = driver.find_element(by=By.CSS_SELECTOR, value='button.css-1bm49rc.e8ju0x51')
        application_btn.click()
        terminalLogger(message='Easy Apply button found')
        #switch focus to new tab
        driver.switch_to.window(driver.window_handles[1])
        easyApply(driver)
    except:
        terminalLogger(message='Easy Apply button not found') 
        pass


for post in posts:
    post.click()
    checkEasyApply(driver=driver)
    time.sleep(3)

terminalLogger(message='end script in 5', sleepTime=5)

driver.quit()

time.sleep(999)