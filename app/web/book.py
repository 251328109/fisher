from flask import jsonify, request
from app.libs import helper
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
    q = request.args['q']
    page = request.args['page']
    # 参数验证
    form = SearchForm(request.args)
    if form.validate():
        q = form.q.data.strip()
        page = form.q.data
        # isbn格式或者key
        isbn_or_key = helper.is_isbn_or_key(q)
        yushu = YuShuBook()
        if isbn_or_key == 'isbn':
            result = yushu.search_by_isbn(q)
        else:
            result = yushu.search_by_keyword(q)
        return jsonify(result)
    else:
        return jsonify(form.errors)

    # return json.dump()


@web.route('/hello/')
def hello():
    return "hello world"
