"""
Web application architecture.
"""
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from uvicorn import run

from modules.db_manager import LootDatabase

loot_db = None
app = FastAPI(title="NVBLootChecker")
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})

@app.get("/verify/{loot_uuid}", response_class=HTMLResponse)
async def verify(request: Request, loot_uuid: str):
    loot_infos = loot_db.get_loot_by_uuid(loot_uuid)
    if loot_infos is None:
        return templates.TemplateResponse("uuid_error.html", {"request": request})
    else:
        if loot_infos['checked']:
            return templates.TemplateResponse("not_ok.html", {"request": request})
        else:
            loot_db.set_loot_checked_by_uuid(loot_uuid)
            return templates.TemplateResponse("ok.html", {"request": request, "loot_name": loot_infos['name']})

@app.get("/reset/{loot_uuid}", response_class=HTMLResponse)
async def reset(request: Request, loot_uuid: str):
    loot_infos = loot_db.get_loot_by_uuid(loot_uuid)
    if loot_infos is None:
        return templates.TemplateResponse("uuid_error.html", {"request": request})
    else:
        if loot_infos['checked']:
            loot_db.reset_loot_checked_by_uuid(loot_uuid)
            return templates.TemplateResponse("reset_ok.html", {"request": request, "loot_name": loot_infos['name'], "loot_uuid": loot_uuid})
        else:
            return templates.TemplateResponse("already_zero.html", {"request": request, "loot_name": loot_infos['name'], "loot_uuid": loot_uuid})

def run_app(host: str, port: int, db_path: str):
    global loot_db
    loot_db = LootDatabase(db_path)
    run(app, host=host, port=port)
