from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains
class ActionsTest(object):
    def __init__(self):
        self.driver=webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
    def baidu_advance_search(self):
        self.driver.get("https://www.baidu.com")
        setting_link=self.driver.find_element_by_xpath('//div[@id="u1"]/span')
        setting_link.click()
        advance_link=self.driver.find_element_by_xpath('//*[@class="s-user-setting-pfmenu"]/a[2]')
        advance_link.click()

    def baidu_advance_by_hover(self):
        """
        通过鼠标经过元素显示出下拉选项
        :return:
        """
        self.driver.get("https://www.baidu.com")
        setting_link = self.driver.find_element_by_xpath('//div[@id="u1"]/span')
        action=ActionChains(self.driver)
        #调用perform()方法执行
        #先移动到元素上
        action.move_to_element(setting_link).pause(3).perform()
        #再来定位新元素
        advance_link = self.driver.find_element_by_xpath('//*[@class="s-user-setting-pfmenu"]/a[2]')
        #最后再执行click
        action.click(advance_link)
        action.perform()

    def aliyun_drag_and_drop(self):
        self.driver.get('https://account.aliyun.com/register/register.html')
        #切换frame
        frame=self.driver.find_element_by_xpath('//*[@id="alibaba-register-box"]')
        self.driver.switch_to.frame(frame)
        #2:被拖拽的元素
        drag_source=self.driver.find_element_by_xpath('//*[@id="nc_1_n1z"]')
        div=self.driver.find_element_by_xpath('//*[@id="nc_1__scale_text"]')
        #获取滑动模块的宽度
        # width=div.get_property('width')这个不能用，后期用js来实现
        action=ActionChains(self.driver)
        action.drag_and_drop_by_offset(drag_source,320,0).perform()
if __name__ == '__main__':
    a=ActionsTest()
    # a.baidu_advance_by_hover()
    a.aliyun_drag_and_drop()