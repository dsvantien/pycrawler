# CREATE TABLE catagorys(
#     id int PRIMARY KEY AUTO_INCREMENT,
#     name varchar(100)
#
# );
# CREATE TABLE books (
#     book_id int PRIMARY KEY AUTO_INCREMENT,
#     title varchar(100),
#     price varchar(100),
#     status_stock varchar(100),
#     img_url text
#     rate varchar(100),
#     description text,
#     filename text,
#     cat_id int not null,
#     FOREIGN KEY(cat_id) REFERENCES catagorys(id) ON DELETE CASCADE
# );
#
#
#  CREATE TABLE other_info(
#      id int PRIMARY KEY AUTO_INCREMENT,
#      UPC varchar(100),
#      type varchar(50),
#      excl_tax varchar(100),
#      incl_tax varchar(100),
#      tax double,
#      reviews_count varchar(100),
#      book_id int UNIQUE, unique-->one to one relation
#      FOREIGN KEY(book_id) REFERENCES books(id) ON DELETE CASCADE
#  )

import requests
from bs4 import BeautifulSoup
import mysql.connector
import bs4
import os.path
from urllib.parse import urljoin
import re

url = 'http://books.toscrape.com'
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36"}

conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='bookcraw'
)
if conn.is_connected():
    print('connect db ss!')
cursor = conn.cursor()


def store_category(category):
    cursor.execute('''INSERT IGNORE INTO catagorys (name) VALUES(%s)''', (category,))
    cursor.execute('''SET @id = LAST_INSERT_ID()''')
    conn.commit()


def store_book(cat_url, category):
    res = requests.get(cat_url, headers=headers)
    soup = BeautifulSoup(res.text, 'lxml')
    row = soup.find('ol', class_='row')
    detail = row.find_all('a')
    for ele in detail:
        raw_url = ele.get('href')
        detail_url = urljoin(cat_url, raw_url)
        get_book_detail(detail_url, category)


def get_book_detail(detail_url, category):
    res = requests.get(detail_url, headers=headers)
    soup = BeautifulSoup(res.text, 'lxml')
    image = soup.find('img')
    r_img_url = image.get('src')
    img_url = urljoin(url, r_img_url)
    title = image.get('alt')
    file_name = url_to_filename(r_img_url, title)
    download_img(img_url, file_name, category)
    price = soup.find('p', class_='price_color').get_text(strip=True)[1:]
    rate = soup.find('p', class_='star-rating').get('class')
    star = rate[-1]
    try:
        desc = soup.find(id='product_description').find_next_sibling('p').get_text(strip=True)
    except AttributeError:
        desc = "nothing"
    status = soup.find('p', class_='instock availability').get_text(strip=True)
    cursor.execute('''INSERT IGNORE INTO books (title,price,status_stock,img_url,description,rate,filename,cat_id) VALUES(%s,%s,%s,%s,%s,%s,%s,@id)
        ''', (title, price, status, img_url, desc, star, file_name,))
    cursor.execute('''SET @bk_id = LAST_INSERT_ID()''')
    conn.commit()
    UPC = soup.find('th', string='UPC').find_next_sibling('td').get_text(strip=True)
    type = soup.find('th', string='Product Type').find_next_sibling('td').get_text(strip=True)
    excl_tax = soup.find('th', string='Price (excl. tax)').find_next_sibling('td').get_text(strip=True)
    incl_tax = soup.find('th', string='Price (incl. tax)').find_next_sibling('td').get_text(strip=True)
    tax = soup.find('th', string='Tax').find_next_sibling('td').get_text(strip=True)
    reviews_count = soup.find('th', string='Number of reviews').find_next_sibling('td').get_text(strip=True)
    store_other_info(UPC, type, excl_tax, incl_tax, tax, reviews_count)


def url_to_filename(img_url, title):
    url = img_url.split('/')[-1]
    tail = re.findall(r'\.\w+', url)
    body = title.replace(' ', '-').strip()
    body = re.sub(r'[:()#,\\\s\d+]', '', body)
    return body + tail[-1]


def download_img(img_url, file_name, category):
    file_store = f'./download/{category}/'
    if not os.path.exists(file_store):
        os.makedirs(file_store)
    res = requests.get(img_url, headers=headers, stream=True)
    try:
        with open(os.path.join(file_store, file_name), 'wb') as the_image:
            for chunk in res.iter_content(chunk_size=4096 * 4):
                the_image.write(chunk)
    except (PermissionError, FileNotFoundError) as e:
        pass


def store_other_info(UPC, type, excl_tax, incl_tax, tax, reviews_count):
    cursor.execute('''INSERT IGNORE INTO other_info (UPC,type,excl_tax,incl_tax,tax,reviews_count,book_id) VALUES(%s,%s,%s,%s,%s,%s,@bk_id)
    ''', (UPC, type, excl_tax, incl_tax, tax, reviews_count,))
    conn.commit()


res = requests.get(url, headers=headers)
soup = BeautifulSoup(res.text, 'lxml')
main_tag = soup.find('div', class_='side_categories')
ul_tag = main_tag.find('ul')
for li_tag in ul_tag.find('li').find('a').next_siblings:
    if type(
            li_tag) is not bs4.element.NavigableString:  # if you have spaces in your markup in between nodes BeautifulSoup will turn those into NavigableString's
        for item in li_tag.find_all('a'):
            category = item.getText(strip=True)
            print(f'[+] crawling category {category}')
            store_category(category)
            cat_rurl = item.get('href')
            cat_url = urljoin(url, cat_rurl)
            store_book(cat_url, category)
