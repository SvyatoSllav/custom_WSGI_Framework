from even_framework.templator import render


class Index:
    def __call__(self):
        return '200 OK', render('index.html', title='title')
