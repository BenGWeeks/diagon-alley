from fastapi import APIRouter
from lnbits.db import Database
from lnbits.helpers import template_renderer

db = Database("ext_diagonalley")

diagonalley_ext: APIRouter = APIRouter(prefix="/diagonalley", tags=["diagonalley"])

diagonalley_static_files = [
    {
        "path": "/diagonalley/static",
        "name": "diagonalley_static",
    }
]


def diagonalley_renderer():
    return template_renderer(["diagonalley/templates"])


from .views import *  # noqa
