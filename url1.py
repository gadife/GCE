import urllib
import re


#url = 'https://www.google.com/finance?cid=659701'
stocks = ['https://www.google.com/finance?cid=659701','https://www.google.com/finance?q=NASDAQ%3AGOOGL&ei=ZPWGVsm-DdCDsAGow4b4Cg', 'https://www.google.com/finance?cid=718288']

#info = webfile.info()

for stock in stocks:
  webfile = urllib.urlopen(stock)
  for line in webfile:
    if line.find('<meta itemprop="tickerSymbol"')>=0:
      name_raw = webfile.next()
      name = re.search(r'"\w+',name_raw)
      name_final = name.group()
      name_final = name_final[1:]
    if line.find('<meta itemprop="price"') >= 0: 
      #print line
      price_raw = webfile.next()
      price = re.search(r'\d+.\d+',price_raw)
      print name_final + ' price: ' + price.group()
    
    

#print webfile.read()
