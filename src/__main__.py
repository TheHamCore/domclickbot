from src.cfg.config import TOKEN
from src.command_handler.text_handler import text_handler
from src.router.router import router
from telegram.ext import ApplicationBuilder, CallbackQueryHandler, CommandHandler, MessageHandler, filters
from telegram import Update
from src.logger.logger_settings import logger
from src.views.start import start


def main():
    application = ApplicationBuilder().token(TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(router))
    application.add_handler(MessageHandler(filters.TEXT, text_handler))
    logger.info('start')
    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == '__main__':
    main()
