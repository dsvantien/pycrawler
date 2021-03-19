import requests
import time
import re
import os
import os.path
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urldefrag
from sqlalchemy.exc import IntegrityError
import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="wikicraw"
)
if mydb.is_connected():
    print("connect to db successfully!")
cursor = mydb.cursor()
# create table
# CREATE TABLE IF NOT EXISTS pages (
#     url_id INTEGER PRIMARY KEY AUTO_INCREMENT,
#     url TEXT,
#     created_at TIMESTAMP DEFAULT NOW(),
#     html_file text NULL,
#     visited_at TIMESTAMP NULL
# );
#
# CREATE TABLE IF NOT EXISTS links (
#     link_url_id INTEGER PRIMARY KEY AUTO_INCREMENT,
#     url text,
#     link_url text
#    );
#
# CREATE TABLE IF NOT EXISTS images(
#     img_url_id INTEGER PRIMARY KEY AUTO_INCREMENT,
#     url text,
#     img_url text,
#     img_file text
# )
base_url = 'https://en.wikipedia.org/wiki/'
file_store = './downloads/'
current = time.strftime('%Y-%m-%d %H:%M:%S')
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36"}
if not os.path.exists(file_store):
    os.makedirs(file_store)


def url_to_file_name(url, text):
    urlpar = url.split('/')[-1]
    tail = re.findall(r'\.\w+', urlpar)
    body = text.strip().replace(' ', '_')
    if not tail:
        pass
    else:
        return body + tail[-1]
    # url = str(url).strip().replace(' ', '_')
    # return re.sub(r'(?u)[^-\w.]', '', url)  # (?u) just for unicode but can omit that in python3


def url_to_file_name_html(url):
    url = str(url).strip().replace(' ', '_')
    return re.sub(r'(?u)[^-\w.]', '', url)


def download(url, filename):
    r = requests.get(url, headers=headers, stream=True)
    # try:
    print(url)
    if filename:
        with open(os.path.join(file_store, filename), 'wb') as the_image:
            print(filename)
            for byte_chunk in r.iter_content(chunk_size=4096 * 4):
                the_image.write(byte_chunk)
    else:
        pass


def store_page(url):
    try:
        cursor.execute('INSERT INTO pages (url) VALUES (%s)', (url,))
        mydb.commit()
    except IntegrityError:
        pass


def store_link(url, link_url):
    try:
        sql = '''INSERT INTO links (url, link_url)
        VALUES (%s, %s)'''
        task = (url, link_url)
        cursor.execute(sql, task)
        mydb.commit()
    except IntegrityError:
        pass


def store_image(url, img_url, img_file):
    try:
        sql = '''INSERT INTO images (url, img_url, img_file)
        VALUES (%s, %s, %s)'''
        task = (url, img_url, img_file)
        cursor.execute(sql, task)
        mydb.commit()
    except IntegrityError:
        pass


def set_visited(url, html_file):
    sql = '''UPDATE pages
    SET visited_at=%s,
    html_file=%s
    WHERE url=%s'''
    task = (current, html_file, url)
    cursor.execute(sql, task)
    mydb.commit()


def get_random_unvisited_page():
    cursor.execute('SELECT * FROM pages WHERE visited_at IS NULL ORDER BY RAND() LIMIT 1')
    link = cursor.fetchone()
    print(link)
    return None if link is None else link[1]


def should_visit(link_url):
    link_url = urldefrag(link_url)[0]  # www.example.com/foo.html#bar the fragment url is the #bar urldefrag remove this and return tuple
    if not link_url.startswith('https://en.wikipedia.org/wiki/'):
        return None
    return link_url


def visit(url):
    print('Now visiting:', url)
    html = requests.get(url, headers=headers).text
    html_soup = BeautifulSoup(html, 'html.parser')
    # Store a-tag links
    for link in html_soup.find_all("a"):
        link_url = link.get('href')
        if link_url is None:
            continue
        link_url = urljoin(base_url, link_url)
        store_link(url, link_url)
        full_url = should_visit(link_url)
        if full_url:
            # Queue for crawling
            store_page(full_url)
        # Store img-src files
    for img in html_soup.find_all("img"):
        img_url = img.get('src')
        if img_url is None:
            continue
        img_url = urljoin(base_url, img_url)
        text = img.get('alt')
        filename = url_to_file_name(img_url, text)
        download(img_url, filename)
        store_image(url, img_url, filename)
    # Store the HTML contents
    filename = url_to_file_name_html(url) + '.html'
    fullname = os.path.join(file_store, filename)
    with open(fullname, 'w', encoding='utf-8') as the_html:
        the_html.write(html)
    set_visited(url, filename)


store_page(base_url)
url_to_visit = get_random_unvisited_page()
while url_to_visit is not None:
    visit(url_to_visit)
    url_to_visit = get_random_unvisited_page()
