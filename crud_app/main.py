from fastapi import FastAPI, Request

from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from crud_app.blog import models
from crud_app.blog.database import engine

# from crud_app.blog.routers import items, blogs, users, authentication


models.Base.metadata.create_all(engine)

app = FastAPI()

# Static Files and Templates
app.mount("/static", StaticFiles(directory="crud_app/static"), name="static")

templates = Jinja2Templates(directory="crud_app/templates")

# Routers
# app.include_router(items.router)
# app.include_router(blogs.router)
# app.include_router(users.router)
# app.include_router(authentication.router)


# Home Page
@app.get("/", response_class=HTMLResponse, include_in_schema=False)
def landing_page(request: Request):
    data = {"page": "Home page"}
    return templates.TemplateResponse("index.html", {"request": request, "data": data})
