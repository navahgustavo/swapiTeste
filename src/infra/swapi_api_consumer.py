import requests

class SwapiApiConsumer:

    def get_starships(self, page):
        ''' Faz requisição nas starships '''

        req = requests.Request(method='GET', url='https://swapi.dev/api/starships/', params={'page': page})
        req_prepared = req.prepare()
        response = self._send_http_request(req_prepared)
        return {
            'status_code': response.status_code,
            'request': req,
            'response': response.json()
        }

    @classmethod
    def _send_http_request(cls, req_prepared):
        ''' Prepara a sessão e manda a requisição '''

        http_session = requests.Session()
        response = http_session.send(req_prepared)
        return response