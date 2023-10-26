import requests

class SwapiApiConsumer:
    @classmethod
    def get_starships(cls, page):
        parametros = {'page': page}
        response = requests.get('https://swapi.dev/api/starships/', params = parametros)
        return response.json()