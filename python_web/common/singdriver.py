from selenium import webdriver
class demo_driver(object):

    # @classmethod
    # def test_driver(self):
    #     driver=webdriver.Chrome()
    #     driver.get('http://49.233.108.117:3000/signin')
    #     driver.maximize_window()
    #     driver.implicitly_wait(10)
    #     return driver

    '''
    单例模式：统一管理浏览器的实例
    
    '''
    __instance=None

    def __new__(cls, *args, **kwargs):
        """
        new：对象实例化自动调用
        :param args:
        :param kwargs:
        :return:
        """
        if cls.__instance is None:
            cls.__instance=webdriver.Chrome()
            cls.__instance.get('http://49.233.108.117:3000/signin')
        cls.__instance.implicitly_wait(10)
        cls.__instance.maximize_window()
        return cls.__instance



