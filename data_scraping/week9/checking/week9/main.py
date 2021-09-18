from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from decimal import Decimal
import matplotlib, io, base64
import matplotlib.pyplot as plt
import numpy as np

app = FastAPI()
app.mount('/static', StaticFiles(directory='static'), name='static')
templates = Jinja2Templates(directory='templates')
matplotlib.use('Agg')


def get_roots(a: int, b: int, c: int):
    if not a:
        return [] if not b else [-c / b]
    D = b**2 - 4 * a * c
    if D < 0:
        return []
    if D == 0:
        return [-b / (2 * a)]
    x1 = (-b + D**0.5) / (2 * a)
    x2 = (-b - D**0.5) / (2 * a)
    return [x1, x2]


def get_y(a: int, b: int, c: int, x: float):
    return a * x**2 + b * x + c


@app.get('/solve')
async def solve(a: int, b: int, c: int):
    return {'roots': get_roots(a, b, c)}


@app.get('/main')
async def main(request: Request):
    return templates.TemplateResponse('main.html', {'request': request})


@app.post('/plot')
async def plot(request: Request, a: int = Form(...), b: int = Form(...), c: int = Form(...)):
    fig = plt.figure()
    plt.grid(True)

    # axes
    plt.axhline(y=0, linewidth=0.5, color='black')
    plt.axvline(x=0, linewidth=0.5, color='black')

    roots = get_roots(a, b, c)
    roots_num = len(roots)

    if not a:
        if not b:
            msg = f'Equation has no real roots.'
        else:
            root_x = roots[0]
            points = [(x, b * x + c) for x in np.arange(root_x - 5, root_x + 5, 0.1)]
            x, y = zip(*points)
            plt.plot(x, y)
            msg = f'Equation has {roots_num} root(s): {roots}.'
    else:
        vertex_x = int(-b / (2 * a))

        # discriminant < 0 (no roots)
        if not roots:
            points = [(x, get_y(a, b, c, x)) for x in np.arange(vertex_x - 5, vertex_x + 5, 0.1)]
            x, y = zip(*points)
            plt.plot(x, y)
        # discriminant = 0 (one root)
        elif roots_num == 1:
            root_x = roots[0]
            low_x = min(vertex_x, root_x)
            high_x = max(vertex_x, root_x)
            points = [(x, get_y(a, b, c, x)) for x in np.arange(low_x - 5, high_x + 5, 0.1)]
            x, y = zip(*points)
            plt.plot(x, y)
            plt.plot(root_x, get_y(a, b, c, root_x), 'o', color='red')
        # discriminant > 0 (two roots)
        else:
            root_x1, root_x2 = roots
            low_x = min(root_x1, root_x2)
            high_x = max(root_x1, root_x2)
            points = [(x, get_y(a, b, c, x)) for x in np.arange(low_x - 5, high_x + 5, 0.1)]
            x, y = zip(*points)
            plt.plot(x, y)
            plt.plot((root_x1, root_x2), (get_y(a, b, c, root_x1), get_y(a, b, c, root_x2)), 'o', color='red')

        discriminant_sign = '<' if not roots else '=' if roots_num == 1 else '>'
        msg = f'Discriminant {discriminant_sign} 0 ⇒ equation has {roots_num} root(s): {roots}.'

    img = io.BytesIO()
    fig.savefig(img)
    img_encoded = base64.b64encode(img.getvalue()).decode('ascii')

    params = {
        'request': request,
        'plot': img_encoded,
        'coeff_a': a,
        'coeff_b': f'+ {b}' if b >= 0 else f'- {-b}',
        'coeff_c': f'+ {c}' if c >= 0 else f'- {-c}',
        'message': msg
    }
    return templates.TemplateResponse('plot.html', params)
