<img src="https://r2cdn.perplexity.ai/pplx-full-logo-primary-dark%402x.png" style="height:64px;margin-right:32px"/>

# make it markdown file for me to copy

Here’s the complete README.md content formatted as Markdown. You can copy-paste it directly into your README.md file.

# Simple Server Manager (FastAPI + Typer CLI)

A minimal project to manage “servers” using:

- FastAPI backend (in-memory CRUD)
- Typer CLI that calls the API via HTTP
- Clean, beginner-friendly code


## What It Does

- List all servers
- Get server details by ID
- Create a server
- Update a server (only the fields you pass)
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
- __pycache__/ — Python cache (ignored)


## Setup

### 1) Clone

```bash
git clone <your-repo-url>
cd <repo-folder>
```


### 2) Virtual env

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

- API base: http://127.0.0.1:8000
- Docs: http://127.0.0.1:8000/docs


## Use the CLI

In another terminal (with venv activated):

```bash
python cli_app.py list
python cli_app.py info 1
python cli_app.py add --title "web" --team "dev" --cluster "mumbai" --plan "basic" --auto_increase_storage
python cli_app.py update 1 --title "web-updated" --plan "premium"
python cli_app.py delete 1
```


## Notes

- The API stores data in memory (a Python list). Restarting the server resets data.
- The CLI assumes API at http://127.0.0.1:8000. If you change it, update the API variable in cli_app.py.
- This is a learning/demo project. For production, add a database, validation (Pydantic), auth, and better error handling.

