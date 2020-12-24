import os

def get_screen_shot():
    dirname = os.path.dirname(os.path.dirname(__file__))
    """
    如果项目根目录下不存在screenshoots目录，那么就创建一个
    :return:screenshoots的绝对路径
    """
    screen_dir=os.path.join(dirname+'\\','screenshoots')
    if not os.path.exists(screen_dir):
        screen_dir=os.makedirs(screen_dir)
    return screen_dir
def get_png_file_name():
    """
    返回文件名
    :return:
    """

    pass

get_screen_shot()