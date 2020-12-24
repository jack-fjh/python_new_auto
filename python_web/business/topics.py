from common.singdriver import demo_driver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from business.usercenter import UserCenter
from business.login import login_first_page

class TopicAction(object):
    """
    业务代码
    话题相关操作
    1：发布话题
    2：修改话题
    3：删除话题
    4：回复话题
    """
    driver=demo_driver()
    def __create_topic(self,topic_title_name,topic_content_name):
        self.driver.find_element_by_xpath('//*[@class="nav pull-right"]/li[1]/a').click()#点击首页
        topic_name_value=self.driver.find_elements_by_xpath('//*[@id="create_topic_btn"]/span')#点击发表话题
        if  len(topic_name_value)!=0:
            self.driver.find_element_by_xpath('//*[@id="create_topic_btn"]/span').click()
        self.driver.find_element_by_xpath('//*[@id="tab-value"]').click()#点击选择模板
        self.driver.find_element_by_xpath('//*[@id="tab-value"]/option[2]').click()
        self.driver.find_element_by_xpath('//*[@id="title"]').send_keys(topic_title_name)
        self.pub_func_topic(topic_content_name)

    def add_topic(self,title_name,content_name):
        """
        新建话题
        :return:
        """
        self.__create_topic(title_name,content_name)

    def edit_topic(self):
        """
        更新话题
        :return:
        """
        self.driver.find_element_by_xpath('//*[@class="fa fa-lg fa-pencil-square-o"]').click()



    def delete_topic(self):
        """
        删除话题
        :return:
        """
        self.driver.find_element_by_xpath('//*[@class="fa fa-lg fa-trash"]').click()

    def reply_recent_create_topic(self):
        """
        选择在个人中心最近创建的话题中进行回复话题
        :return:
        """
        self.pub_func_topic('雷霆嘎巴')

    def reply_topic(self):
        """
        操作首页的话题进行回复
        :return:
        """
        self.driver.find_element_by_xpath('//*[@class="nav pull-right"]/li[1]/a').click()#点击首页
        while True:
            res = self.driver.find_element_by_xpath('//*[@id="topic_list"]//a[@class="topic_title"]')
            context = res.text
            if context == '肯德基活动今天数据库炸了~~~':
                break
        res.click()
        ele=self.driver.find_element_by_xpath('//*[@class="CodeMirror-scroll"]')
        action=ActionChains(self.driver)
        action.move_to_element(ele).click().pause(3).send_keys('雷霆嘎巴').perform()
        self.driver.find_element_by_xpath('//*[@value="回复"]').click()

    def pub_func_topic(self,topic_value):
        """
        封装回复话题或发布话题公共方法
        :return:
        """
        ele = self.driver.find_element_by_xpath('//*[@class="CodeMirror-scroll"]')
        #因为定位到的文本是textarea，不是平常见到的input标签，所以需要模拟人为操作
        ele.click()  # 首先获取焦点
        action=ActionChains(self.driver)
        action.move_to_element(ele).click().pause(3).send_keys(topic_value).perform()#pause是暂停的功能，最后需要调用perform()来执行
        '''
                模拟快捷键：ctrl+a,ctrl+b
                '''
        # action.move_to_element(ele).click()
        # action.key_down(Keys.CONTROL).send_keys('a')
        # action.key_up(Keys.CONTROL)
        # action.key_down(Keys.CONTROL).send_keys('b')
        # action.key_up(Keys.CONTROL)
        # action.perform()
        self.driver.find_element_by_xpath('//*[@class="span-primary submit_btn"]').click()

if __name__ == '__main__':
    login_first_page().test_login_in('test60','123456')
    action=TopicAction()
    action.add_topic('hello world','world hello')