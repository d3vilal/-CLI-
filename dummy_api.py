from fastapi import FastAPI

# FastAPI app
app = FastAPI()

# Simple in-memory data (resets on restart)
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


# List all servers
@app.get("/servers")
def get_servers():
    return servers


# Get one server by ID
@app.get("/servers/{server_id}")
def get_server(server_id: int):
    for server in servers:
        if server["id"] == server_id:
            return server
    return {"error": "server not found"}


# Create a new server
@app.post("/servers")
def create_server(server_data: dict):
    new_id = max((s["id"] for s in servers), default=0) + 1
    server_data["id"] = new_id
    servers.append(server_data)
    return server_data


# Update a server (partial fields ok)
@app.put("/servers/{server_id}")
def update_server(server_id: int, server_data: dict):
    for i, server in enumerate(servers):
        if server["id"] == server_id:
            servers[i].update(server_data)
            return servers[i]
    return {"error": "server not found"}


# Delete a server
@app.delete("/servers/{server_id}")
def delete_server(server_id: int):
    for i, server in enumerate(servers):
        if server["id"] == server_id:
            deleted = servers.pop(i)
            return {"message": "server deleted", "deleted": deleted}
    return {"error": "server not found"}
