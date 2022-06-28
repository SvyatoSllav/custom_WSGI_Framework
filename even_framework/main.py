import quopri
from .framework_requests import GetRequest, PostRequest


class PageNotFound404:
    def __call__(self, request):
        return '404 NOT FOUND', 'Cтраница не найдена'


class Framework:
    def __init__(self, routes_list) -> None:
        self.routes_list = routes_list

    def __call__(self, environ, start_response):
        path = environ['PATH_INFO']

        if not path.endswith('/'):
            path = f'{path}/'

        request = {}
        method = environ.get('REQUEST_METHOD', None)
        request['method'] = method

        if method == 'GET':
            request_params = GetRequest().get_request_params(environ)
            request['request_params'] = request_params
            print(f'Нам пришли GET-параметры: {request_params}')

        elif method == 'POST':
            data = PostRequest().get_request_params(environ)
            request['data'] = data
            print(f'Пришел POST request: {Framework.decode_value(data)}')

        if path in self.routes_list:
            view = self.routes_list[path]
        else:
            view = PageNotFound404()

        code, body = view(request)
        start_response(code, [('Content-Type', 'text/html')])
        return [body.encode('utf-8')]

    @staticmethod
    def decode_value(data):
        new_data = {}
        for key, value in data.items():
            val = bytes(value.replace('%', '=').replace('+', ' '), 'UTF-8')
            val_decode_str = quopri.decodestring(val).decode('UTF-8')
            new_data[key] = val_decode_str
        return new_data
