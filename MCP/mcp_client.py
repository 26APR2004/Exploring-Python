from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import asyncio

from mcp import ClientSession
from mcp.client.sse import sse_client

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def root():
    return """
    <html>
        <body>
            <h2>Simple MCP Interface</h2>
            <button onclick="addNumbers()">Add 4 + 5</button>
            <p id="result"></p
            <script>
                async function addNumbers() {
                    const response = await fetch('/add');
                    const data = await response.json();
                    document.getElementById('result').innerText = 'Result: ' + data.result;
                }
            </script>
        </body>
    </html>
    """

@app.get("/add")
async def add():
    async with sse_client(url="http://localhost:8000/sse") as streams:
        async with ClientSession(*streams) as session:
            await session.initialize()
            result = await session.call_tool("add", arguments={"a": 4, "b": 5})
            # Assuming result.content[0].text holds the output number as string
            return {"result": result.content[0].text}
