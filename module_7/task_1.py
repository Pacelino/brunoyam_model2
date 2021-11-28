
import requests
from bs4 import BeautifulSoup

import lxml
import re



url = 'https://mfd.ru/currency/?currency=USD'
header = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:94.0) Gecko/20100101 Firefox/94.0',
          'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8'}
# req = requests.get(url=url, headers=header)
# with open('usd.html', 'w') as file:
#     file.write(req.text)
with open('usd.html', 'r') as file:
    src = file.read()

soup = BeautifulSoup(src, 'lxml')
item_list = []
date_l = []
number_l = []
test = soup.find(class_ = "mfd-table mfd-currency-table").find_all('td')
for item in test:
    item_text = item.text.strip()
    date = re.findall(r'с \d\d\.\d\d\.\d\d\d\d', item_text)
    number = re.findall(r'[7,6]\d\.\d\d\d\d', item_text)
    item_list.append(item_text)
    date_l.extend(date)
    number_l.extend(number)
print(number_l)
print(date_l)

# top_table = soup.find(class_ = "mfd-table mfd-currency-table").find_all('th')
# for i in top_table:
#     table_text = i.text
#     print(table_text)


