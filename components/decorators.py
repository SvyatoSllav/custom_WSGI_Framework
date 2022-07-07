# Decorator for routing urls
def AppRoute(routes, url):

    def ViewClass(cls):
        routes[url] = cls()
    return ViewClass
