import pytest
'''
除了使用tmp.py中的方式，也可以使用下面这个
定义func函数为函数级别的参数，运行时，在下面定义测试用例的时候，需要用到函数执行时，只需要在测试用例的参数中引用即可
例如test_03(func),test_01(func),func为@pytest.fixture运行时配置,其中，执行之前和执行之后使用yield隔开，yield是用例执行后再执行的

scope='module'-->模块级别 
scope='session'-->所有文件执行前后操作
pytest -s -v tmp2.py
'''

@pytest.fixture()#默认function
def func(fix_session,module,fix_class):
    print('....function set up--- ')
    yield
    print('---function teardown---')

@pytest.fixture(scope='module')
def module():
    print('---module setup---')
    yield
    print('---module teardown---')

@pytest.fixture(scope='class')
def fix_class():
    print('---set up class---')
    yield
    print('---tear down class---')

@pytest.fixture(scope='session')
def fix_session():
    print('---set up session---')
    yield
    print('---tear down session---')

class TestTmp2:
    def test_01(self,func):
        print('---test_01---')

    def test_02(self,func):
        print('---test02---')

class Testtm:
    def test_1(self,func):
        print('----test_1----')