import typer
import requests

app = typer.Typer()
API = "http://127.0.0.1:8000"

@app.command()
def list():
    try:
        r = requests.get(API + "/servers")
        servers = r.json()
        if not servers:
            print("no servers found.")
            return
        for s in servers:
            print(f"{s['id']}: {s['title']} ({s.get('plan', '-')})")
    except Exception:
        print("api error.")

@app.command()
def info(sid: int):
    try:
        r = requests.get(API + f"/servers/{sid}")
        s = r.json()
        if "error" in s:
            print("server not found")
        else:
            print(f"id: {s['id']}")
            print(f"title: {s.get('title', '-')}")
            print(f"team: {s.get('team', '-')}")
            print(f"cluster: {s.get('cluster', '-')}")
            print(f"plan: {s.get('plan', '-')}")
            print(f"auto increase storage: {s.get('auto_increase_storage', '-')}")
    except Exception:
        print("api error.")

@app.command()
def add(
    title: str = typer.Option(..., "--title"),
    team: str = typer.Option(..., "--team"),
    cluster: str = typer.Option("", "--cluster"),
    plan: str = typer.Option("", "--plan"),
    auto_increase_storage: bool = typer.Option(False, "--auto-increase-storage"),
):
    try:
        r = requests.get(API + "/servers")
        servers = r.json()
        new_id = max([s["id"] for s in servers], default=0) + 1
    except Exception:
        new_id = 1
    data = {
        "id": new_id,
        "title": title,
        "team": team,
        "cluster": cluster,
        "plan": plan,
        "auto_increase_storage": auto_increase_storage
    }
    try:
        added = requests.post(API + "/servers", json=data)
        if added.status_code == 200:
            print("server added!")
        else:
            print("could not add server.")
    except Exception:
        print("api error.")

@app.command()
def update(
    sid: int,
    title: str = typer.Option("", "--title"),
    team: str = typer.Option("", "--team"),
    cluster: str = typer.Option("", "--cluster"),
    plan: str = typer.Option("", "--plan"),
    auto_increase_storage: bool = typer.Option(None, "--auto-increase-storage"),
):
    try:
        r = requests.get(API + f"/servers/{sid}")
        current = r.json()
        if "error" in current:
            print("server not found")
            return
        
        if title:
            current["title"] = title
        if team:
            current["team"] = team
        if cluster:
            current["cluster"] = cluster
        if plan:
            current["plan"] = plan
        if auto_increase_storage is not None:
            current["auto_increase_storage"] = auto_increase_storage
        
        updated = requests.put(API + f"/servers/{sid}", json=current)
        if updated.status_code == 200:
            print("server updated!")
        else:
            print("could not update server.")
    except Exception:
        print("api error.")

@app.command()
def delete(sid: int):
    try:
        r = requests.delete(API + f"/servers/{sid}")
        result = r.json()
        if "error" in result:
            print("server not found")
        else:
            print("server deleted!")
    except Exception:
        print("api error.")

if __name__ == "__main__":
    app()
