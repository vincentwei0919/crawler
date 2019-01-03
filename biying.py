
import time
import urllib.request
import os
import bs4
import json
from bs4 import BeautifulSoup
import urllib.parse

save_path = 'X:\\人物数据'

def FindLink(PageNum, InputData, word):
    for i in range(PageNum):
        print(i)
        try:
            url = 'http://cn.bing.com/images/async?q={0}&first={1}&count=35&relp=35&lostate=r&mmasync=1&dgState=x*175_y*848_h*199_c*1_i*106_r*0'
            # 定义请求头
            agent = {
                'User-Agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.165063 Safari/537.36 AppEngine-Google."}
            page1 = urllib.request.Request(url.format(InputData, i * 35 + 1), headers=agent)
            page = urllib.request.urlopen(page1)
            #使用beautifulSoup进行解析网页
            soup = BeautifulSoup(page.read(), 'html.parser')
            # 创建文件夹
            if not os.path.exists(save_path + "\\" + word):
                os.mkdir(save_path+'\\' + word)

            for StepOne in soup.select('.mimg'):
                link = StepOne.attrs['src']
                count = len(os.listdir(save_path + '\\' + word)) + 1
                SaveImage(link, word, count)
        except:
            print('URL OPENING ERROR !')


def SaveImage(link,InputData,count):
    try:
        time.sleep(0.2)
        urllib.request.urlretrieve(link, save_path + '\\'+InputData+'\\'+str(count)+'.jpg')
    except Exception :
        time.sleep(1)
        print("产生未知错误，放弃保存")
    else:
        print("图+1,已有" + str(count) + "张图")



if __name__=='__main__':
    #输入需要加载的页数，每页35幅图像
    PageNum = 100
    #输入需要搜索的关键字
    word='艾莉亚史塔克'
    #UTF-8编码
    InputData=urllib.parse.quote(word)
    print(InputData)
    FindLink(PageNum,InputData,word)