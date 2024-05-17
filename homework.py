from datetime import time


def test_dark_theme_by_time():
    """
    Протестируйте правильность переключения темной темы на сайте в зависимости от времени
    """
    current_time = time(hour=0)
    is_dark_theme = None

    if time(hour=21) >= current_time > time(hour=6):
        is_dark_theme = False
    else:
        is_dark_theme = True

    assert is_dark_theme is True

# 0 - ночь, темная тема
# 1 - ночь, темная тема
# 2 - ночь, темная тема
# 3 - ночь, темная тема
# 4 - ночь, темная тема
# 5 - ночь, темная тема

# 6 - день, светлая тема
# 7 - день, светлая тема
# 8 - день, светлая тема
# 9 - день, светлая тема
# 10 - день, светлая тема
# 11 - день, светлая тема
# 12 - день, светлая тема
# 13 - день, светлая тема
# 14 - день, светлая тема
# 15 - день, светлая тема
# 16 - день, светлая тема
# 17 - день, светлая тема
# 18 - день, светлая тема
# 19 - день, светлая тема
# 20 - день, светлая тема
# 21 - день, светлая тема

# 22 - ночь, темная тема
# 23 - ночь, темная тема


def test_dark_theme_by_time_and_user_choice():
    """
    Протестируйте правильность переключения темной темы на сайте
    в зависимости от времени и выбора пользователя
    dark_theme_enabled_by_user = True - Темная тема включена
    dark_theme_enabled_by_user = False - Темная тема выключена
    dark_theme_enabled_by_user = None - Пользователь не сделал выбор (используется переключение по времени системы)
    """
    current_time = time(hour=7)
    # (с 22 до 6 часов утра - ночь)

    is_dark_theme = None
    dark_theme_enabled_by_user = True

    if dark_theme_enabled_by_user:
        is_dark_theme = dark_theme_enabled_by_user
    elif dark_theme_enabled_by_user is None:
        if time(hour=21) >= current_time > time(hour=6):
            is_dark_theme = False
        else:
            is_dark_theme = True

    assert is_dark_theme is True


def test_find_suitable_user():
    """
    Найдите нужного пользователя по условиям в списке пользователей
    """
    users = [
        {"name": "Oleg", "age": 32},
        {"name": "Sergey", "age": 24},
        {"name": "Stanislav", "age": 15},
        {"name": "Olga", "age": 45},
        {"name": "Maria", "age": 18},
    ]


    users.sort(key=lambda user: user['name'] == 'Olga', reverse=True)
    suitable_users = users[0]

    assert suitable_users == {"name": "Olga", "age": 45}

    suitable_users = []

    for user in users:
        for k, v in user.items():
            if k == 'age' and int(v) < 20:
                suitable_users.append(user)

    assert suitable_users == [
        {"name": "Stanislav", "age": 15},
        {"name": "Maria", "age": 18},
    ]


# Сделайте функцию, которая будет печатать
# читаемое имя переданной ей функции и значений аргументов.
# Вызовите ее внутри функций, описанных ниже
# Подсказка: Имя функции можно получить с помощью func.__name__
# Например, вызов следующей функции должен преобразовать имя функции
# в более читаемый вариант (заменить символ подчеркивания на пробел,
# сделать буквы заглавными (или первую букву), затем вывести значения всех аргументов этой функции:
# >>> open_browser(browser_name="Chrome")
# "Open Browser [Chrome]"


def print_function_name_and_args(func, *args):
    func_name = func.__name__.replace('_', ' ').title()
    args_name = ", ".join([*args])
    print(f"{func_name} [{args_name}]")

    return f"{func_name} [{args_name}]"


def test_readable_function():
    open_browser(browser_name="Chrome")
    go_to_companyname_homepage(page_url="https://companyname.com")
    find_registration_button_on_login_page(page_url="https://companyname.com/login", button_text="Register")

def open_browser(browser_name):
    actual_result = print_function_name_and_args(open_browser, browser_name)
    assert actual_result == "Open Browser [Chrome]"


def go_to_companyname_homepage(page_url):
    actual_result = print_function_name_and_args(go_to_companyname_homepage, page_url)
    assert actual_result == "Go To Companyname Homepage [https://companyname.com]"


def find_registration_button_on_login_page(page_url, button_text):
    actual_result = print_function_name_and_args(find_registration_button_on_login_page, page_url, button_text)
    assert actual_result == "Find Registration Button On Login Page [https://companyname.com/login, Register]"
