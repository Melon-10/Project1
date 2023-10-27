import uvicorn
from fastapi import FastAPI,Header,Form
from fastapi.responses import JSONResponse,HTMLResponse

app=FastAPI()

@app.get("/")
def user():
    html_content="""
    <html>
    <head>
    <meta charset="utf-8"/>
    <title>测试主页</title>
        <body>
        <p style="color:red">Welcome !</p>
        <img src="https://auto.youth.cn/xw/202310/W020231026550359809120.jpg" width="800px" height="500px">
        </body>
        </html>
    """
    return HTMLResponse(content=html_content)

@app.get("/user")
def user(id, token=Header(None)):
    return {"id":id,"token":token}

@app.post("/login")
def user(username=Form(None),password=Form(None)):
    if username=="123" and password=='aaa':
        return JSONResponse(content={"data":{"code":"1","username":username,"password":password}},
                            status_code=200,
                            headers={"token":"98u98hfwehf9823rh"})

    else:
        return JSONResponse(content={"code":"-1","msg":"账号或密码错误"})

if __name__ == '__main__':
    uvicorn.run(app)