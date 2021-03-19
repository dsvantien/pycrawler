import requests
from bs4 import BeautifulSoup
url = "https://phephimz.net/api/movie-update-view.html"
url = "https://prd.jwpltx.com/v1/jwplayer6/ping.gif?h=-1466017906&e=s&n=2858367515385583&aid=GCCG&at=1&c=-1&ccp=0&cp=0&d=0&eb=1&ed=6&emi=71uj7n1hank2&gfb=0&gifr=0&gios=0&i=1&lsa=fail&mt=0&pbd=1&pbr=1&pgi=1t3hn6iqj81x&ph=0&pii=0&pl=590&plc=1&pli=1cbtsv01wv5k&pp=hlsjs&ppm=VOD&prc=1&ps=3&pss=1&pt=&pu=https%3A%2F%2Fphephimz.net%2F&pv=8.8.2&pyc=1&s=0&sdk=0&stc=1&stpe=0&tv=3.13.0&vb=1&vi=1&vl=100&wd=1048&abm=1&bwe=6554&cae=0&cct=0&drm=0&ff=20&l=4&lng=en&mk=hls&mu=https%3A%2F%2Fp2p.movie3s.net%2Fembed%2Fblob%3Ahttps%3A%2Fp2p.movie3s.net%2F42b10d11-2212-466b-8b32-72c596f2b483&pd=2&plng=en&pni=0&pnl=37&pr=1&q=32&qcr=initial%20choice&sp=0&strt=30&tb=21.4&tt=0&vd=2715&vh=480&vs=3&vw=854&sa=1604931906104"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36"}
url = "https://phephimz.net/phim/10-nam-3-thang-30-ngay-7856/tap-3-111224.html"
res = requests.get(url,headers=headers)
soup = BeautifulSoup(res.text, 'lxml')
print(soup.prettify())