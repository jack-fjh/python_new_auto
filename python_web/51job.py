from selenium import webdriver
import time
driver=webdriver.Chrome()
driver.get('https://www.51job.com/shanghai/')
driver.maximize_window()
driver.find_element_by_xpath('//p[@class="ipt"]/input[2]').send_keys('自动化测试')
driver.find_element_by_xpath('//div[@class="d_search Fm"]//button').click()
driver.find_element_by_xpath('//div[@class="j_filter"]/div[@class="fbox"][2]//div[@class="clist"]/a[10]/span').click()
time.sleep(5)
res=driver.find_elements_by_xpath('//div[@class="j_joblist"]//a/p[1]')
print(res)
for res_name in res:
    print(res_name.text)