import requests
import xlwt
from bs4 import BeautifulSoup
import pandas as pd
from time import sleep
#excelデータから場所の名前を取得
df = pd.read_excel('toshi.xlsx',header = 0)
print(df)
wait_time = 2.0
#データを格納
queries = []
for i in range(1,79):
    queries.append(df.iloc[i,79])
print(queries)
#新しいエクセルファイルを作成
book = xlwt.Workbook()
newsheet1 = book.add_sheet('NewSheet1') 

i = 0
for q in queries:
    url = 'https://www.geocoding.jp/?q={0}'.format(q)
    res = requests.get(url)
    soup = BeautifulSoup(res.content, "html.parser")
    print(soup)
    if "見つかりませんでした" not in str(soup):
        ido = soup.find_all('b')[1]
        keido = soup.find_all('b')[2]
        print(ido.get_text(), keido.get_text())
        newsheet1.write(i,2,ido.get_text())
        newsheet1.write(i,3,keido.get_text())
    i += 1
    #アクセス不可がかからないように2秒待つ
    sleep(wait_time)
book.save('geocoding.xls')