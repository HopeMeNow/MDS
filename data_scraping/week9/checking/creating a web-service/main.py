#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import base64
import io
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

mpl.use("AGG")
mpl.style.use("seaborn")

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


def solve_equation(a: int, b: int, c: int):
    roots = np.roots([a, b, c])
    roots = np.unique(roots[np.isreal(roots)]).tolist()

    return roots


@app.get("/solve")
def solve(a: int, b: int, c: int):
    return {"roots": solve_equation(a, b, c)}


@app.get("/main", response_class=HTMLResponse)
def main(request: Request):
    return templates.TemplateResponse("main.html", {"request": request})


@app.post("/plot")
def plot(request: Request, a: int = Form(...), b: int = Form(...), c: int = Form(...)):
    f = lambda x: a * x ** 2 + b * x + c
    roots = solve_equation(a, b, c)

    if roots:
        roots_desc = f"Roots of the equation are: {roots}"
        x = np.linspace(min(roots) - 5, max(roots) + 5, num=100)
    elif a != 0:
        roots_desc = "There are no real roots of the equation"
        x = np.linspace(-b / 2 / a - 5, -b / 2 / a + 5, num=100)
    else:
        roots_desc = "There are no real roots of the equation"
        x = np.linspace(-5, 5, num=100)

    fig = plt.figure(figsize=(8, 6))

    plt.axhline(y=0, linewidth=1, color="tab:grey", zorder=1)
    plt.axvline(x=0, linewidth=1, color="tab:grey", zorder=1)
    plt.plot(x, f(x), linewidth=3, color="tab:blue", label="graph", zorder=2)
    plt.scatter(
        roots, np.zeros_like(roots), s=100, color="tab:red", label="roots", zorder=3
    )
    plt.legend(loc="best")

    png_img = io.BytesIO()

    fig.savefig(png_img, bbox_inches="tight")
    base64_str = base64.b64encode(png_img.getvalue()).decode("ascii")

    return templates.TemplateResponse(
        "plot.html",
        {"request": request, "plot_img": base64_str, "roots_desc": roots_desc},
    )

