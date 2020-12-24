import pytest

from common.singdriver import demo_driver
from business.viewmanage import ViewManage
from business.user import UserAction
from business.topics import TopicAction
from business.usercenter import UserCenter
from common.utils import get_screen_shot
import time


driver=demo_driver()
user_action=UserAction()
view_manage=ViewManage()
topicpage=TopicAction()

@pytest.fixture(scope='module',autouse=True)
def module():
    '''
    所有的操作依赖登录，所有的用例执行之前应该先扽登录
    :return:
    '''
    user_action.user_login('test60', '123456')  # 1:先登录
    yield
    '''
    关闭浏览器
    '''
    driver.quit()

@pytest.fixture(scope='function',autouse=True)
def func():
    print('-------------begin func-----------')
    yield
    pic_dir_name = get_screen_shot()
    picture_name = time.strftime('%Y%m%d %H-%M-%S')
    driver.save_screenshot(pic_dir_name +'\\'+ picture_name + '.png')
    print('-------------end func-------------')
    '''
    这里的截图操作，可以放在module中最后执行，具体看各自需求
    '''




def test_newtopic():
    """
    创建新话题
    :return:
    """
    topicpage.add_topic()#2：新建话题



def test_updatetopic():
    UserCenter().click_current_create_topic_by_index()