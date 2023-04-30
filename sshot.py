import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from urllib.parse import urlunsplit
from urllib.parse import urlparse

def deal_url(url):
    scheme,netloc,path,params,query,fragment=urlparse(url)
    if scheme=="https":
        pass
    else:
        scheme='http'
    url=urlunsplit([scheme,netloc+path,params,query,fragment])
    return url

def get_image(driver,url, pic_name):
    """
    #设置chrome开启的模式，headless就是无界面模式
    # 创建一个参数对象，用来控制chrome以无界面模式打开
    :param url:             获取获取网页的地址
    :param pic_name:        需要保存的文件名或路径＋文件名
    :return:
    """
    url=deal_url(url)
    # 打开网页
    driver.get(url)
    # driver.maximize_window()
    # 加延时 防止未加载完就截图
    time.sleep(2)
    # 用js获取页面的宽高，如果有其他需要用js的部分也可以用这个方法
    width = driver.execute_script("return document.documentElement.scrollWidth")
    height = driver.execute_script("return document.documentElement.scrollHeight")
    # 获取页面宽度及其宽度
    print(width,height)
    # 将浏览器的宽高设置成刚刚获取的宽高
    driver.set_window_size(width, height)
    time.sleep(1)
    # 截图
    driver.get_screenshot_as_file(pic_name)
    driver.set_window_size(800, 600)
    

#需要的东西
# chrome_options = Options()
# chrome_options.add_argument('--headless')
# chrome_options.add_argument('--disable-gpu')
# # 创建浏览器对象
# #     driver = webdriver.Chrome(executable_path='./chromedriver', chrome_options=chrome_options)
# driver = webdriver.Chrome(options=chrome_options)

# url_str = 'www.baidu.com'

# pic_name = r'qwq.png'

# get_image(driver,url_str, pic_name)

# driver.quit()