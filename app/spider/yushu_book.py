from app.libs.myhttp import Http
from flask import current_app


class YuShuBook:
    _isbn_url = 'http://t.yushu.im/v2/book/isbn/{}'

    _keyword_url = 'http://t.yushu.im/v2/book/search?q={}&count={}&start={}'

    def search_by_isbn(self, isbn):
        url = self._isbn_url.format(isbn)
        result = Http.get(url)
        #save data to database
        return result

    def search_by_keyword(self, keyword, page=1):
        url = self._keyword_url.format(keyword, current_app.config['PER_PAGE'], self.calculate_start(page))
        result = Http.get(url)
        return result

    @staticmethod
    def calculate_start(page):
        return (page - 1) * current_app.config['PER_PAGE']
