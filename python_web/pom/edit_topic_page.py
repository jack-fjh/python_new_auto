from common.singdriver import demo_driver
class EditTopicPage():
    def __init__(self):
        self.driver=demo_driver()
    @property
    def breadcrumb(self):
        '''
        编辑话题文本
        :return:
        '''
        return self.driver.find_element_by_xpath('//*[@class="breadcrumb"]/li[@class="active"]').text

    @property
    def error_msg_text(self):
        '''
        获取标题值不能为空的文本
        :return:
        '''
        return self.driver.find_element_by_xpath('//*[@id="content"]//div[@class="inner post"]//strong').text
    @property
    def alert_msg_text(self):
        '''
        切换到弹框，也就是alert
        获取文本，alert.text
        点击确定，alert.accept()
        :return:
        '''
        alert=self.driver.switch_to.alert#切换到alert
        text=alert.text
        alert.accept()
        return text


