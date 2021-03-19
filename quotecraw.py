# CREATE TABLE authors (
#     id INT PRIMARY KEY AUTO_INCREMENT,
#     name VARCHAR(100) UNIQUE,
#     born_date datetime,
#     born_location VARCHAR(255),
#     description text
# );
#
# CREATE TABLE quotes (
#     id INT PRIMARY KEY AUTO_INCREMENT,
#     quote_text text UNIQUE,
#     author_id int NOT null,
#    CONSTRAINT fk_authorquote FOREIGN KEY(author_id) REFERENCES authors(id) ON DELETE CASCADE ON UPDATE CASCADE
# );
#
# CREATE TABLE tags(
#     id INT PRIMARY KEY AUTO_INCREMENT,
#     tag_name text
# );
#
# CREATE TABLE quote_tags(
#     quote_id INT,
#     tag_id INT,
#     CONSTRAINT fk_tagquote FOREIGN KEY(quote_id) REFERENCES quotes(id) ON DELETE CASCADE ON UPDATE CASCADE,
#     CONSTRAINT fk_quotetag FOREIGN KEY(tag_id) REFERENCES tags(id) ON DELETE CASCADE ON UPDATE CASCADE,
#     PRIMARY KEY(quote_id, tag_id)
# );


import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import mysql.connector
import datetime
import time
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36"}

t1 = time.perf_counter()
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='quotecraw'
)
if conn.is_connected():
    print('connect db ss!')
cursor = conn.cursor()


def store_quote(quote_text, author_id):
    cursor.execute('''INSERT INTO quotes (quote_text, author_id) VALUE(%s,%s)''', (quote_text, author_id))
    cursor.execute('''SET @quote_id = LAST_INSERT_ID()''')
    conn.commit()


def store_author(author_link, author_name):
    res = requests.get(author_link, headers=headers)
    soup = BeautifulSoup(res.text, 'lxml')
    author_detail = soup.find('div', class_='author-details')
    # name = author_detail.find('h3', class_='author-title').get_text(strip=True) the name not the same
    born_date = author_detail.find('span', class_='author-born-date').get_text(strip=True)
    format_born_date = datetime.datetime.strptime(born_date, '%B %d, %Y')
    born_location = author_detail.find('span', class_='author-born-location').get_text(strip=True)
    description = author_detail.find('div', class_='author-description').get_text(strip=True)
    cursor.execute('''INSERT IGNORE INTO authors (name,born_date,born_location,description) VALUE(%s,%s,%s,%s)''', (author_name, format_born_date, born_location, description))
    conn.commit()


def store_tag(tag_name):
    cursor.execute('''INSERT IGNORE INTO tags (tag_name) VALUE(%s) ON DUPLICATE KEY UPDATE tag_name=VALUE(tag_name),id = LAST_INSERT_ID(id)''', (tag_name,))
    #  if duplicate set id = last insert id this mean old id the id insert before not the new id
    cursor.execute('''SET @id = LAST_INSERT_ID()''')
    cursor.execute('''INSERT IGNORE INTO quote_tags (quote_id, tag_id) VALUE(@quote_id,@id)''')
    conn.commit()


def get_author_id(author_name):
    print(author_name)
    cursor.execute('''SELECT id FROM authors WHERE name =%s''', (author_name,))
    id = cursor.fetchone()
    return None if id is None else id[0]


def worker(i):
    url = f'http://quotes.toscrape.com/page/{i}'
    res = requests.get(url, headers=headers)
    soup = BeautifulSoup(res.text, 'lxml')
    for item in soup.find_all('div', class_='quote'):
        author_tag = item.find('small', class_='author')
        author_name = author_tag.get_text(strip=True)
        author_link = author_tag.find_next_sibling('a')
        author_raw_url = author_link.get('href')
        author_link = urljoin('http://quotes.toscrape.com', author_raw_url)
        store_author(author_link, author_name)
        text_item = item.find('span', class_='text')
        quote_text = text_item.get_text(strip=True) if text_item else None
        author_id = get_author_id(author_name)
        store_quote(quote_text, author_id)
        tag = item.find_all('a', class_='tag')
        for el in tag:
            tag_name = el.get_text(strip=True)
            store_tag(tag_name)


for i in range(1, 10):
    worker(i)
t2 = time.perf_counter()
print(f'Finished in {t2-t1} seconds')
