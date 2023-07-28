from src.ui_interface.ui_template import get_ui_template

start_data_ui: dict[str, dict] = {
        'Запросить сумму на ипотеку': get_ui_template(callback='get_credit'),
}

start_data_exit: dict[str, dict] = {
        'Назад 🔙': get_ui_template(callback='back_to_menu')
}