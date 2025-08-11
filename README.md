

# Simple Server Manager (FastAPI + Typer CLI)

A minimal project to manage “servers” using:

- FastAPI backend (in-memory CRUD)
- Typer CLI that calls the API via HTTP
- Clean, beginner-friendly code


## Repository

- GitHub: https://github.com/d3vilal/-CLI-


## What It Does

- List all servers
- Get server details by ID
- Create a server
- Update a server (only the fields passed)
- Delete a server


## Tech Stack

- Python 3.10+
- FastAPI
- Uvicorn
- Typer
- requests


## Project Structure

- dummy_api.py — FastAPI app exposing CRUD endpoints
- cli_app.py — Typer CLI that calls the API



## Setup

### 1) Clone the repo

```bash
git clone https://github.com/d3vilal/-CLI-.git
cd -CLI-
```


### 2) Create and activate virtual environment

```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate
```


### 3) Install dependencies

```bash
pip install fastapi uvicorn typer requests
```


## Run the API

```bash
uvicorn dummy_api:app --reload
```

- API base URL: http://127.0.0.1:8000
- Swagger docs: http://127.0.0.1:8000/docs
- ReDoc docs: http://127.0.0.1:8000/redoc


## Use the CLI

In another terminal (with the virtual environment activated):

```bash
python cli_app.py list
python cli_app.py info 1
python cli_app.py add --title "web" --team "dev" --cluster "mumbai" --plan "basic" --auto_increase_storage
python cli_app.py update 1 --title "web-updated" --plan "premium"
python cli_app.py delete 1
```


## Default API URL in CLI

- The CLI expects the API at http://127.0.0.1:8000.
- To change it, edit:

```python
API = "http://127.0.0.1:8000"  # in cli_app.py
```


## API Endpoints

- GET http://127.0.0.1:8000/servers
- GET http://127.0.0.1:8000/servers/{server_id}
- POST http://127.0.0.1:8000/servers
- PUT http://127.0.0.1:8000/servers/{server_id}
- DELETE http://127.0.0.1:8000/servers/{server_id}


## Example Server JSON

```json
{
  "id": 1,
  "title": "main_server",
  "team": "bird",
  "cluster": "mumbai",
  "plan": "basic",
  "auto_increase_storage": false
}

