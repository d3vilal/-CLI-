Simple Server Manager (FastAPI + Typer CLI)
A minimal project to manage “servers” using:

FastAPI backend (in-memory CRUD)

Typer CLI that calls the API via HTTP

Clean, beginner-friendly code

What it does

List all servers

Get server details by ID

Create a server

Update a server (only the fields you pass)

Delete a server

Tech Stack

Python 3.10+

FastAPI

Uvicorn

Typer

requests

Project Structure

dummy_api.py — FastAPI app exposing CRUD endpoints

cli_app.py — Typer CLI that calls the API

pycache/ — Python cache (ignored)

Setup

Clone

git clone <your-repo-url>

cd <repo-folder>

Virtual env

python -m venv .venv

.venv\Scripts\activate (Windows)

source .venv/bin/activate (macOS/Linux)

Install dependencies

pip install fastapi uvicorn typer requests

Run the API

uvicorn dummy_api:app --reload

API base: http://127.0.0.1:8000

Docs: http://127.0.0.1:8000/docs

Use the CLI
In another terminal (with venv activated):

python cli_app.py list

python cli_app.py info 1

python cli_app.py add --title "web" --team "dev" --cluster "mumbai" --plan "basic" --auto_increase_storage

python cli_app.py update 1 --title "web-updated" --plan "premium"

python cli_app.py delete 1

Notes

The API stores data in memory (a Python list). Restarting the server resets data.

The CLI assumes API at http://127.0.0.1:8000. If you change it, update API variable in cli_app.py.

This is a learning/demo project. For production, add a database, validation (Pydantic), auth, and better error handling.