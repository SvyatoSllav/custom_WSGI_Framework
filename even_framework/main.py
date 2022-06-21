class PageNotFound404:
    def __call__(self):
        return '404 NOT FOUND', 'Cтраница не найдена'


class Framework:
    def __init__(self, routes_list) -> None:
        self.routes_list = routes_list

    def __call__(self, environ, start_response):
        path = environ['PATH_INFO']

        if not path.endswith('/'):
            path = f'{path}/'

        if path in self.routes_list:
            view = self.routes_list[path]
        else:
            view = PageNotFound404()
        print(view)
        code, body = view()

        start_response(code, [('Content-Type', 'text/html')])
        return [body.encode('utf-8')]
