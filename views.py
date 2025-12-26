from fastapi import Depends, Request
from fastapi.templating import Jinja2Templates
from lnbits.core.models import User
from lnbits.decorators import check_user_exists
from starlette.responses import HTMLResponse

from . import diagonalley_ext, diagonalley_renderer

templates = Jinja2Templates(directory="templates")


@diagonalley_ext.get("/", response_class=HTMLResponse)
async def index(request: Request, user: User = Depends(check_user_exists)):
    return diagonalley_renderer().TemplateResponse(
        "diagonalley/index.html",
        {"request": request, "user": user.json()},
    )


@diagonalley_ext.get("/market", response_class=HTMLResponse)
async def market(request: Request):
    return diagonalley_renderer().TemplateResponse(
        "diagonalley/market.html",
        {"request": request},
    )
