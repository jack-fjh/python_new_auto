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


def setup_module():
    '''
    所有的操作依赖登录，所有的用例执行之前应该先扽登录
    :return:
    '''
    user_action.user_login('test60', '123456')  # 1:先登录
def teardown_module():
    '''
    执行完所有的用例之后，关闭浏览器
    :return:
    '''
    driver.quit()

def teardown():
    '''
    每一条测试用例执行完之后，截屏
    :return:
    '''
    pic_dir_name=get_screen_shot().get_screen_shot()
    picture_name=time.strftime('%Y%m%d %H-%M-%S')
    driver.save_screenshot(pic_dir_name+picture_name+'.png')

def test_newtopic():
    """
    创建新话题
    :return:
    """
    topicpage.add_topic()#2：新建话题



def test_updatetopic():
    UserCenter().click_current_create_topic_by_index(1)