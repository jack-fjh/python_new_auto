import pytest
# from common.singdriver import demo_driver
# from business.user import UserAction
# from business.usercenter import UserCenter
# from business.topics import TopicAction
#
# driver=demo_driver()
# userAction=UserAction()
# userCenter=UserCenter()
# topic=TopicAction()

@pytest.fixture(scope='module',autouse=True)
def module():
    # 1:登录
    print('。。。。。登录成功。。。。。')
    yield
    # driver.quit()
    print('.....退出登录.....')

testdata=[
    ('share','1'),
    (None,'aaaaaaaa')
]
@pytest.fixture(params=testdata,ids=['title is None','content is None'])
def data(request):
    '''
    数据传参的时候，主要是作为不同数据的不同解释
    :param request:
    :return:
    '''
    return  request.param


def test_topic_ex(data):
    print('------>>>>>>',data[0],data[1])
