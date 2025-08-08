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

@app.put("/servers/{sid}")
def update_server(sid: int, updated_data: dict):
    for i, s in enumerate(servers):
        if s["id"] == sid:
            updated_data["id"] = sid
            servers[i] = updated_data
            return servers[i]
    return {"error": "server not found"}

@app.delete("/servers/{sid}")
def delete_server(sid: int):
    for i, s in enumerate(servers):
        if s["id"] == sid:
            deleted = servers.pop(i)
            return {"message": "server deleted", "deleted": deleted}
    return {"error": "server not found"}
