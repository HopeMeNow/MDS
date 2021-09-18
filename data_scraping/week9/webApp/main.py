from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import io
import base64

matplotlib.use('Agg')

app = FastAPI()

templates = Jinja2Templates(directory='templates')


def is_int(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


def solve_equation(a, b, c):
    roots = np.roots([a, b, c])
    if (np.any(np.iscomplex(roots))):
        return []
    return list(roots)


@app.get('/solve')
async def solve(a, b, c):
    if is_int(a) and int(a) == 0:
        return 'Error: parameter a must be not zero'
    if not is_int(a) or not is_int(b) or not is_int(c):
        return 'Error: All coefficients should be integer'
    a, b, c = int(a), int(b), int(c)
    return {'roots': set(list(map(int, solve_equation(a, b, c))))}


@app.get('/main')
async def main(request: Request):
    return templates.TemplateResponse('index.html', {'request': request})


@app.post('/plot_graph')
async def plot_graph(
    request: Request,
    a: str = Form(...),
    b: str = Form(...),
    c: str = Form(...)
):
    if is_int(a) and int(a) == 0:
        return templates.TemplateResponse(
            'error.html',
            {
                'request': request,
                'error_message': 'Parameter "a" must be not zero'
            }
        )
    if not is_int(a) or not is_int(b) or not is_int(c):
        return templates.TemplateResponse(
            'error.html',
            {
                'request': request,
                'error_message': 'All coefficients should be integer'
            }
        )

    a, b, c = int(a), int(b), int(c)

    roots = solve_equation(a, b, c)
    if len(roots) > 0:
        x = np.linspace(roots[0]-10, roots[1]+10, 1000)

        y = a*x**2 + b*2*x + c

        fig = plt.figure()
        plt.plot(x, y)
        plt.axvline(x=roots[0], color='r')
        plt.axvline(x=roots[1], color='r')

        pngImage = io.BytesIO()
        fig.savefig(pngImage)

        pngImageBase64 = base64.b64encode(pngImage.getvalue()).decode('ascii')
        return templates.TemplateResponse(
            'plot.html',
            {'request': request, 'picture': pngImageBase64}
        )
    else:
        return templates.TemplateResponse(
            'error.html',
            {
                'request': request,
                'error_message': 'Quadratic equation has no roots'
            }
        )
