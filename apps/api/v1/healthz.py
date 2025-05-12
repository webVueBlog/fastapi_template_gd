

# @File    : example
# @Desc    : 测试
from fastapi import APIRouter
from tortoise import Tortoise
router = APIRouter()


@router.get('/healthz/', summary='健康检查')
async def monitor():
    return 'ok'
