import requests
from bs4 import BeautifulSoup
import codecs,queue,threading

def ying_cai_wang(i):                 #英才网
    url= 'http://hr.eyuyao.com/search/job/?k=外贸&t=00&d=180'
    for num in range(1, i+1):
        response = requests.get(url='http://hr.eyuyao.com/search/job/?k=外贸&t=00&d=180&page=' + str(num))

        soup = BeautifulSoup(response.text,'lxml')
        soup = soup.find_all(class_='xSLE')
        for i in soup:
            print(i.text)
            yin_cai_wang=[]
            yin_cai_wang.append(i)
    yin_cai_wang=list(set(yin_cai_wang))
    return  yin_cai_wang

def yuyao(i):                      #余姚人才网
    for j in range(1,i+1):
        response = requests.get(url="http://www.yyrc.com/job/?JobType=0&WorkPlace=0&Trade=0&Property=0&JobProperty=0&Degree=0&WorkYears=0&Sex=0&MonthPay=0&PublishDate=0&Key=%CD%E2%C3%B3&Orderid=0&Styleid=2&PageNo="+str(j))
        soup =  BeautifulSoup(response.text,'lxml')
        yuyao_list = []
        soup = soup.find_all(attrs='li',class_='seaList13')
        for k in soup:
            print(k.text)
            yuyao_list.append(k.text)
    yuyao_list=list(set(yuyao_list))
    return yuyao_list


def ci_xi_ren_cai_wang (i):           #慈溪人才网
    for j in range(1,i+1):
        response = requests.get(url='http://www.cxhr.com/search/jobList.jsp?curpage='+str(j)+'&&keywords=外贸')
        soup = BeautifulSoup(response.text,'lxml')
        soup = soup.find_all(class_='coname')
        ci_xi_ren_cai_wang_list =[]
        for i  in soup:
            ci_xi_ren_cai_wang_list.append(i.text)
            print(i.text)
    ci_xi_ren_cai_wang_list=list(set(ci_xi_ren_cai_wang_list))
    return ci_xi_ren_cai_wang_list

def wu_ba_tong_cheng_yu_yao(i):           #58余姚人才
    for j in range(1,i+1):
        response = requests.get(url='http://yuyao.58.com/job/pn3/?key=外贸&final=1&jump=1&PGTID=0d302408-014d-5d88-19fb-1bbd43ee0802&ClickID='+str(j))
        soup = BeautifulSoup(response.text,'lxml')
        soup = soup.find_all(class_='fl',target="_blank")
        wu_ba_tong_cheng_list =[]
        for i  in soup:
            wu_ba_tong_cheng_list.append(i.text)
            print(i.text)
    wu_ba_tong_cheng_list=list(set(wu_ba_tong_cheng_list))
    return wu_ba_tong_cheng_list

def wu_ba_tong_cheng_ci_xi(i):           #58余姚人才
    for j in range(1,i+1):
        response = requests.get(url='http://cixi.58.com/job/pn2/?key=外贸&final=1&jump=1&PGTID=0d302408-014d-698e-27b5-f2fb229b775c&ClickID='+str(j))
        soup = BeautifulSoup(response.text,'lxml')
        soup = soup.find_all(class_='fl',target="_blank")
        wu_ba_tong_cheng_list_ci_xi =[]
        for i  in soup:
            wu_ba_tong_cheng_list_ci_xi.append(i.text)
            print(i.text)
    wu_ba_tong_cheng_list_ci_xi = list(set(wu_ba_tong_cheng_list_ci_xi))
    return wu_ba_tong_cheng_list_ci_xi



def xian_shi(name,list_1):
    yi_cun_zai=[]
    yao_xian_shi_de_ =[]
    txt = codecs.open(str(name)+'mulu.txt', 'r', 'utf-8')
    yi_cun_zai = [k.strip() for k in txt]
    txt.close()
    txt = codecs.open(str(name)+'mulu.txt', 'r', 'utf-8')

    for j in list_1:
            if j in yi_cun_zai:
                continue
            else:
                #print(j)
                yao_xian_shi_de_.append(j)
                txt.write(j+'\r\n')
    txt.close()
    return yao_xian_shi_de_
