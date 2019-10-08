import requests
from urllib import request

# python中自带一个urllib模块，可以用来发送请求
# 用一个第三方库叫做requests
class HTTP:
    @staticmethod
    def get(url, return_json=True):
        r = requests.get(url)
        # 简化if else语句的技巧：使用三元表达式
        if r.status_code != 200:
            return {} if return_json else ''
        return r.json() if return_json else r.text

    # @staticmethod
    # def get_with_request(url, json_return = True):
    #     url = quote(url, safe = '/:?=&')
    #     # req = request.Request(url, headers=headers)
    #     try:
    #         with request.urlopen(url) as r:
    #             result_str = r.read()
    #             result_str = str(result_str, encoding='utf-8')
    #         if json_return:
    #             return json.loads(result_str)
    #         else:
    #             return result_str
    #     except OSError as e:
    #         # 对于外部的数据，如果出现异常，最好不要抛出来，而是应该默认值处理
    #         print(e.reason)
    #         if json_return:
    #             return {}
    #         else:
    #             return None



