from common.singdriver import demo_driver


class UserCenterPage(object):
    driver=demo_driver()

    def click_personal(self):
        '''
        点击头像进行个人中心
        :return:
        '''
        return self.driver.find_element_by_xpath('//div[@class="user_card"]//span[@class="user_name"]/a')

    def current_create_topic(self):
        '''
        选举第一个最近创建的话题
        :return:
        '''
        return self.driver.find_element_by_xpath('//*[@id="main"]//div[@class ="panel"][2]/div[@class ="cell"][1]//div[@class="topic_title_wrapper"]/a')