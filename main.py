# For scraping we will use Beautiful SOUP
# request lib

import requests  # download html
from bs4 import BeautifulSoup  # allows us to use html
import pprint


res = requests.get('https://news.ycombinator.com/news')
soup = BeautifulSoup(res.text, 'html.parser')
# print(soup.body)
# print(soup.find_all('div')) #CSS selectors allows to grap the elements
# print(soup.select('.score')) # grabbing class
links = soup.select('.storylink')
# votes = soup.select('.score')
subtext = soup.select('.subtext')
# print(votes[0])
# print(votes[0].get('score_22073037'))


def sorted_with_votes(hnlist):
    return sorted(hnlist, key=lambda k: k['votes'], reverse=True)


def create_custom_hacker_news(links, subtext):
    hn = []
    for index, item in enumerate(links):

        title = item.getText()
        href = item.get('href', None)
        vote = subtext[index].select('.score')
        if len(vote):
            vpoints = int(vote[0].getText().replace('points', ''))
            if vpoints > 99:
                # Dictonary
                hn.append({'title': title, 'link': href, 'votes': vpoints})
    return sorted_with_votes(hn)


pprint.pprint(create_custom_hacker_news(links, subtext))
