from common.singdriver import demo_driver

class login_first_page(object):
    """
    业务：登录
    """
    driver=demo_driver()
    def test_login_in(self,username,password):
        self.driver.find_element_by_xpath('//*[@name="name"]').send_keys(username)
        self.driver.find_element_by_xpath('//*[@name="pass"]').send_keys(password)
        self.driver.find_element_by_xpath('//*[@class="span-primary"]').click()

        # 添加断言
        # 1：登录成功应该跳转到首页
        current_url = self.driver.current_url
        current_name = self.driver.find_element_by_xpath('//*[@class="user_card"]//span/a').text
        assert current_url == 'http://49.233.108.117:3000/', '跳转首页失败'
        assert current_name == 'test60', '登录失败'