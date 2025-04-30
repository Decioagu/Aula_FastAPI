from fastapi import FastAPI
from fastapi.requests import Request
from fastapi.templating import Jinja2Templates


app = FastAPI(docs_url=None, redoc_url=None) # elimina pagina de documentação FastAPI

# ================================ CAMINHO DA URL ====================================
from fastapi.staticfiles import StaticFiles
import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Certifique-se de que o caminho está correto "Aula_25/templates"
templates = Jinja2Templates(directory=os.path.join(BASE_DIR, "templates"))

# Serve arquivos estáticos da pasta "Aula_25/static"
app.mount("/static", StaticFiles(directory=os.path.join(BASE_DIR, "static")), name="static")
# ===================================================================================

# Declaração de rotas do arquivo templates/base.html
@app.get('/', name="index")
async def index(request: Request):
    context = {
        "request": request
    }
    return templates.TemplateResponse('home/index.html', context=context)

@app.get("/about", name="about")
async def about(request: Request):
    context = {
        "request": request
    }
    return templates.TemplateResponse("home/about.html", context=context)

@app.get("/contact", name="contact")
async def contact(request: Request):
    context = {
        "request": request
    }
    return templates.TemplateResponse("home/contact.html", context=context)

@app.get("/pricing", name="pricing")
async def pricing(request: Request):
    context = {
        "request": request
    }
    return templates.TemplateResponse("home/pricing.html", context=context)

@app.get("/faq", name="faq")
async def faq(request: Request):
    context = {
        "request": request
    }
    return templates.TemplateResponse("home/faq.html", context=context)

@app.get("/blog", name="blog")
async def blog(request: Request):
    context = {
        "request": request
    }
    return templates.TemplateResponse("home/blog.html", context=context)

@app.get("/blog/post", name="blog_post")
async def blog_post(request: Request):
    context = {
        "request": request
    }
    return templates.TemplateResponse("home/blog_post.html", context=context)

@app.get("/portfolio", name="portfolio")
async def portfolio(request: Request):
    context = {
        "request": request
    }
    return templates.TemplateResponse("home/portfolio.html", context=context)

@app.get("/portfolio/item", name="portfolio_item")
async def portfolio_item(request: Request):
    context = {
        "request": request
    }
    return templates.TemplateResponse("home/portfolio_item.html", {"request": request})

if __name__ == '__main__':
    import uvicorn

    uvicorn.run(app="main:app", host="0.0.0.0", port=8000, log_level='info', reload=True)

# uvicorn Aula_25.main:app --reload

'''
Observação, o uso de:
    from fastapi.staticfiles import StaticFiles
    import os
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))

independe e a execução:
    Fora da pasta: uvicorn Aula_22.main:app --reload
    Dentro da pasta: uvicorn main:app --reload
'''
