!pip install selenium
from selenium import webdriver
from time import sleep
from bs4 import BeautifulSoup
from selenium.webdriver.support.ui import WebDriverWait
import re
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import csv
import re

#%%
browser=webdriver.Chrome()
browser.get('https://www.youtube.com/channel/UC9i2Qgd5lizhVgJrdnxunKw/videos')
browser.maximize_window()
# browser.find_element_by_xpath("/html/body/div[5]/div/div[3]/button[2]").click() 
#browser.find_element_by_id('video-title')
# browser.find_element_by_id('select_location02').send_keys('Taipei')
# browser.find_element_by_id('typesofticket').send_keys('One-Way')
# browser.find_element_by_id('Departdate01').send_keys('2021-04-21')
# browser.find_element_by_id('outWardTime').send_keys('09:30')
# browser.find_element_by_xpath('//*[@id="index-tab-01"]/div/div[4]/div/button').send_keys('College Student')
#%%
with open('output.csv', 'w', newline='') as csvfile:
  # 建立 CSV 檔寫入器
  writer = csv.writer(csvfile)
  # 寫入一列資料
  writer.writerow(['title', 'viewcount','img'])
# browser.find_element_by_id('start-search').click()
sleep(30)
soup = BeautifulSoup(browser.page_source, 'html.parser')
#sleep(1)
title=soup.find_all('a', id='video-title')
title_link=soup.find_all(id='video-title')
print(title_link)
img=soup.find_all(id='img')
count=soup.find_all('span',{'class':'style-scope ytd-grid-video-renderer'})
#%%
ptn = re.compile(r'(?<=[\v\=]).+')
video_id = []

for link in title_link:
    #print(link['href'])
    a = re.search(r'(?<=[\v\=]).+',link['href'])
    video_id.append(a.group())
print(len(video_id))

#print(ptn.findall(r'/watch?v=-T0yrWmNYZ7Q'))

#print(img)
img_src = []
i = 0
a = 0


for image in img:
    #print(image['src'])
    try:
        if re.match('https://i.ytimg.com/',image['src'])!= None:
            #print(image['src'])
            img_src.append(image['src'])
        else:
            print(image['src'])
            a = a+1
    except:
        i =i+1
        print(image)
#print(img)
print(len(img_src))
print(i)
print(a)
print(len(img))

print(len(title))
print(len(count))

print(len(soup))
print(len(title))
print(len(count))
print(count[1].text)
print(count[0].text)
longtime = []
b = 0
for i in range(len(title)):
    demo = count[2*i+1].text.replace(' ', '')
    print(demo)
    if re.match(r'\d+(?=[個年])',demo)!=None:
        if re.match(r'1個月',demo)!=None:
            longtime.append(0)
        else:
            longtime.append(1)
            b = b + 1
    else:
        longtime.append(0)

print(b)
#%%
import requests
import os
from PIL import Image
# r = requests.get(image_link).content
#  with open(f"{folder_name}/{title}images{i+1}.jpg", "wb+") as f:
#     f.write(r)


def getpic(video_id):
    #print(video_id)
    saveDir = './images1/'
    if not os.path.isdir(saveDir):
        os.mkdir(saveDir)
    picurl = 'https://img.youtube.com/vi/'+video_id+'/hqdefault.jpg'
    img = requests.get(picurl)
    with open(saveDir+video_id+'.jpg', 'wb') as f:
        f.write(img.content)
        print('success',video_id)
#%%
import re
#ptn = re.compile(r'\d+(?=[萬])')

# print(ptn.findall(r'2340萬'))
# a = re.match(r'\d+(?=[萬])',
# viewcount = int(ptn.findall(r'2340萬')[0])*1000
# #count[2*i].text
viewcount =[]
for i in range(len(title)):
    demo = count[2*i].text
    demo = demo.replace(' ', '')
    if re.search(r'\d+(?=[萬])',demo) != None:
        a = re.search(r'\d+(?=[萬])',demo).group()
        viewcount.append(int(a)*10000)
    else:
        print(demo)
        viewcount.append(int(re.search(r'\d+',demo).group()))
    
print(len(viewcount))

for i in range(len(title)):
    print(title[i]['title'])
    print(count[2*i].text)
    with open('output.csv', 'a', newline='',encoding="utf-8") as csvfile:
        # 建立 CSV 檔寫入器
        if longtime[i] == 1:
            writer = csv.writer(csvfile)
            writer.writerow([title[i]['title'],viewcount[i],video_id[i]])
            getpic(video_id[i])
