
class ArticleCLS:
    def __init__(self, href, author,  title, text):
        self.href = href
        self.title = title
        self.text = text
        self.author = author

    def __str__(self):
        res="Ссылка: " + self.href + "\n"
        res += self.title + "\n"
        res += self.author + "\n"
        res += self.text + "\n"

        return res

