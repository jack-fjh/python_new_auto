'''
切换窗口，切换弹窗等操作
'''

from selenium import webdriver
import time
class BaseDemo(object):
    def __init__(self):
        self.driver=webdriver.Chrome()
        self.driver.implicitly_wait(10)

    def switch_window_demo(self):
        """
        浏览器打开了多个窗口，每个窗口都不一样，进行自动化操作的时候，需要切换window窗口
        :return:
        """
        self.driver.get('https://www.baidu.com')
        self.driver.find_element_by_xpath('//input[@name="wd"]').send_keys('helloworld')
        self.driver.find_element_by_css_selector('input#su').click()
        self.driver.find_element_by_xpath('//div[@id="content_left"]/div[1]//h3[@class="t c-gap-bottom-small"]/a').click()
        #切换浏览器窗口
        all_windows=self.driver.window_handles
        print(all_windows)
        self.driver.switch_to.window(all_windows[1])
        self.driver.find_element_by_xpath('//div[@class="layout"]//div[@class="form"]/form[1]/input').clear()
        #切回到第一个窗口
        self.driver.switch_to.window(all_windows[0])
        self.driver.find_element_by_css_selector('input[name="wd"]').clear()

    def switch_iframe_demo(self):
        self.driver.get('https://login.anjuke.com/login/form')
        iframe_ele=self.driver.find_element_by_xpath('//iframe[@id="iframeLoginIfm"]')
        #切换到iframe
        self.driver.switch_to.frame(iframe_ele)
        self.driver.find_element_by_xpath('//input[@id="phoneIpt"]').send_keys('123456789')
        #切换回到上一级（有两种方式：switch_to.parent_frame()和switch_to.default_content()）
        self.driver.switch_to.parent_frame()
        self.driver.find_element_by_link_text('联系我们')

    def switch_alert_demo(self):
        self.driver.get(r'C:\tools\git\git-cangku\python_web\demo.html')
        #切换到alert
        alert=self.driver.switch_to.alert
        time.sleep(5)
        #点击确定
        alert.accept()#点击确定，dissmiss就是取消

if __name__ == '__main__':
    B=BaseDemo()
    # B.switch_window_demo()
    # B.switch_iframe_demo()
    B.switch_alert_demo()