from flask import jsonify
import helper
from yushu_book import YuShuBook


@app.route('/book/search/<q>/<page>')
def search(q, page):
    # isbn格式或者key
    isbn_or_key = helper.is_isbn_or_key(q)
    yushu = YuShuBook()
    if isbn_or_key == 'isbn':
        result = yushu.search_by_isbn(q)
    else:
        result = yushu.search_by_keyword(q)
    return jsonify(result)
    # return json.dump()


@app.route('/hello')
def hello():
    return "hello world"
