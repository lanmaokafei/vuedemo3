from flask import Flask, jsonify, make_response

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/data')
def data():
    products_list = {
        'productList': {
            'pc': {'title': 'PC产品', 'list': [{'name': '数据统计', 'url': 'http://127.0.0.1/analysis'},
                                             {'name': '数据统计', 'url': 'http://127.0.0.1/analysis'},
                                             {'name': '数据统计', 'url': 'http://127.0.0.1/analysis'}]},
            'app': {'title': '手机应用类', 'list': [{'name': '数据统计', 'url': 'http://127.0.0.1/analysis'},
                                               {'name': '数据统计', 'url': 'http://127.0.0.1/analysis'},
                                               {'name': '数据统计', 'url': 'http://127.0.0.1/analysis'}]}
        },
        'boardList': [
            {
                'title': '开放产品',
                'description': '开放产品是一款开放产品',
                'saleout': False
            },
            {
                'title': '品牌营销',
                'description': '开放产品是一款开放产品',
                'saleout': False
            },
            {
                'title': '使命必达',
                'description': '开放产品是一款开放产品',
                'saleout': False
            },
            {
                'title': '勇攀高峰',
                'description': '开放产品是一款开放产品',
                'saleout': False
            }
        ],
        'newList': [
            {
                'title': '数据统计',
                'url': 'http://127.0.0.1/analysis'
            },
            {
                'title': '数据统计',
                'url': 'http://127.0.0.1/analysis'},
            {
                'title': '数据统计',
                'url': 'http://127.0.0.1/analysis'}
        ],
    }
    response = make_response(jsonify(products_list))
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'GET'
    response.headers['Access-Control-Allow-Headers'] = 'x-requested-with,content-type'
    return response


@app.route('/data2')
def data2():
    products_list = {
        'productList': {
            'pc': {'title': 'PC产品', 'list': [{'name': '数据统计', 'url': 'http://127.0.0.1/analysis'},
                                             {'name': '数据统计', 'url': 'http://127.0.0.1/analysis'},
                                             {'name': '数据统计', 'url': 'http://127.0.0.1/analysis'}]},
            'app': {'title': 'PC产品', 'list': [{'name': '数据统计', 'url': 'http://127.0.0.1/analysis'},
                                              {'name': '数据统计', 'url': 'http://127.0.0.1/analysis'},
                                              {'name': '数据统计', 'url': 'http://127.0.0.1/analysis'}]}
        }
    }
    return jsonify(products_list)


if __name__ == '__main__':
    app.run()
