from .swapi_api_consumer import SwapiApiConsumer

def test_get_starships():

    # requests_mock.get('https://swapi.dev/api/starships/', status_code=200, json={'alguma': 'coisa'})
    
    swapi_api_consumer = SwapiApiConsumer()
    page = 1
    response = swapi_api_consumer.get_starships(page=page)

    assert response['request'].method == 'GET'
    assert response['request'].url == 'https://swapi.dev/api/starships/'
    assert response['request'].params == {'page': page}
    
    assert response['status_code'] == 200
    assert isinstance(response['response']['results'], list)