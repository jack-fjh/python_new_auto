from pom.usercenter_page import UserCenterPage
class UserCenter(object):

    def __init__(self):
        self.user_center_page=UserCenterPage()

    def click_current_create_topic_by_index(self):
        '''
        点击个人中心的第几个话题
        :param index:
        :return:
        '''
        self.user_center_page.click_personal().click()
        self.user_center_page.current_create_topic().click()
