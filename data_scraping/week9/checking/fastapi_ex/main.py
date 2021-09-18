
import os
import io
import base64

from fastapi import FastAPI, Request, Form, File, UploadFile
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np


app = FastAPI()

app.mount('/static', StaticFiles(directory='static'), name='static')

templates = Jinja2Templates(directory='templates')


def get_roots(a: int, b: int, c: int):
    roots = np.roots([a, b, c])
    roots = np.unique(roots, axis=0)

    roots = roots[~np.iscomplex(roots)]
    roots = sorted(roots)
    return [int(root) * root.is_integer() or root for root in roots]


@app.get('/')
async def root(request: Request, message='Peer-graded Assignment: Creating a Web-Service'):
    return templates.TemplateResponse('index.html',
                                      {'request': request, 'message': message})


@app.get('/solve')
async def solve(request: Request, a: int, b: int, c: int):
    return {'roots': get_roots(a, b, c)}


@app.get('/plot')
async def plot(request: Request, a: int, b: int, c: int):
    coeff = [a, b, c]
    roots = get_roots(a, b, c)

    fig = plt.figure()
    middle_point = 0
    if len(roots) == 1:
        middle_point = roots[0]
    elif len(roots) == 2:
        middle_point = (roots[0] + roots[1]) / 2
    x = np.linspace(middle_point-15, middle_point+15, 1000)
    y = a * (x ** 2) + b * x + c

    plt.plot(x, y)

    png_image = io.BytesIO()
    fig.savefig(png_image)
    png_image_b64_string = base64.b64encode(png_image.getvalue()).decode('ascii')

    return templates.TemplateResponse('plot.html',
                                      {'request': request,
                                       'coeff': coeff,
                                       'roots': roots,
                                       'picture': png_image_b64_string})
