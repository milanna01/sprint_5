# 🍔 Stellar Burgers - UI Autotests

Автоматизированные UI-тесты для веб-приложения Stellar Burgers с использованием Selenium и Pytest.

## 📋 Описание проекта

Проект представляет собой набор автоматизированных тестов для проверки функциональности сервиса Stellar Burgers. Тесты охватывают основные пользовательские сценарии: регистрацию, авторизацию, навигацию и работу с конструктором бургеров.

**Технологии:** Python 3.13.5, Selenium WebDriver 4.38.0, Pytest 9.0.1  
**Тестируемое приложение:** https://stellarburgers.nomoreparties.site/

## ⚙️ Установка проекта

### 1. Установка зависимостей
```bash
pip install -r requirements.txt
2. Проверка окружения
Убедитесь, что установлен Google Chrome

Файл chromedriver.exe должен находиться в корне проекта

Python 3.13.5

🚀 Запуск проекта
Запуск всех тестов
bash
pytest -v
Запуск отдельных тестовых модулей
bash
# Тесты авторизации
pytest tests/test_login.py -v

# Тесты регистрации
pytest tests/test_registration.py -v

# Тесты навигации
pytest tests/test_constructor_sections.py -v

# Тесты личного кабинета
pytest tests/test_to_personal_account.py -v
Запуск с отчетом
bash
pytest -v --html=report.html
📁 Структура проекта
text
Sprint_5/
├── tests/                          # Директория с тестами
│   ├── test_login.py               # Тесты авторизации
│   ├── test_registration.py        # Тесты регистрации
│   ├── test_logout.py              # Тесты выхода из системы
│   ├── test_to_personal_account.py # Тесты перехода в ЛК
│   ├── test_pers_acc_to_constructor.py # Тесты возврата в конструктор
│   └── test_constructor_sections.py # Тесты разделов конструктора
│
├── conftest.py                     # Фикстуры Pytest
├── locators.py                     # Локаторы элементов
├── data.py                         # Тестовые данные
├── helpers.py                      # Вспомогательные функции
├── urls.py                         # URL-адреса
├── chromedriver.exe                # Драйвер браузера
├── requirements.txt                # Зависимости
└── README.md                       # Документация
🧪 Покрытие тестами
✅ Авторизация - 4 способа входа в систему

✅ Регистрация - успешная и негативные сценарии

✅ Личный кабинет - переход и навигация

✅ Конструктор - переключение между разделами

✅ Выход из системы - корректное завершение сессии

🛠 Технические характеристики
Python: 3.13.5

Selenium WebDriver: 4.38.0

Pytest: 9.0.1

Chrome Driver: совместимая версия

📞 Поддержка
При возникновении проблем:

Проверьте совместимость версий Chrome и chromedriver

Убедитесь, что все файлы находятся в правильных директориях

Запускайте тесты из корневой папки проекта

text

## 🔧 requirements.txt (обновленный)
```txt
selenium==4.38.0
pytest==9.0.1
