import requests
from bs4 import BeautifulSoup
# from selenium import webdriver

# option = webdriver.ChromeOption()
# # I use the following options as my machine is a window subsystem linux.
# # I recommend to use headless option at least, out of the 3
# option.add_argument('--headless')
# option.add_argument('--no-sandbox')
# option.add_argument('--disable-dev-sh-usage')
# # Replace YOUR-PATH-TO-CHROMEDRIVER with your chromedriver location
# driver = webdriver.Chrome('/Users/efrainlemus-martinez/Downloads/chromedriver', options=option)

page = requests.get('https://seekingalpha.com/symbol/TSLA/analysis') # getting page HTML through request
# driver.get('https://www.imdb.com/chart/top/') # getting page HTML through request
soup = BeautifulSoup(page.content, 'html.parser') # parsing content through beautiful soup

titles = soup.select('.post-list-item-title') # selecting all of the anchor with titles
dates = soup.select('.wkL.wkF') # selecting all of the anchor with titles
first10 = titles[:10] # keep only the first 10 anchors
dates10 = dates[:10] # keep only the first 10 anchors
# for anchor in first10:
    # print(anchor.text) # display the inner text of each anchor

for f, b in zip(first10, dates10):
    print('Movie name: ' + f.text + ' and Movie date: ' + b.text)
# for date in dates10:
#     print(date.text) # display the inner text of each anchor

# first_link=driver.find_elements_by_css_selector('table tbody tr td.titleColumn a')[0]
# first_link.click()