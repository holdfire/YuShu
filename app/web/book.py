from flask import jsonify,request
from helper import is_isbn_or_key
from yushu_book import YuShuBook
from app.forms.book import SearchForm
from . import web
# 下面这个hello函数，在flask里面叫做视图函数，和mvc模式的control是一个意思
# 视图函数会返回：status code，如200,404,301；还有content type放在http header里面，默认值为text/html
# 视图函数返回的是一个response对象
# flask能够兼容带/和不带/两种情况，是通过服务器对url做重定向来实现的
# 其目的是为了保证url的唯一性，这样不会被搜索引擎检索到2次，SEO
# 下面是注册路由的方式一，通常用这种就可以，够优雅
# 下面就是API,其难点在于如何设计
# 注册路由的方式二，如果使用基于类的视图，就必须用这种方式
# app.add_url_rule('/hello', view_func=hello)


@web.route('/book/search')
def search():
    form = SearchForm(request.args)
    if form.validate():
        q = form.q.data.strip()
        page = form.page.data
        isbn_or_key = is_isbn_or_key(q)
        if isbn_or_key == 'isbn':
            result = YuShuBook.search_by_isbn(q)
        else:
            result = YuShuBook.search_by_keyword(q, page)
        return jsonify(result)
    else:
        return jsonify(form.errors)

