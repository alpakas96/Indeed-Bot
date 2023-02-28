
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


###IMPORTANT###
# 1. open terminal

# 2. run: 

# open -na "Google Chrome" --args --remote-debugging-port=9222

# 3. navigate to indeed.com 

# 4. log in 

# 5. clear job title and location 

# 6. run program

def terminalLogger(sleepTime=0.5, message=''):
    print(message)
    time.sleep(sleepTime)
    print('\n')


# Replace the path with the path to your Chrome driver executable
driver_path = './chromedriver'

chrome_options = Options()
chrome_options.add_argument('--remote-debugging-port=9222')
driver_path = './chromedriver'
driver = Chrome(service=ChromeService(executable_path=driver_path), options=chrome_options)

wait = WebDriverWait(driver, 10)

######### Input job search params
terminalLogger(message='typing job title')
what_input = wait.until(EC.element_to_be_clickable((By.ID, 'text-input-what')))


terminalLogger(message='typing location')
where_input = driver.find_element(by=By.ID, value='text-input-where')

what_input.click()

ActionChains(driver) \
    .send_keys_to_element(what_input, info.position) \
    .perform()

ActionChains(driver) \
    .send_keys_to_element(where_input, info.location) \
    .perform()

search_button = driver.find_element(by=By.CLASS_NAME, value='yosegi-InlineWhatWhere-primaryButton')
terminalLogger(message='search button found')
search_button.click()
terminalLogger(message='search button clicked')

posts_list = driver.find_element(by=By.CLASS_NAME, value='jobsearch-ResultsList')
posts = posts_list.find_elements(by=By.CLASS_NAME, value='jcs-JobTitle')
print(len(posts))

def checkEasyApply(driver=driver):
    driver.implicitly_wait(10)
    time.sleep(5)
    wait = WebDriverWait(driver, 10)

    try:

        ### find Easy apply button
        print('clicked on post')
        rightPane = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div.jobsearch-RightPane')))
        terminalLogger(message='right pane found')

        #debugging here: 
        # try:
        #     driver.switch_to.frame(rightPane)
        #     terminalLogger(message='switched to right pane')

        # except Exception as e:
        #     print(f"An exception occurred: {e}")
        
        iframe = driver.find_element(by=By.TAG_NAME, value='iframe')
        terminalLogger(message='iframe found')
        
        driver.switch_to.frame(iframe)
        terminalLogger(message='switched to iframe')

        # application_btn = driver.find_element(by=By.CSS_SELECTOR, value='button.css-1bm49rc.e8ju0x51')
        application_btn = driver.find_element(by=By.CLASS_NAME, value='css-1bm49rc.e8ju0x51')
        application_btn.click()
        terminalLogger(message='Easy Apply button found')

        #switch focus to new tab
        driver.switch_to.window(driver.window_handles[1])
        easyApply(driver)

    except:
        terminalLogger(message='Easy Apply button not found') 
        #undo switch to iframe
        driver.switch_to.default_content()
        terminalLogger(message='switched focus back to default content')
        pass


for post in posts:
    post.click()
    checkEasyApply(driver=driver)
    time.sleep(3)

terminalLogger(message='end script in 5', sleepTime=5)

driver.quit()

time.sleep(999)