@echo off
echo Установка виртуального окружения...
python -m venv venv
call venv\Scripts\activate.bat

echo Установка зависимостей...
pip install -r requirements.txt

echo Установка завершена. Запуск тестов...
pytest

echo.
echo Для запуска анализа используйте команду:
echo python -m src.main --files path/to/your/file.csv --report average-rating
echo.