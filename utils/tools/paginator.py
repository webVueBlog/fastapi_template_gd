

# @File    : paginator.py
# @Desc    : 分页功能


async def paginator(qs, page: int = 1, page_size: int = 15) -> list:
    """
    分页器
    :param qs:  QuerySet object
    :param page: 第n页
    :param page_size: 每页条数
    """
    offset = (page - 1) * page_size
    limit = page_size
    return await qs.offset(offset).limit(limit)
