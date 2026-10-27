from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from database import Base, engine, SessionLocal
from app.domains.categories.category_router import router as category_router
from app.domains.products.product_router import router as product_router
from app.domains.products.models.product_model import Product as ProductModel

app = FastAPI()
app.include_router(category_router)
app.include_router(product_router)

Base.metadata.create_all(bind=engine)

templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    print("Request for index page received")
    return templates.TemplateResponse(request, "index.html", {"request": request})


@app.post("/hello", response_class=HTMLResponse)
async def hello(request: Request, name: str = Form(...)):
    if name:
        print("Request for hello page received with name=%s" % name)
        return templates.TemplateResponse(
            request, "hello.html", {"request": request, "name": name}
        )
    else:
        print(
            "Request for hello page received with no name or blank name -- redirecting"
        )
        return RedirectResponse(
            request.url_for("index"), status_code=status.HTTP_302_FOUND
        )


@app.get("/")
def print_hello():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
def get_name(name: str):
    return {"message": f"hello {name}"}


@app.get("/db-check")
def db_check():
    local_session = SessionLocal()
    product_count = local_session.query(ProductModel).count()
    return product_count
