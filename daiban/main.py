import uvicorn
import asyncio
from fastapi import FastAPI, Request, Form
from fastapi.responses import RedirectResponse
from starlette.templating import Jinja2Templates
from tortoise.contrib.fastapi import register_tortoise

from daiban.dao.models import Todo

app=FastAPI()
template=Jinja2Templates("pages")

# 数据库绑定
register_tortoise(app,db_url="mysql://root:123456@localhost:3306/fastapi",
                  modules={"models":['dao.models']},
                  add_exception_handlers=True,
                  generate_schemas=True)

todos = ["写日记", "看电影", "玩游戏"]

# 添加首页
@app.get("/")
async def user(req:Request):
    todos=await Todo.all()
    print(todos)
    return template.TemplateResponse("index.html",context={"request":req,"todos":todos})

@app.post("/todo")
def todo(todo=Form(None)):
    todos.insert(0,todo)
    return RedirectResponse("/",status_code=302)

if __name__ == '__main__':
    uvicorn.run(app)