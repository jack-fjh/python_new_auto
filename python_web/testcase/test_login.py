from common.singdriver import demo_driver
import pytest
class login_first_page(object):
    """
    业务：登录
    """
    driver=demo_driver()



    @pytest.fixture(params=[(None,'123456','用户或密码不能为空'),('testuser1',None,'用户或密码不能为空')])
    def user_data(request):
        return request.param



    def test_login_in(user_data):
        print(user_data)
        # self.driver.find_element_by_xpath('//*[@name="name"]').send_keys(username)
        # self.driver.find_element_by_xpath('//*[@name="pass"]').send_keys(password)
        # self.driver.find_element_by_xpath('//*[@class="span-primary"]').click()

