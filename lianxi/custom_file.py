import uvicorn
from fastapi import FastAPI
from fastapi.responses import JSONResponse,HTMLResponse
from starlette.responses import FileResponse

app=FastAPI()

@app.get("/user")
def user():
    return JSONResponse(content={"msg":"get user"},
                        status_code=202,
                        headers={"a":"b"})

@app.get("/")
def user():
    html_content="""
    <html>
        <body><p style="color:red">Hello World</p></body>
        </html>
    """
    return HTMLResponse(content=html_content)

@app.get("/avatar")
def user():
    avatar='./static/111a.png'
    return FileResponse(avatar)

if __name__ == '__main__':
    uvicorn.run(app)