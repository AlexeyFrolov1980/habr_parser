import requests
from bs4 import BeautifulSoup
import article_cls

st_accept = "text/html"  # говорим веб-серверу,
# что хотим получить html
# имитируем подключение через браузер Mozilla на macOS
st_useragent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 12_3_1) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.4 Safari/605.1.15"
# формируем хеш заголовков
headers = {
    "Accept": st_accept,
    "User-Agent": st_useragent
}

URL = "https://habr.com/ru/articles"
SITE = "https://habr.com"

# отправляем запрос с заголовками по нужному адресу
page = requests.get(URL)
# считываем текст HTML-документа


all_articles = []

soup = BeautifulSoup(page.text, "html.parser")

all_page_articles = soup.findAll('a', class_='tm-title__link', href=True)



#print(all_page_articles)
#print(len(all_page_articles))
#print(all_page_articles[0])

for article in all_page_articles:

    #Проваливаемся в статью
    article_url = SITE+article['href']
    print(article_url)

    article_page = requests.get(article_url)
    soup = BeautifulSoup(article_page.text, "html.parser")
     #print(article_page.text)

    article_title = soup.find('h1', class_="tm-title tm-title_h1")

    article_title_txt = article_title.text

    article_author = soup.find(class_ = "tm-user-info tm-article-snippet__author")

    author_txt = article_author.find('a')['title'] + '  (' + SITE + article_author.find('a')['href']+')'

    article_body = soup.find('div', class_="tm-article-body")

    #article = article_cls.ArticleCLS(

    article = article_cls.ArticleCLS(article_url, author_txt, article_title_txt , article_body.text)

    all_articles.append(article)

#Запишем статьи в файл
text_for_file = ''

for a in all_articles:
    text_for_file += str(a) + '--------------------------\n'

with open('articles.txt', 'w+', encoding='utf-8') as f:
    f.write(text_for_file)