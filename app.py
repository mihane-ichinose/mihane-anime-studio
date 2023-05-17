### 作者：Mihane_Ichinose
### 仅用于个人

import requests
from bs4 import BeautifulSoup
import time
import cn2an
import re, json, os
import psycopg2
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

version = "2.1beta1"
m_version = "2.1beta1"
year = time.strftime("%Y", time.localtime())

def get_db_connection():
    print('addr:',os.environ.get('DBADDR'))
    conn = psycopg2.connect(host=os.environ.get('DBADDR'),
                            port='5433',
                            database=os.environ.get('DBNAME'),
                            user=os.environ.get('DBUSER'),
                            password=os.environ.get('DBPASS'))
    return conn

@app.route('/', methods = ['POST', 'GET'])
def index():
    return render_template('index.html', version=version, year=year)

@app.route('/findAnimeById', methods=['POST'])
def findAnimeById():
    searchID = request.form['searchInput']
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM anime_name where index_no = '+searchID+';')
    anime_name = list(cur.fetchall()[0])
    cur.close()
    conn.close()
    anime_name_data = {
        'index_no':anime_name[0],
        'title_cn':anime_name[1],
        'title_jp':anime_name[2],
        'status':anime_name[3],
        'recommend':anime_name[4],
        'year':anime_name[5],
        'season':anime_name[6]
    }
    return jsonify(anime_name_data)

@app.route('/findAnimeByName', methods=['POST'])
def findAnimeByName():
    searchName = request.form['searchInput']
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM anime_name where title_cn ilike \'%'+searchName+'%\';')
    anime_names = cur.fetchall()
    cur.close()
    conn.close()
    anime_name_datum = []
    for anime_name in anime_names:
        anime_name_data = {
            'index_no':anime_name[0],
            'title_cn':anime_name[1],
            'title_jp':anime_name[2],
            'status':anime_name[3],
            'recommend':anime_name[4],
            'year':anime_name[5],
            'season':anime_name[6]
        }
        anime_name_datum.append(anime_name_data)
    print(anime_name_datum)
    return jsonify(anime_name_datum)

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

    url = 'https://agemys.com'

    print("欢迎使用针对AGE动漫首页每周放送列表（番表）的爬虫系统！版本V0.1")
    print("正在获取数据......")

    strhtml = requests.get(url=url, headers=headers) #Get方式获取网页数据
    soup = BeautifulSoup(strhtml.text, "lxml")

    blockcontent = soup.select("div[class*=blockcontent]")
    script = blockcontent[0].find("script")

    pattern = re.compile(r"var new_anime_list = (.*?);", re.MULTILINE | re.DOTALL) #在对应javascript中获取变量
    new_anime_list = pattern.search(script.string)
    new_anime_list_json = json.loads(new_anime_list.groups()[0])

    title_list = []
    ji_list = []
    day_list = []
    id_list = []

    for listing in new_anime_list_json:
        # 番组名称
        title = listing.get("name")
        # 集数
        ji = listing.get("namefornew")
        # AGEFANS内部动画ID
        id = listing.get("id")
        # 日期
        day = listing.get("wd")

        #智能过滤：去除带完结且无更新时间的番剧
        if method == 'filtered':
            if "完结" in ji and len(ji.split()) == 1:
                continue

        title_list.append(title)
        if ji == "第集":
            ji_list.append("未更新")
        else:
            ji_list.append(ji)
        id_list.append(id)
        if day == 0:
            day_list.append("星期日")
        else:
            day_list.append("星期"+cn2an.an2cn(str(day)))
        # print(listing.get("name"))
    
    anime_list = list(zip(title_list, ji_list, id_list, day_list))

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