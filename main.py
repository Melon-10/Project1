import uvicorn
from fastapi import FastAPI

app = FastAPI()
# 添加首页
@app.get("/")
def index():
    "这里是首页"
    return "This is Home Page."

@app.get("/users")
def users():
    "这里是用户"
    return {"meg":"Get aii users","code":200}

@app.post("/login")
def login():
    "登录"
    return {"meg":"login success","code":200}


if __name__ == '__main__':
    uvicorn.run(app)

