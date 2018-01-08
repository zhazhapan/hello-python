from wsgiref.simple_server import make_server
from cgi import parse_qs, escape
import os


# 导入我们自己编写的application函数:
def application(environ, start_response):
    qs = parse_qs(environ["QUERY_STRING"])
    test=qs.get("test",['unkown'])[0]
    print(test)
    print("number")
    if test == 'some':
        os.system('ls')
        print("yes")
    start_response('200 OK', [('Content-Type', 'text/html')])
    return [b'haha']


# 创建一个服务器，IP地址为空，端口是8000，处理函数是application:
httpd = make_server('', 8000, application)
print('Serving HTTP on port 8000...')
# 开始监听HTTP请求:
httpd.serve_forever()
