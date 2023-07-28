async def render_new_dialog_window(context,
                                   chat_id: int,
                                   reply_markup: list,
                                   text: str):
    return await context.bot.send_message(text=text,
                                          chat_id=chat_id,
                                          reply_markup=reply_markup)