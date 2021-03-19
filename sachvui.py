import requests
from bs4 import BeautifulSoup
import mysql.connector
import time
import re
import os.path
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36"}
url = 'https://sachvui.com/'
current = time.strftime('%Y-%m-%d %H:%M:%S')

conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='tusachmienphi'
)
if conn.is_connected():
    print('connect db ss')
cursor = conn.cursor()


def store_cat(cat):
    cursor.execute('''INSERT IGNORE INTO categorys (name,createdAt) VALUES(%s,%s)''', (cat, current))
    cursor.execute('''SET @id = LAST_INSERT_ID()''')
    conn.commit()


def cat_page(cat_url, cat):
    res = requests.get(cat_url, headers=headers)
    soup = BeautifulSoup(res.text, 'lxml')
    page = soup.find('ul',class_='pagination pagination-sm')
    if page is not None:
        li_page = page.find_all('li')
        if li_page[-1].get_text(strip=True) == '→':
            num_of_page = int(li_page[-2].get_text(strip=True))
        else:
            num_of_page = int(li_page[-1].get_text(strip=True))
        for i in range(1,num_of_page+1):
            print(f"page[{i}]")
            res1 = requests.get(cat_url+f"/{i}", headers=headers)
            soup1 = BeautifulSoup(res1.text, 'lxml')
            row1 = soup1.find('div', class_='panel-body')
            detail = row1.find_all('a', class_='thumbnail')
            for ele in detail:
                detail_url = ele.get('href')
                print(f'cawling book[{detail_url}]')
                store_book(detail_url, cat)
    else:
        row = soup.find('div', class_='panel-body')
        detail = row.find_all('a', class_='thumbnail')
        for ele in detail:
            detail_url = ele.get('href')
            store_book(detail_url, cat)


def store_author(author):
    cursor.execute('''INSERT IGNORE INTO authors(name,createdAt) VALUES(%s,%s) ON DUPLICATE KEY UPDATE name=VALUE(name),author_id = LAST_INSERT_ID(author_id)''', (author, current))
    cursor.execute('''SET @author_id = LAST_INSERT_ID()''')
    conn.commit()


# def download_img(image_url, cat, img_filename):
#     res = requests.get(image_url, stream=True, headers=headers)
#     file_store = f'./images/{cat}/'
#     if not os.path.exists(file_store):
#         os.makedirs(file_store)
#     with open(os.path.join(file_store, img_filename), 'wb') as the_image:
#         for chunk in res.iter_content(chunk_size=4096 * 4):
#             the_image.write(chunk)


# def download_pdf(pdf_url, pdf_file, cat):
#     res = requests.get(pdf_url, stream=True, headers=headers)
#     file_store = f'./pdfs/{cat}/'
#     if not os.path.exists(file_store):
#         os.makedirs(file_store)
#     with open(os.path.join(file_store, pdf_file), 'wb') as the_pdf:
#         for chunk in res.iter_content(chunk_size=2000):
#             the_pdf.write(chunk)


def store_book(detail_url, cat):
    res = requests.get(detail_url, headers=headers)
    soup = BeautifulSoup(res.text, 'lxml')
    image_url = soup.find('img', class_='img-thumbnail').get('src')
    img_filename = image_url.split('/')[-1]
    # download_img(image_url, cat, img_filename)
    title = soup.find('h1', class_='ebook_title text-primary').get_text(strip=True)
    author_tag = soup.find('h5', string=re.compile(r'Tác giả\s?:\s?(.*)')).get_text(strip=True)
    author = re.search(r'(Tác giả\s?:\s?)(.*)', author_tag)
    author = author.group(2)
    luotxem_tag = soup.find('h5', string=re.compile(r'Lượt xem\s?:\s?(.*)')).get_text(strip=True)
    luotxem = re.search(r'(Lượt xem\s?:\s?)(.*)', luotxem_tag)
    luotxem = luotxem.group(2)
    pdf = soup.find('a', string='PDF')
    if pdf:
        pdf_url = pdf.get('href')
        pdf_file = img_filename.split('.')[0] + '.pdf'
        # download_pdf(pdf_url, pdf_file, cat)
    else:
        pdf_url = detail_url
    desc_tag = soup.find('div', class_='gioi_thieu_sach text-justify').find_all('p')
    description =""
    for item in desc_tag:
        description += item.getText(strip=True)
        description += "\n"
    # cursor.execute('''INSERT IGNORE INTO books(title, image_url, img_filename,pdf_url,luotxem, description, createdAt,categoryId) VALUES
    # (%s,%s,%s,%s,%s,%s,%s,@id)''', (title, image_url, img_filename, pdf_url, luotxem, description, current))
    # cursor.execute('''SET @book_id = LAST_INSERT_ID()''')
    # conn.commit()
    # store_author(author)
    # cursor.execute('''INSERT IGNORE INTO authorbooks(createdAt,bookBookId,authorAuthorId) VALUES(%s,@book_id,@author_id)''', (current,))
    # conn.commit()


res = requests.get(url, headers=headers)
soup = BeautifulSoup(res.text, 'lxml')
ul_tag = soup.find('ul', class_='center-block row')
for item in ul_tag.find_all('li'):
    cat_url = item.find('a').get('href')
    cat = item.find('a').get_text(strip=True)
    print(cat)
    # store_cat(cat)
    cat_page(cat_url,cat)

