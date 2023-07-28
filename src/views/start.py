from datetime import datetime

from telegram import Update
from telegram.ext import ContextTypes

from src.database.repository import repository
from src.ui_interface.start_menu import start_data_ui
from src.utility.keyboard import prepare_keyboard
from src.utility.telegram_form_parser import UserInfo


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data['full_amount']: None = None
    context.user_data['full_payment']: None = None
    user_info: UserInfo = UserInfo(**update.to_dict())
    context.user_data['telegram_chat_id'] = user_info.message.chat.telegram_chat_id
    if not repository.repo_user.is_user_exist(telegram_chat_id=user_info.message.chat.telegram_chat_id):
        await context.bot.send_message(text=f'{user_info.message.chat.first_name}, '
                                            f'добро пожаловать в бот "Дом Клик"!\n'
                                            f'Вы можете оставить заявку через\n'
                                            f'наш сайт по адресу https://domclick.ru/ipoteka/programs/onlajn-zayavka.',
                                       chat_id=user_info.message.chat.telegram_chat_id)

        repository.repo_user.register_user(first_name=user_info.message.chat.first_name,
                                           telegram_chat_id=user_info.message.chat.telegram_chat_id,
                                           date=datetime.now().date())

    reply_markup = prepare_keyboard(keyboard_data=start_data_ui)
    await update.message.reply_text(text="Главное меню",
                                    reply_markup=reply_markup)
