from even_framework.main import Framework
from wsgiref.simple_server import make_server
from views import urls

application = Framework(urls)

with make_server('', 8000, application) as httpd:
    print('Server is started')
    httpd.serve_forever()
