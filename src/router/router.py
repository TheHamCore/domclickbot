import json

from src.views.credit import get_credit


async def router(update, context):
    query = update.callback_query
    payload_data: dict = json.loads(query.data)

    print(payload_data, 'HHHEEERES')

    callback: callable = get_routers(func=payload_data['callback'])
    print(callback, 222211312212121)
    await callback(update=update, context=context)


def get_routers(func) -> callable:
    return {
        'get_credit': get_credit,
        'back_to_menu': get_credit
    }[func]

    # print(query)
    # logger.debug(f'Callback is {routers[query.data]}')
    # await routers[query.data](update,
    #                           context)
