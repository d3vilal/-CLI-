from fastapi import FastAPI

app = FastAPI()
servers = [
    {
        "id": 1,
        "title": "main_server",
        "team": "bird",
        "cluster": "mumbai",
        "plan": "basic",
        "auto_increase_storage": False,
    },
    {
        "id": 2,
        "title": "backup_server",
        "team": "bird",
        "cluster": "mumbai",
        "plan": "basic",
        "auto_increase_storage": False,
    },
]


@app.get("/servers")
def get_servers():
    return servers


@app.get("/servers/{server_id}")
def get_server(server_id: int):
    for server in servers:
        if server["id"] == server_id:
            return server
    return {"error": "server not found"}


@app.post("/servers")
def create_server(server_data: dict):
    if servers:
        new_id = max(server["id"] for server in servers) + 1
    else:
        new_id = 1
    server_data["id"] = new_id
    servers.append(server_data)
    return server_data


@app.put("/servers/{server_id}")
def update_server(server_id: int, server_data: dict):
    for i, server in enumerate(servers):
        if server["id"] == server_id:
            servers[i].update(server_data)
            return servers[i]
    return {"error": "server not found"}


@app.delete("/servers/{server_id}")
def delete_server(server_id: int):
    for i, server in enumerate(servers):
        if server["id"] == server_id:
            deleted_server = servers.pop(i)
            return {"message": "server deleted", "deleted": deleted_server}

    return {"error": "server not found"}
