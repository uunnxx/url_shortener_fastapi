from fastapi import FastAPI
from shortener import router


app = FastAPI()


app.include_router(router.shortener, prefix='/shortener')

# @app.get('/')
# def read_root():
#     return {'Hello': 'World!'}
#
# @app.get('/items/{item_id}')
# def read_item(item_id: int):
#     return {'item_id': item_id}
