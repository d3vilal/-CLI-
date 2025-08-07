from fastapi import FastAPI

app = FastAPI()

servers = [
    {"id": 1, "title": "main server", "team": "skibidi", "cluster": "mumbai", "plan": "pro", "auto_increase_storage": False},
    {"id": 2, "title": "backup", "team": "giga", "cluster": "delhi", "plan": "basic", "auto_increase_storage": True}
]

@app.get("/servers")
def read_servers():
    return servers

@app.get("/servers/{sid}")
def read_server(sid: int):
    for s in servers:
        if s["id"] == sid:
            return s
    return {"error": "server not found"}

@app.post("/servers")
def add_server(s: dict):
    servers.append(s)
    return s
