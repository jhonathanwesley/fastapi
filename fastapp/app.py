from http import HTTPStatus

from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from fastapp.schemas import Message, UserSchema

app = FastAPI(title='Jhonathan Server Side')


@app.get('/index', status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    return {'message': 'Bem Vindo a API'}


@app.get('/', status_code=HTTPStatus.OK, response_class=HTMLResponse)
def write_html():
    with open('fastapp/index.html', 'r', encoding='utf-8') as f:
        html_content = f.read()
    return HTMLResponse(html_content, HTTPStatus.OK)


@app.get('/hello', status_code=HTTPStatus.OK, response_class=HTMLResponse)
def hello_html():
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Hello World API endpoint</title>
    </head>
    <body>
        <h1>Hello World</h1>
    </body>
    </html>"""


@app.post('/users/', status_code=HTTPStatus.CREATED,)
def create_user(user: UserSchema):
    return user
