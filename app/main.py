from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def read_root():
    return """
    <html>
        <body>
            <h2>Hello, World!</h2>
            <p>This is a FastAPI application served by Uvicorn.</p>
            <p>The source code is in the file 'app/main.py'.</p>
            <p>The server is started with the following command: </p>
            <code>uvicorn main:app --host 0.0.0.0 --port 8080</code>
            <p>See the serve.sh file.</p>

        </body>
    </html>
    """
