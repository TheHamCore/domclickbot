from telegram import Update
from telegram.ext import CallbackContext

from src.cfg.config import MAX_CREDIT, MIN_CREDIT
from src.logger.logger_settings import logger
from src.ui_interface.start_menu import start_data_ui
from src.utility.keyboard import prepare_keyboard
from src.utility.render import render_new_dialog_window
from src.utility.telegram_form_parser import UserInfo


async def text_handler(update: Update, context: CallbackContext):
    user_info: UserInfo = UserInfo(**update.to_dict())
    text: str = user_info.message.text.strip()

    # ------
    full_amount: bool or None = context.user_data.get('full_amount')
    init_payment: bool or None = context.user_data.get('init_payment')
    if full_amount:
        return await full_amount_handler(update=update,
                                         user_info=user_info,
                                         context=context,
                                         text=text)
    if init_payment:
        return await init_payment_handler(update=update,
                                          user_info=user_info,
                                          context=context,
                                          text=text)

    reply_markup = prepare_keyboard(keyboard_data=start_data_ui)
    return await context.bot.send_message(text=f'Я не понимаю команду {text}.',
                                          chat_id=user_info.message.chat.telegram_chat_id,
                                          reply_markup=reply_markup)


async def init_payment_handler(update,
                               context,
                               user_info: UserInfo,
                               text: str):
    print('heresese')
    context.user_data['init_payment']: bool = False
    context.user_data['full_amount']: bool = False
    init_payment: float or None = await check_input(context=context,
                                                    user_info=user_info,
                                                    text=text,
                                                    reset="init_payment")
    if not isinstance(init_payment, float):
        return

    full_payment: float = context.user_data['full_payment']
    if full_payment <= init_payment:
        context.user_data['init_payment']: bool = True
        logger.error(f'Первоначальная сумма больше кредита.')
        return await context.bot.send_message(text=f'Первоначальная сумма "{init_payment}" больше '
                                                   f'запрашиваемого кредита в размере "{full_payment}".\n'
                                                   f'Попробуйте снова.',
                                              chat_id=user_info.message.chat.telegram_chat_id)
    if init_payment <= 0:
        context.user_data['init_payment']: bool = True
        logger.error(f'Первоначальная сумма должна быть больше нуля.')
        return await context.bot.send_message(text=f'Первоначальная сумма должна быть больше нуля.\n'
                                                   f'Попробуйте снова.',
                                              chat_id=user_info.message.chat.telegram_chat_id)

    is_valid: bool = is_valid_percent(init_payment=init_payment,
                                      full_payment=full_payment)
    if not is_valid:
        context.user_data['init_payment']: bool = True
        logger.error(f'ПВ меньше 15 %.')
        is_valid_init_payment: float = full_payment * 0.15
        return await context.bot.send_message(text=f'Первоначальная сумма должна быть больше или равна 15%.\n'
                                                   f'Ваш первоначальный взнос "{init_payment}".\n'
                                                   f'Минимальная сумма должна быть {is_valid_init_payment}.',
                                              chat_id=user_info.message.chat.telegram_chat_id)

    context.user_data['full_amount']: None = None
    context.user_data['full_payment']: None = None

    reply_markup = prepare_keyboard(keyboard_data=start_data_ui)
    return await context.bot.send_message(text=f'Спасибо, ваша заявка отправлена.\n'
                                               f'Напомним Вам, что Вы можете оставить заявку через\n'
                                               f'наш сайт по адресу https://domclick.ru/ipoteka/programs/onlajn-zayavka.',
                                          chat_id=user_info.message.chat.telegram_chat_id,
                                          reply_markup=reply_markup)


def is_valid_percent(init_payment: float,
                     full_payment: float):
    percent: float = (100 * init_payment) / full_payment
    if percent < 15:
        return False
    return True


async def full_amount_handler(update: Update,
                              context,
                              user_info: UserInfo,
                              text: str
                              ):
    context.user_data['full_amount']: bool = False

    full_amount: float or None = await check_input(context=context,
                                                   user_info=user_info,
                                                   text=text,
                                                   reset="full_amount")
    if not isinstance(full_amount, float):
        return

    if not MIN_CREDIT < full_amount < MAX_CREDIT:
        context.user_data['full_amount']: bool = True
        logger.error(f'Неверно введенная сумма: {full_amount}')
        return await context.bot.send_message(text=f'Вы ввели сумму равной "{full_amount}".'
                                                   f'Мы выдаем ипотеку от "{MIN_CREDIT}" до "{MAX_CREDIT}".\n'
                                                   f'Попробуйте снова.',
                                              chat_id=user_info.message.chat.telegram_chat_id)

    context.user_data['full_amount']: bool = False
    context.user_data['full_payment']: float = full_amount
    context.user_data['init_payment']: bool = True
    return await context.bot.send_message(text=f'Вам необходим кредит в размере "{full_amount}".\n'
                                               f'Введите пожалуйста сумму вашего первоначального взноса.\n'
                                               f'Первоначальный взнос должен быть не меньше 15% от суммы кредита.',
                                          chat_id=user_info.message.chat.telegram_chat_id)


async def check_input(text: str,
                      context,
                      user_info,
                      reset: str) -> float or None:
    try:
        full_amount: float = float(text)
    except ValueError as e:
        context.user_data[reset]: bool = True
        logger.error(f'Неверно введенная сумма: {e}')
        return await context.bot.send_message(text='Cумма должна быть цифрой, попробуйте снова',
                                              chat_id=user_info.message.chat.telegram_chat_id)
    return full_amount
