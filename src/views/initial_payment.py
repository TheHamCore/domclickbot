from telegram import Update
from telegram.ext import ContextTypes

from src.ui_interface.start_menu import start_data_exit
from src.utility.check_context import check_context
from src.utility.keyboard import prepare_keyboard


async def get_credit(update: Update,
                              context: ContextTypes.DEFAULT_TYPE):
    check_context(context=context,
                  update=update)
    query = update.callback_query
    await query.edit_message_text('Введите, пожалуйста, сумму, которую вы хотите оформить в кредит.')

    reply_markup = prepare_keyboard(keyboard_data=start_data_exit)
    context.user_data['full_amount'] = True
    await query.message.edit_reply_markup(reply_markup=reply_markup)