import typer
import requests

app = typer.Typer()
API = "http://127.0.0.1:8000"  # base URL of the FastAPI server


# lists all servers
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


# show details of one server
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
    except Exception:
        print("api error.")


# add a new server
@app.command()
def add(
    title: str = typer.Option(..., "--title"),
    team: str = typer.Option(..., "--team"),
    cluster: str = typer.Option("", "--cluster"),
    plan: str = typer.Option("", "--plan"),
    auto_increase_storage: bool = typer.Option(False, "--auto_increase_storage"),
):
    # build request body from given options
    data = {
        "title": title,
        "team": team,
        "cluster": cluster,
        "plan": plan,
        "auto_increase_storage": auto_increase_storage,
    }
    try:
        r = requests.post(API + "/servers", json=data)
        if r.status_code == 200:
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
):

    data = {}
    if title:
        data["title"] = title
    if team:
        data["team"] = team
    if cluster:
        data["cluster"] = cluster
    if plan:
        data["plan"] = plan

    try:
        r = requests.put(API + f"/servers/{sid}", json=data)
        result = r.json()
        if "error" in result:
            print("server not found")
        else:
            print("server updated!")
    except Exception:
        print("api error.")


# delete a server by id
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
