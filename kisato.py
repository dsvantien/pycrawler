import requests
from bs4 import BeautifulSoup
import os.path

def download_img(image_url,cat,file_name,link):
    file_store = f'./mau biet thu/{cat}/'
    if not os.path.exists(file_store):
        os.makedirs(file_store)
    try:
        res = requests.get(image_url, stream=True, headers=headers)
        with open(os.path.join(file_store, file_name), 'wb') as the_image:
            for chunk in res.iter_content(chunk_size = 4096 * 4):
                the_image.write(chunk)
        with open(os.path.join(file_store, 'link.txt'), 'w') as f:
            f.write(link)
    except:
        pass



headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36"}
url = 'http://kisato.vn/mau-biet-thu/'
# test ='http://kisato.vn/thi-cong-tron-goi-mau-nha-vuon-kinh-phi-17-ty-tai-chon-thanh-binh-phuoc/'


resp = requests.get(url, headers=headers)
soup_html = BeautifulSoup(resp.text, 'lxml')
# video=soup_html.find('div',class_='wp-block-embed__wrapper').find('iframe').get('src')


page = soup_html.find('ul',class_='page-numbers')
# pg = None
if page is not None:
    li_page = page.find_all('li')
    if li_page[-1].get_text(strip=True) == '→':
        num_of_page = int(li_page[-2].get_text(strip=True))
        print(num_of_page)
    else:
        num_of_page = int(li_page[-1].get_text(strip=True))
        print(num_of_page)
    for i in range(3,num_of_page+1):
        # pg =i
        print(f'downloading page...{i}')
        res = requests.get(f'{url}/page/{i}/', headers=headers)
        soup = BeautifulSoup(res.text, 'lxml')
        a_tag = soup.find_all('a', class_='woocommerce-LoopProduct-link woocommerce-loop-product__link')
        for ele in a_tag:
            detail_url = ele.get('href')
            print(f'downloading...{detail_url}')
            res1 = requests.get(detail_url, headers=headers)
            soup1 = BeautifulSoup(res1.text, 'lxml')
            p_tag = soup1.find_all('p')
            figure = soup1.find_all('figure')
            cat =soup1.find('h3',class_='product_title entry-title').get_text(strip=True)
            x = cat.find(":")
            if x==-1:
                cate = cat
            else:
                cate = "-".join(cat.split(':'))
            if len(figure)>3:
                figure = soup1.find_all('figure')
                i = 0
                for el in figure:
                    img = el.find_all('img')
                    if len(img)>0:
                        i+=1
                        for item in img:
                            img_url = item.get('src')
                            if img_url=='http://kisato.vn/wp-content/uploads/2020/09/kisato-miền-bắc.jpg'or img_url=='http://kisato.vn/wp-content/uploads/2020/09/zalo-kisato-e1599172426213.jpg':
                                break
                            print(img_url)
                            file_name = f'anh{i}.jpg'
                            download_img(img_url,cate,file_name,detail_url)
                print('done')
            else:
                i = 0
                for el in p_tag:
                    img = el.find_all('img')
                    if len(img)>0:
                        i+=1
                        for item in img:
                            img_url = item.get('src')
                            if img_url=='http://kisato.vn/wp-content/uploads/2020/09/kisato-miền-bắc.jpg'or img_url=='http://kisato.vn/wp-content/uploads/2020/09/zalo-kisato-e1599172426213.jpg':
                                break
                            print(img_url)
                            file_name = f'anh{i}.jpg'
                            download_img(img_url,cate,file_name,detail_url)
                print('done')





