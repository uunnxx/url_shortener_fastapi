import secrets
import string

from fastapi import APIRouter
from shortener.models import CreateUrlShortener, CreateUrlShortenerResponse
from shortener.database import MockDBOperations
from starlette.responses import RedirectResponse


shortener = APIRouter()

mock_db_operations = MockDBOperations()

@shortener.post('/create', response_model=CreateUrlShortenerResponse)
async def create(shortner: CreateUrlShortener):
    short_url_length = 7
    res = ''.join(secrets.choice(string.ascii_uppercase + string.digits)
                  for _ in range(short_url_length))
    short_url = str(res)
    status = await mock_db_operations.add_data_to_db(url=shortner.url, short_url=short_url)

    # If the url is added to the database, return the short url
    if status:
        return CreateUrlShortenerResponse(short_url=short_url, url=shortner.url)
    else:
        # If the url is not added to the DB, return the error message
        return CreateUrlShortenerResponse(short_url='', url='')


@shortener.get('/list', response_model=list[CreateUrlShortenerResponse])
async def list():
    # Get the data from the DB
    data = await mock_db_operations.fetch_all_data()
    # Create a list of CreateUrlShortenerResponse
    lst = []
    for key, value in data.items():
        lst.append(CreateUrlShortenerResponse(short_url=key, url=value))
    return lst


@shortener.delete('/delete/{short_url}')
async def delete_short_url(short_url: str):
    status = await mock_db_operations.delete_data_from_db(short_url=short_url)
    if status:
        return {'messages': f'{short_url} successfully deleted!'}
    else:
        return {'message': f'Failed to delete {short_url}'}


@shortener.get('/test/{short_url}')
async def test(short_url: str):
    data = await mock_db_operations.fetch_all_data()
    if short_url in data:
        url = data[short_url]
        response = RedirectResponse(url=url)
        return response
    else:
        return {'message': 'Failed to fetch'}
    
