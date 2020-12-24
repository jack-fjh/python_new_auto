from common.singdriver import demo_driver

class UserAction(object):
    driver = demo_driver()
    # def __init__(self):
    #     self.driver=demo_driver()

    def user_login(self,username,password):
        """
        用户登录业务
        :param username:
        :param password:
        :return:
        """
        self.driver.find_element_by_xpath('//*[@name="name"]').send_keys(username)
        self.driver.find_element_by_xpath('//*[@name="pass"]').send_keys(password)
        self.driver.find_element_by_xpath('//*[@class="span-primary"]').click()

    def user_register(self):
        """
        用户注册业务
        :return:
        """
        login_name=self.driver.find_element_by_xpath('//*[@class="user_name"]/a').text
        if login_name:
            self.driver.find_element_by_xpath('//*[@data-method="post"]').click()
            self.driver.find_element_by_xpath('//*[@class="nav pull-right"]/li[5]/a').click()
            self.driver.find_element_by_xpath('//*[@id="loginname"]').send_keys('test007')
            self.driver.find_element_by_xpath('//*[@id="pass"]').send_keys('123456')
            self.driver.find_element_by_xpath('//*[@id="re_pass"]').send_keys('123456')
            self.driver.find_element_by_xpath('//*[@id="email"]').send_keys('18516735896@163.com')
            self.driver.find_element_by_xpath('//*[@class="span-primary"]').click()








