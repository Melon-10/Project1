import uvicorn
from fastapi import FastAPI

app = FastAPI()
# 添加首页
@app.api_route("/login",methods=["get","post","put"])
def login():
    return {"msg":"This  is hen dou methods"}

if __name__ == '__main__':
    uvicorn.run(app)
