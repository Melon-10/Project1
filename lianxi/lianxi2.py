import uvicorn
from fastapi import FastAPI,Request
from fastapi.templating import Jinja2Templates

app=FastAPI()
template=Jinja2Templates("pages")

@app.get("/")
def user(req:Request):
    return template.TemplateResponse("index.html",context={"request":req})

if __name__ == '__main__':
    uvicorn.run(app)