from pymongo import MongoClient
from selenium import webdriver

from flask import Flask, render_template, jsonify, request
import requests
from bs4 import BeautifulSoup
import time
app = Flask(__name__)

client = MongoClient('localhost', 27017)
db = client.stock


#
# def get_url():
#     headers = {
#         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
#     data = requests.get('https://finance.yahoo.com/most-active', headers=headers)
#
#     soup = BeautifulSoup(data.text, 'html.parser')
#
#     name = soup.select('//*[@id="quote-header-info"]/div[2]/div[1]/div[1]/h1')
#
#     return name
#
# def pharm_stock(name) :
#
#     headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
#     stock_data = requests.get('https://finance.yahoo.com/most-active',headers=headers)
#     soup = BeautifulSoup(stock_data.text, 'html.parser')
#
#     stock = soup.select_one('//*[@id="quote-header-info"]/div[3]/div[1]/div/span[1]')
#     return stock
#
# def pharm_trial(name) :
#     headers = {
#         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
#     stock_data = requests.get('https://finance.yahoo.com/most-active', headers=headers)
#     soup = BeautifulSoup(stock_data.text, 'html.parser')
#     trial = soup. select_one('//*[@id="theDataTable"]/tbody/tr[1]/td[4]/a')


# list={
#     'name':name,
#     'stock':stock,
#     'trial':trial,
# }
#
# db.pharm.insert_one(list)


@app.route('/')
def home():
    return render_template('index.html')

#API  역할
@app.route('/api/stock_list', methods=['GET'])
def company_stock():

    print("test")
    site1 = 'https://finance.yahoo.com/quote/PFE?p=PFE&.tsrc=fin-srch'
    site2 = 'https://finance.yahoo.com/quote/RHHBY?p=RHHBY&.tsrc=fin-srch'
    # 타겟 URL을 읽어서 HTML를 받아오고,
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
    b = requests.get(site1, headers=headers)

    # HTML을 BeautifulSoup이라는 라이브러리를 활용해 검색하기 용이한 상태로 만듦
    # soup이라는 변수에 "파싱 용이해진 html"이 담긴 상태가 됨
    # 이제 코딩을 통해 필요한 부분을 추출하면 된다.
    a = BeautifulSoup(b.text, 'html.parser')

    print(a.select_one('#quote-header-info > div.My\(6px\).Pos\(r\).smartphone_Mt\(6px\) > div.D\(ib\).Va\(m\).Maw\(65\%\).Ov\(h\) > div > span.Trsdu\(0\.3s\).Fw\(b\).Fz\(36px\).Mb\(-4px\).D\(ib\)').text)
    stock_number = a.select_one('#quote-header-info > div.My\(6px\).Pos\(r\).smartphone_Mt\(6px\) > div.D\(ib\).Va\(m\).Maw\(65\%\).Ov\(h\) > div > span.Trsdu\(0\.3s\).Fw\(b\).Fz\(36px\).Mb\(-4px\).D\(ib\)').text
    print(a.select_one('#quote-header-info > div.My\(6px\).Pos\(r\).smartphone_Mt\(6px\) > div.D\(ib\).Va\(m\).Maw\(65\%\).Ov\(h\) > div > span.Trsdu\(0\.3s\).Fw\(500\).Pstart\(10px\).Fz\(24px\).C\(\$negativeColor\)').text)
    percent = a.select_one('#quote-header-info > div.My\(6px\).Pos\(r\).smartphone_Mt\(6px\) > div.D\(ib\).Va\(m\).Maw\(65\%\).Ov\(h\) > div > span.Trsdu\(0\.3s\).Fw\(500\).Pstart\(10px\).Fz\(24px\).C\(\$negativeColor\)').text
    print(a.select_one('#quote-header-info > div.Mt\(15px\) > div.D\(ib\).Mt\(-5px\).Mend\(20px\).Maw\(56\%\)--tab768.Maw\(52\%\).Ov\(h\).smartphone_Maw\(85\%\).smartphone_Mend\(0px\) > div.D\(ib\) > h1').text)
    company_name = a.select_one('#quote-header-info > div.Mt\(15px\) > div.D\(ib\).Mt\(-5px\).Mend\(20px\).Maw\(56\%\)--tab768.Maw\(52\%\).Ov\(h\).smartphone_Maw\(85\%\).smartphone_Mend\(0px\) > div.D\(ib\) > h1').text

    driver = webdriver.Chrome("./chromedriver")

    # "Google"에 접속한다



    site1_trial = 'https://clinicaltrials.gov/ct2/results?cond=COVID&term=&type=&rslt=&age_v=&gndr=&intr=&titles=&outc=&spons=pfizer&lead=&id=&cntry=&state=&city=&dist=&locn=&rsub=&strd_s=&strd_e=&prcd_s=&prcd_e=&sfpd_s=&sfpd_e=&rfpd_s=&rfpd_e=&lupd_s=&lupd_e=&sort='
    driver.get(site1_trial)

    time.sleep(3)

    d = BeautifulSoup(driver.page_source, 'html.parser')
    print(d.select('#theDataTable > tbody > tr'))
    print(len(d.select('#theDataTable > tbody > tr')))
    number_trial = len(d.select('#theDataTable > tbody > tr'))
    print(d.select('#theDataTable > tbody > tr:nth-child(1) > td:nth-child(3) > span'))

    driver.quit()

    # headers = {
    #     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
    # c = requests.get(site1_trial, headers=headers)
    # d = BeautifulSoup(c.text, 'html.parser')

    # print("ll")
    # print(d.select('#theDataTable > tbody > tr'))
    # print("hhhh")
    # trial_list = list(d.select('#theDataTable > tbody > tr'))
    # print(list(trial_list))

    return jsonify({'company_name': company_name, 'stock' : stock_number, 'percent': percent, 'number_trial':number_trial})

# def company_trial():
#     site1_trial='https://clinicaltrials.gov/ct2/results?cond=COVID&term=&type=&rslt=&age_v=&gndr=&intr=&titles=&outc=&spons=pfizer&lead=&id=&cntry=&state=&city=&dist=&locn=&rsub=&strd_s=&strd_e=&prcd_s=&prcd_e=&sfpd_s=&sfpd_e=&rfpd_s=&rfpd_e=&lupd_s=&lupd_e=&sort='
#     headers = {
#         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
#     c = requests.get(site1_trial, headers=headers)
#     d = BeautifulSoup(c.text, 'html.parser')
#
#     print("ll")
#     print(d.select('#theDataTable > tbody > tr'))
#     print("hhhh")
#     trial_list = list(d.select('#theDataTable > tbody > tr'))
#     print(list(trial_list))

# #API  역할
# @app.route('/list', methods=['GET'])
# def company_stock():
#     stocks=list(db.stock.find())
#     return jsonify({'result':'success','stock_list': stocks })
#

# #theDataTable > tbody > tr
# [<> <>]
#list_a = [1,3,7]
#len(list_a)
if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
