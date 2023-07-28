
def check_context(context,
                  update):
    if not context.user_data:
        context.user_data['telegram_chat_id'] = update.to_dict()['callback_query']['from']['id']