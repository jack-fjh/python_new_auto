
def setup_module():
    """
    文件中的所有测试用例运行之前执行
    :return:
    """
    print('----setup module----')

def teardown_module():
    """
        文件中的所有测试用例运行之前执行
        :return:
    """
    print('----tear down module----')


class Testtmp(object):
    def setup(self):
        print('---setup func---')

    def teardown(self):
        print('---tear down func ---')
        
    @classmethod
    def setup_class(self):
        print('---setup class---')

    @classmethod
    def teardown_class(self):
        print('---teardown class---')

    def test_03(self):
        print('---test_01---')

    def test_01(self):
        print('---test02---')
