import pytest,os
from common.singdriver import demo_driver
from business.user import UserAction
from business.usercenter import UserCenter
from business.topics import TopicAction
from pom.edit_topic_page import EditTopicPage
from common.do_data import do_csv

driver=demo_driver()
userAction=UserAction()
userCenter=UserCenter()
topic=TopicAction()
edittopicPage=EditTopicPage()

@pytest.fixture(scope='module',autouse=True)
def module():
    # 1:登录
    userAction.user_login('test60', '123456')
    yield
    driver.quit()

data_file_path=os.path.dirname(os.path.dirname(__file__))
file_path=os.path.join(data_file_path+'/','data/data1.csv')
testdata=do_csv(file_path)
test_title=['title is None','content is None']

@pytest.fixture(params=testdata,ids=test_title)
def data(request):
    '''
    数据传参的时候，主要是作为不同数据的不同解释
    :param request: 
    :return: 
    '''
    return  request.param


def test_topic_ex(data):

    topic.add_topic(data[0],data[1])
    page_text=edittopicPage.error_msg_text
    assert page_text==data[2]

    # alert_text=edittopicPage.error_msg_text
    # assert alert_text==data[2]