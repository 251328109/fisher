from http import Http


class YuShuBook:
    _isbn_url = 'http://t.yushu.im/v2/book/isbn/{}'

    _keyword_url = 'http://t.yushu.im/v2/book/search?q={}&count={}&start={}'

    def search_by_isbn(self, isbn):
        url = self._isbn_url.format(isbn)
        result = Http.get(url)
        return result

    def search_by_keyword(self, keyword, count=15, start=0):
        url = self._keyword_url.format(keyword, count, start)
        result = Http.get(url)
        return result
