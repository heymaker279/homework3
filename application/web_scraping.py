import bs4
import requests

'''формат: <дата> - <заголовок> - <ссылка>'''
KEYWORDS = ['дизайн', 'фото', 'React', 'python', 'DevOps', 'SQL']
url = 'https://habr.com'
id_ = ["660597", "660599", "660593"]
HEADERS = {
    'Cookie': '_ym_uid=1639148487334283574; _ym_d=1639149414; _ga=GA1.2.528119004.1639149415; '
              '_gid=GA1.2.512914915.1639149415; habr_web_home=ARTICLES_LIST_ALL; hl=ru; fl=ru; _ym_isad=2; '
              '__gads=ID=87f529752d2e0de1-221b467103cd00b7:T=1639149409:S=ALNI_MYKvHcaV4SWfZmCb3_wXDx2olu6kw',
    'Accept-Language': 'ru-RU,ru;q=0.9',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Cache-Control': 'max-age=0',
    'If-None-Match': 'W/"37433-+qZyNZhUgblOQJvD5vdmtE4BN6w"',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/96.0.4664.93 Safari/537.36',
    'sec-ch-ua-mobile': '?0'}


def get_request():
    ret = requests.get(url, headers=HEADERS)
    soup = bs4.BeautifulSoup(ret.text, 'lxml')
    articles = soup.find(class_="tm-articles-list").find_all(class_="tm-articles-list__item")
    for word in KEYWORDS:
        for article in articles:
            if word in article.text.strip().split(" "):
                print(word)
                href = article.find(class_='tm-article-snippet__title tm-article-snippet__title_h2').find('a').attrs[
                    'href']
                link = url + href
                title_ = article.find(class_='tm-article-snippet__title tm-article-snippet__title_h2').find('span').text
                date = article.find(class_="tm-article-snippet__datetime-published").find("time").attrs['title']
                print(f"{date} - {title_} - {link}")
