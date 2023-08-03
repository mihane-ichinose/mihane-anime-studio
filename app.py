### 作者：Mihane_Ichinose
### 仅用于个人

import requests
from bs4 import BeautifulSoup
import time
import cn2an
import re, json
from flask import Flask, render_template, request

app = Flask(__name__)

version = "2.2"
m_version = "2.2"
year = time.strftime("%Y", time.localtime())

@app.route('/', methods = ['POST', 'GET'])
def index():
    return render_template('index.html', version=version, year=year)

@app.route('/animelist', methods = ['POST', 'GET'])
def animelist():
    method = request.form.get("filterInput")
    if method == 'filtered':
        print("智能过滤模式")

# create = True #修改此变量，是否新建html

    update_time = time.strftime("%Y-%m-%d %H:%M UTC", time.localtime())

    # date = time.strftime("%Y-%m-%d", time.localtime()) #日期戳，用于区分文件名
    # html_head ="""
    # <!DOCTYPE html>
    # <html lang="en">
    # <head>
    #     <meta charset="UTF-8">
    #     <title>AGE动画每周更新番组列表 """+date+"""</title>
    # </head>
    # <body>
    #   <table width="100%" border="1" cellspacing="0">
    #     <thead>
    #         <tr>
    #             <th colspan="4">AGE动画每周更新番组列表 """+date+"""</th>
    #         </tr>
    #     </thead>
    #     <tr>
    # 	    <th width="25%">番组名</th>
    # 	    <th width="25%">集数</th>
    #         <th width="25%">AGE链接</th>
    #         <th width="25%">更新时间</th>
    #     </tr>
    # """
    # if(create):
    #     f = open('age番表 '+date+'.html','w',encoding="utf-8")
    #     f.write(html_head)
    #     f.close()
        
    # proxy = {
    #    'http': 'http://localhost:8080',
    #    'https': 'https://localhost:8080'
    # }

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.0; WOW64; rv:24.0) Gecko/20100101 Firefox/24.0'
    }

    url = 'https://agemys.org'

    print("欢迎使用针对AGE动漫首页每周放送列表（番表）的爬虫系统！版本V0.2")
    print("新版AGEMYS.ORG首页适配完毕，日期2023.8.4")
    print("正在获取数据......")

    strhtml = requests.get(url=url, headers=headers) #Get方式获取网页数据
    soup = BeautifulSoup(strhtml.text, "lxml")

    strhtml = requests.get(url=url, headers=headers) #Get方式获取网页数据
    soup = BeautifulSoup(strhtml.text, "lxml")

    total_index = 7

    weekday_title_list = [[s for a in soup.select("#week-0-pane .pe-2 a") for s in a.stripped_strings],
    [s for a in soup.select("#week-1-pane .pe-2 a") for s in a.stripped_strings],
    [s for a in soup.select("#week-2-pane .pe-2 a") for s in a.stripped_strings],
    [s for a in soup.select("#week-3-pane .pe-2 a") for s in a.stripped_strings],
    [s for a in soup.select("#week-4-pane .pe-2 a") for s in a.stripped_strings],
    [s for a in soup.select("#week-5-pane .pe-2 a") for s in a.stripped_strings],
    [s for a in soup.select("#week-6-pane .pe-2 a") for s in a.stripped_strings]]

    weekday_href_list = [[a['href'] for a in soup.select("#week-0-pane .pe-2 a")],
    [a['href'] for a in soup.select("#week-1-pane .pe-2 a")],
    [a['href'] for a in soup.select("#week-2-pane .pe-2 a")],
    [a['href'] for a in soup.select("#week-3-pane .pe-2 a")],
    [a['href'] for a in soup.select("#week-4-pane .pe-2 a")],
    [a['href'] for a in soup.select("#week-5-pane .pe-2 a")],
    [a['href'] for a in soup.select("#week-6-pane .pe-2 a")]]

    weekday_ji_list = [[s for div in soup.select("#week-0-pane .title_sub") for s in div.stripped_strings],
    [s for div in soup.select("#week-1-pane .title_sub") for s in div.stripped_strings],
    [s for div in soup.select("#week-2-pane .title_sub") for s in div.stripped_strings],
    [s for div in soup.select("#week-3-pane .title_sub") for s in div.stripped_strings],
    [s for div in soup.select("#week-4-pane .title_sub") for s in div.stripped_strings],
    [s for div in soup.select("#week-5-pane .title_sub") for s in div.stripped_strings],
    [s for div in soup.select("#week-6-pane .title_sub") for s in div.stripped_strings]]

    # print(weekday_ji_list)

    # blockcontent = soup.select("div[class*=blockcontent]")
    # script = blockcontent[0].find("script")

    # pattern = re.compile(r"var new_anime_list = (.*?);", re.MULTILINE | re.DOTALL) #在对应javascript中获取变量
    # new_anime_list = pattern.search(script.string)
    # new_anime_list_json = json.loads(new_anime_list.groups()[0])

    title_list = []
    ji_list = []
    day_list = []
    href_list = []

    # 从0-6：周日到周六遍历列表
    for day in range(total_index):
        # 遍历每一天的列表（默认列表无空）
        for i in range(len(weekday_title_list[day])):
            # 集数
            ji = weekday_ji_list[day][i]
            # 智能过滤：去除带完结且无更新时间的番剧
            if method == 'filtered':
                if "完结" in ji and len(ji.split()) == 1:
                    continue
            if ji == "第集":
                ji_list.append("未更新")
            else:
                ji_list.append(ji)
            # 番组名称
            title_list.append(weekday_title_list[day][i])
            # AGEFANS内部动画链接列表
            href_list.append(weekday_href_list[day][i])
            if day == 0:
                day_list.append("星期日")
            else:
                day_list.append("星期"+cn2an.an2cn(str(day)))
    
    anime_list = list(zip(title_list, ji_list, href_list, day_list))
    # print(anime_list)

    # try:
    #     title_list = soup.select("ul#new_anime_page a#one_new_anime_name") #中文番剧名称
    # except:
    #     title_list = []

    # try:
    #     ji_list = soup.select("ul#new_anime_page a#one_new_anime_ji") #对应集数
    # except:
    #     ji_list = []

    # for i in range(len(title_list)):
        
    #     title = title_list[i]
    #     ji = ji_list[i]
    #     id = id_list[i]
    #     daystr = day_list[i]

    #     #为符合格式，自动将期转换为季
    #     for an in range (100):
    #         cn = cn2an.an2cn(str(an))
    #         title = title.replace(str(an)+"期", str(cn)+"季")
        
    #     print(title+", "+ji+", "+id+", "+daystr)

    #     html_row ="""
    #         <tr>
    #             <td style='text-align:center;'>"""+title+"""</td>
    #             <td style='text-align:center;'>"""+ji+"""</td>
    #             <td style='text-align:center;'><a href='https://www.agemys.com/detail/"""+id+"""' target='_blank'>"""+id+"""</a></td>
    #             <td style='text-align:center;'>"""+daystr+"""</td>
    #         </tr>
    #     """

    #     f = open('age番表 '+date+'.html','a+',encoding="utf-8")
    #     f.write(html_row)
    #     f.close()

    # html_tail ="""
    # </body>
    # </html>
    # """

    # f = open('age番表 '+date+'.html','a+',encoding="utf-8")
    # f.write(html_tail)
    # f.close()

    # print("完成列表生成！共生成"+str(len(title_list))+"个条目！")

    return render_template("animelist.html",
    anime_list=anime_list,
    update_time=update_time,
    version=version,
    m_version=m_version,
    year=year,
    method=method)

@app.route('/m', methods = ['POST', 'GET'])
def m():
    return render_template("m.html",
    version=version,
    m_version=m_version,
    year=year)

if __name__ == '__main__':
   app.run()