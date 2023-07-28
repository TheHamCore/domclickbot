import json

from telegram import InlineKeyboardMarkup, InlineKeyboardButton


def prepare_keyboard(keyboard_data: dict[str, dict]):
    keyboard: list[list] = get_keyboard(data=keyboard_data)
    reply_markup = InlineKeyboardMarkup(keyboard)
    return reply_markup


def get_keyboard(data: dict) -> list[list]:
    keyboard: list = []
    for btn_name, payload in data.items():
        payload: str = json.dumps(payload)
        keyboard.append([InlineKeyboardButton(btn_name,
                                              callback_data=payload)])
    return keyboard
