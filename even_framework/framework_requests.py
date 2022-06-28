from typing import Dict


class GetRequest:

    @staticmethod
    def get_request_params(envalueiron) -> Dict[str, str]:
        # Get's string data from environ and then return dict with parameters
        query_string = envalueiron.get('QUERY_STRING', None)
        request_params = GetRequest.parse_query_string(query_string)
        return request_params

    @staticmethod
    def parse_query_string(query_string: str) -> Dict[str, str]:
        # Convert string data to python dictionary
        request_params = {}
        if query_string:
            for item in query_string.split('&'):
                key, value = item.split('=')
                request_params[key] = value
        return request_params


class PostRequest:

    @staticmethod
    def get_wsgi_input_data(environ) -> bytes:
        content_length = int(environ.get('CONTENT_LENGTH', 0))
        data = environ['wsgi.input'].read(content_length) if content_length > 0 else b''
        return data

    def parse_wsgi_input_data(self, data):
        result = {}
        if data:
            data = data.decode(encoding='utf-8')
            result = self.parse_input_data(data)
        return result

    @staticmethod
    def parse_input_data(data):
        result = {}
        params = data.split('&')
        for item in params:
            k, v = item.split('=')
            result[k] = v
        return result

    def get_request_params(self, environ):
        # Getting data
        data = self.get_wsgi_input_data(environ)
        # Convert's data to dict
        data = self.parse_wsgi_input_data(data)
        return data
