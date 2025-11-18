# 🍔 Stellar Burgers UI Tests

Автоматизированные UI-тесты для сервиса Stellar Burgers - космического фастфуда.

### 1. Установка зависимостей
```bash
pip install -r requirements.txt

Запуск тестов
bash
# Все тесты
pytest -v

# Конкретные тесты
pytest tests/test_login.py -v
pytest tests/test_registration.py -v
pytest tests/test_constructor_sections.py -v


Структура проекта
text
Sprint_5/
├── tests/                          # Тесты
│   ├── test_login.py              # Авторизация
│   ├── test_registration.py       # Регистрация
│   ├── test_logout.py             # Выход из системы
│   ├── test_to_personal_account.py # Переход в ЛК
│   ├── test_pers_acc_to_constructor.py # Возврат в конструктор
│   └── test_constructor_sections.py # Разделы конструктора
│
├── conftest.py                    # Фикстуры Pytest
├── locators.py                    # Локаторы элементов
├── data.py                        # Тестовые данные
├── helpers.py                     # Вспомогательные функции
├── urls.py                        # URL-адреса
├── requirements.txt               # Зависимости
└── README.md                      # Документация

🧪 Тестовые сценарии
🔐 Авторизация (test_login.py)
Вход через кнопку "Войти в аккаунт"

Вход через "Личный кабинет"

Вход через форму регистрации

Вход через форму восстановления пароля

📝 Регистрация (test_registration.py)
Успешная регистрация

Ошибки: пустое имя, невалидный email, короткий пароль

Валидные/невалидные пароли

🚪 Выход из системы (test_logout.py)
Выход из личного кабинета

📊 Навигация
Переход в личный кабинет (test_to_personal_account.py)

Возврат в конструктор (test_pers_acc_to_constructor.py)

Переключение разделов конструктора (test_constructor_sections.py)

🛠 Технологии
Python 3.13.5

Selenium WebDriver 4.38.0

pytest 9.0.1

Chrome Driver

⚙️ Настройка
Убедитесь, что установлен Chrome браузер

Файл chromedriver.exe должен быть в корне проекта

Все зависимости указаны в requirements.txt

🎯 Особенности
Явные ожидания (WebDriverWait)

Фикстуры Pytest для управления браузером

Случайные данные для каждого теста

Централизованные локаторы и URL

📞 Поддержка
При возникновении проблем с запуском:

Проверьте версию Chrome и chromedriver

Убедитесь, что все файлы на месте

Запускайте тесты из корневой папки проекта

text

## 🔧 requirements.txt
```txt
selenium==4.35.0
pytest==8.4.1
🚀 Основные команды для вас:
bash
# Из папки Sprint_5 запускайте:
pytest -v                          # Все тесты
pytest tests/test_login.py -v      # Только авторизация
pytest tests/test_registration.py -v # Только регистрация
pytest tests/ -v                   # Все тесты в папке
