from bs4 import BeautifulSoup
import requests

# url = 'https://brownstocktrading.com/'
url = 'https://seekingalpha.com/api/sa/combined/TSLA.xml'
# url = 'https://seekingalpha.com/symbol/TSLA/analysis'
# url = 'https://seeking-alpha.p.rapidapi.com/analysis/TSLA/'
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')

# titles = soup.select('a.qfE')
# titles = soup.select('.wp-block-group .wp-block-post-title a')
titles = soup.select('item title') # seeking alpha rss feed
dates = soup.select('item pubDate') # seeking alpha rss feed
# titles = soup.select('.zcA.keA .ruA.bkA .ruI .ruB .ruE') # seeking alpha actual analysis page

titlesAll = titles[:]
datesAll = dates[:]

# for anchor in titlesAll:
#     # print('hello')
#     print(anchor.text)

for title, date in zip(titlesAll, datesAll):
    print('Title: ' + title.text + ' - Published on: ' + date.text)


# print(titles)

# news = soup.find(name="ul", attrs={'class':'item-list','id':'latest-news-list'})
# root = 'https://seekingalpha.com'

# root = 'https://seekingalpha.com'

# id_list = [i.text for i in news.find_all(name='li',attrs={'class':'item'})]
