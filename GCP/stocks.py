import urllib
import re
import webapp2

#url = 'https://www.google.com/finance?cid=659701'


class MainPage(webapp2.RequestHandler):
  def get (self):
    #self.response.headers['Content-Type'] = 'text/html; charset=utf-8'
    stocks_list = ['https://www.google.com/finance?cid=659701','https://www.google.com/finance?q=NASDAQ%3AGOOGL&ei=ZPWGVsm-DdCDsAGow4b4Cg', 'https://www.google.com/finance?cid=718288']
    self.response.write('<html><body>')
    self.response.write('<h1>My Stocks app</h1>')
    for stock in stocks_list:
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
            #print name_final + ' price: ' + price.group()
            #self.response.write(name_final + ' price: ' + price.group() + ' | ')
            self.response.write('<p>stock ' + name_final + ': ' + price.group() + '<br />')
    self.response.write('</p></body></html>')

app = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)


