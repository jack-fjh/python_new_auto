from selenium import webdriver
import time

driver=webdriver.Chrome()
driver.get('https://www.baidu.com')
input_ele=driver.find_element_by_id('kw')
#get_attribute获取元素本身自带属性
print(input_ele.get_attribute('maxlength'))
print(input_ele.location)
print(input_ele.size)
print(input_ele.rect)
print(input_ele.get_property('clientWidth'))
