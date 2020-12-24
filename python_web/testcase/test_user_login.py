from business.login import login_first_page
from business.topics import TopicAction

def test_login():
    '''
    登录
    :return:
    '''
    login=login_first_page()
    login.test_login_in('test60','123456')
    '''
    发表话题
    '''
    topic=TopicAction()
    # topic.add_topic()
    '''
    回复话题
    '''
    topic.reply_topic()