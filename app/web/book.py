import json
from flask import jsonify, request, render_template
from app.libs import helper
from app.view_models.book import BookViewModel, BookCollection
from . import web
from app.spider.yushu_book import YuShuBook
from app.forms.book import SearchForm


@web.route('/book/search')
def search():
    '''
        获取传参
        ?q=as&page=1
    '''
    # params = request.args.to_dict()
    # q = request.args['q']
    # page = request.args['page']
    # 参数验证
    form = SearchForm(request.args)
    books = BookCollection()

    if form.validate():
        q = form.q.data.strip()
        page = form.q.data
        # isbn格式或者key
        isbn_or_key = helper.is_isbn_or_key(q)
        yushu_book = YuShuBook()

        if isbn_or_key == 'isbn':
            yushu_book.search_by_isbn(q)
        else:
            yushu_book.search_by_keyword(q)
        books.fill(yushu_book, q)
        # return jsonify(books.__dict__)
        return json.dumps(books, default=lambda o: o.__dict__)
    else:
        return jsonify(form.errors)

    # return json.dump()


@web.route('/hello/')
def hello():
    return "hello world"


@web.route('/test/')
def test():
    r = {
        'name': 'wen',
    }
    # flash('')
    # 模板渲染
    return render_template('test.html', data=r)
