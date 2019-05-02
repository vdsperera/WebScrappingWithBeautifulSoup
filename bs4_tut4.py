import bs4 as bs
import urllib.request

source = urllib.request.urlopen('http://pythonprogramming.net/parsememcparseface/')
soup = bs.BeautifulSoup(source, 'lxml')
js_test = soup.find('p', class_ = 'jstest')
print(js_test.text)