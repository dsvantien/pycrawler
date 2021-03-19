import requests
from bs4 import BeautifulSoup
import re
import json
import os.path
import concurrent.futures
file_store = './download/'
if not os.path.exists(file_store):
    os.makedirs(file_store)
news_lists = []
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36"}


def download_news(i):
    url = f'https://news.ycombinator.com/news?p={i}'
    res = requests.get(url, headers=headers)
    soup = BeautifulSoup(res.text, 'lxml')
    for item in soup.find_all('tr', class_='athing'):
        single_new_dict = {}
        link_tag = item.find('a', class_='storylink')
        link = link_tag.get('href') if link_tag else None
        title = link_tag.get_text(strip=True) if link_tag else None
        next_row = item.find_next_sibling('tr')
        score_tags = next_row.find('span', class_='score')
        score = score_tags.get_text(strip=True) if score_tags else '0 point'
        # comment_tag = next_row.find('a', string=re.compile(r'\d+(&nbsp;|\s)comment(s?)'))
        comment_tag = next_row.find('a', string=re.compile(r'(.*)comment(s?)'))
        raw_comment = comment_tag.get_text(strip=True) if comment_tag else '0'
        comment_count = re.findall(r'\d+', raw_comment)
        single_new_dict['link'] = link
        single_new_dict['title'] = title
        single_new_dict['score'] = score
        single_new_dict['comment'] = comment_count
        news_lists.append(single_new_dict)
    with open(os.path.join(file_store, 'news.txt'), 'a+') as the_new:
        json.dump(news_lists, the_new)


with concurrent.futures.ThreadPoolExecutor() as executor:
    executor.map(download_news, [i for i in range(10)])