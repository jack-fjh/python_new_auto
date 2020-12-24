import pytest
'''
autouse=True:可以自动加载
'''
@pytest.fixture(autouse=True)
def fix_func():
    print('---func set up ---')
    yield
    print('---func tear down ---')

@pytest.fixture(scope='class',autouse=True)
def fix_class():
    print('---class set up ---')
    yield
    print('---class tear down ---')

@pytest.fixture(scope='module',autouse=True)
def fix_module():
    print('---module set up ---')
    yield
    print('---module tear down ---')

# class TestTmp2:
#     def test_01(self):
#         print('---test_01---')
#
#     def test_02(self):
#         print('---test02---')

def test_01():
    print('---test_01---')

def test_02():
    print('---test02---')