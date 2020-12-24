from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
op=Options()
op.add_argument(r'C:\Users\v-fengjiahui\AppData\Local\Google\Chrome\Application\chrome.exe')
driver=webdriver.Chrome()
driver.get('https://account.aliyun.com/register/register.html')
iframe=driver.find_element_by_xpath('//*[@id="alibaba-register-box"]')
driver.switch_to.frame(iframe)

div=driver.find_element_by_xpath('//*[@data-nc-lang="_startTEXT"]')
div_window=div.size['width']
span=driver.find_element_by_xpath('//*[@class="nc_iconfont btn_slide"]')
ac=ActionChains(driver)
ac.move_to_element(span)
ac.click_and_hold()