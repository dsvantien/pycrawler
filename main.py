import requests
from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.Util.Padding import pad
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
import random
import base64
import json
import os

class EncryptText:
    def __init__(self):
        self.character = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
        self.iv = '0102030405060708'
        self.public_key = '010001'
        self.modulus = '00e0b509f6259df8642dbc35662901477df22677ec152b' \
                       '5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417' \
                       '629ec4ee341f56135fccf695280104e0312ecbda92557c93' \
                       '870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b' \
                       '424d813cfe4875d3e82047b97ddef52741d546b8e289dc69' \
                       '35b3ece0462db0a22b8e7'
        self.nonce = '0CoJUm6Qyw8W8jud'

    def create16RandomBytes(self):
        generate_string = random.sample(self.character, 16)
        generated_string = ''.join(generate_string)
        return generated_string

    def AESEncrypt(self, clear_text, key):
        clear_text = pad(data_to_pad=clear_text.encode(), block_size=AES.block_size)
        key = key.encode()
        iv = self.iv.encode()
        aes = AES.new(key=key, mode=AES.MODE_CBC, iv=iv)
        cipher_text = aes.encrypt(plaintext=clear_text)
        # 字节串转为字符串
        cipher_texts = base64.b64encode(cipher_text).decode()
        return cipher_texts

    def RSAEncrypt(self, i, e, n):
        num = pow(int(i[::-1].encode().hex(), 16), int(e, 16), int(n, 16))
        result = format(num, 'x')
        return result

    def resultEncrypt(self, input_text):
        """
        对应函数d
        :param input_text:
        :return:
        """
        i = self.create16RandomBytes()
        encText = self.AESEncrypt(input_text, self.nonce)
        encText = self.AESEncrypt(encText, i)
        encSecKey = self.RSAEncrypt(i, self.public_key, self.modulus)
        from_data = {
            'params': encText,
            'encSecKey': encSecKey
        }
        return from_data


class WangYiYunMusic(object):
    def __init__(self):
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                                      'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36'}


    def get_html(self, url, method='GET', from_data=None):
        try:
            if method == 'GET':
                response = requests.get(url, headers=self.headers)
            else:
                response = requests.post(url, from_data, headers=self.headers)
            response.raise_for_status()
            response.encoding = 'utf-8'
            return response.text
        except Exception as err:
            print(err)
            return '请求异常'

    def parse_text(self, text):
        ids_list = json.loads(text)['result']['songs']
        count = 0
        info_list = []
        print('{:*^80}'.format('搜索结果如下'))
        print('{0:{5}<5}{1:{5}<20}{2:{5}<10}{3:{5}<10}{4:{5}<20}'.format('序号', '歌名', '歌手', '时长(s)', '专辑', chr(12288)))
        print('{:-^84}'.format('-'))
        for id_info in ids_list:
            song_name = id_info['name']
            id = id_info['id']
            time = id_info['dt'] // 1000
            album_name = id_info['al']['name']
            # picture_url = id_info['al']['picUrl']
            singer = id_info['ar'][0]['name']
            info_list.append([id, song_name, singer])
            print('{0:{5}<5}{1:{5}<20}{2:{5}<10}{3:{5}<10}{4:{5}<20}'.format(count, song_name, singer, time, album_name,
                                                                             chr(12288)))
            count += 1
            if count == 8:
                # 为了测试方便, 这里只显示了9条数据
                break
        print('{:*^80}'.format('*'))
        return info_list

    def save_file(self, song_text, download_info):
        filepath = './download'
        if not os.path.exists(filepath):
            os.mkdir(filepath)
        filename = download_info[1] + '-' + download_info[2]
        music_url = json.loads(song_text)['data'][0]['url']
        response = requests.get(music_url, headers=self.headers)
        with open(os.path.join(filepath, filename) + '.mp3', 'wb') as f:
            f.write(response.content)
            print("下载完毕!")


if __name__ == '__main__':
    id_url = 'https://music.163.com/weapi/cloudsearch/get/web?csrf_token='
    song_url = 'https://music.163.com/weapi/song/enhance/player/url/v1?csrf_token='

    id_d = {
        "hlpretag": "<span class=\"s-fc7\">",
        "hlposttag": "</span>",
        "s": input("请输入歌名或歌手: "),
        "type": "1",
        "offset": "0",
        "total": "true",
        "limit": "30",
        "csrf_token": ""
    }

    encrypt = EncryptText()
    id_from_data = encrypt.resultEncrypt(str(id_d))

    wyy = WangYiYunMusic()
    id_text = wyy.get_html(id_url, method='POST', from_data=id_from_data)
    info_list = wyy.parse_text(id_text)

    while True:
        input_index = eval(input("请输入要下载歌曲的序号(-1退出): "))
        if input_index == -1:
            break
        download_info = info_list[input_index]
        song_d = {
            "ids": str([download_info[0]]),
            "level": "standard",
            "encodeType": "aac",
            "csrf_token": ""
        }
        song_from_data = encrypt.resultEncrypt(str(song_d))

        song_text = wyy.get_html(song_url, method='POST', from_data=song_from_data)
        wyy.save_file(song_text, download_info)