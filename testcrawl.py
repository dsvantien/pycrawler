# from PIL import Image
# import pytesseract
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract'
#
#
# def cleanFile(filePath, newFilePath):
#     image = Image.open(filePath)
#     # Set a threshold value for the image, and save
#     image = image.point(lambda x: 0 if x < 143 else 255)
#     image.save(newFilePath)
#     return image
#
#
# image = cleanFile('test3.jpg', 'textCleaned.png')
# # call tesseract to do OCR on the newly created image
# print(pytesseract.image_to_string(image, lang='vie'))

# from PIL import Image
# import pytesseract
# import cv2
# import os
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract'
#
# image = cv2.imread( "test3.jpg" )
# gr = cv2.cvtColor( image,cv2.COLOR_BGR2GRAY )
# gr = cv2.threshold( gr,0,255,cv2.THRESH_BINARY|cv2.THRESH_OTSU )[1]
#
# file = "{}.jpg".format( os.getpid() )
# cv2.imwrite( file, gr )
# to_text = pytesseract.image_to_string( Image.open(file),lang='vie' )
# os.remove( file )
# print(to_text)
import pytesseract
from urllib.request import urlretrieve
from urllib.request import urlopen
from bs4 import BeautifulSoup
import subprocess
import requests
from PIL import Image
from PIL import ImageOps
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract'
def cleanImage(imagePath):
    image = Image.open(imagePath)
    image = image.point(lambda x: 0 if x<143 else 255)
    borderImage = ImageOps.expand(image,border=20,fill='white')
    borderImage.save(imagePath)
html = urlopen('http://www.pythonscraping.com/humans-only')
bs = BeautifulSoup(html, 'html.parser')
#Gather prepopulated form values
imageLocation = bs.find('img', {'title': 'Image CAPTCHA'})['src']
formBuildId = bs.find('input', {'name':'form_build_id'})['value']
captchaSid = bs.find('input', {'name':'captcha_sid'})['value']
captchaToken = bs.find('input', {'name':'captcha_token'})['value']
captchaUrl = 'http://pythonscraping.com'+imageLocation
urlretrieve(captchaUrl, 'captcha.jpg')
cleanImage('captcha.jpg')
# p = subprocess.Popen(['tesseract', 'captcha.jpg', 'captcha'], stdout=
# subprocess.PIPE,stderr=subprocess.PIPE)
# p.wait()
captchaResponse = pytesseract.image_to_string('captcha.jpg')
# f = open('captcha.txt', 'r')
# #Clean any whitespace characters
# captchaResponse = f.read().replace(' ', '').replace('\n', '')
print('Captcha solution attempt: '+captchaResponse)
if len(captchaResponse) == 5:
    params = {'captcha_token':captchaToken, 'captcha_sid':captchaSid,
    'form_id':'comment_node_page_form', 'form_build_id': formBuildId,
    'captcha_response':captchaResponse, 'name':'Ryan Mitchell',
    'subject': 'I come to seek the Grail',
    'comment_body[und][0][value]':
    '...and I am definitely not a bot'}
    r = requests.post('http://www.pythonscraping.com/comment/reply/10',
    data=params)
    responseObj = BeautifulSoup(r.text, 'html.parser')
    if responseObj.find('div', {'class':'messages'}) is not None:
        print(responseObj.find('div', {'class':'messages'}).get_text())
else:
    print('There was a problem reading the CAPTCHA correctly!')

