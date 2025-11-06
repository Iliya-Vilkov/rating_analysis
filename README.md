# Инструмент анализа рейтинга брендов

[![CI](https://github.com/Iliya-Vilkov/rating_analysis/actions/workflows/test.yml/badge.svg)](https://github.com/Iliya-Vilkov/rating_analysis/actions/workflows/test.yml)


Инструмент на Python для анализа рейтингов продуктов из CSV файлов и генерации отчетов.

## Быстрая настройка и запуск

Для автоматической установки зависимостей и проверки работоспособности используйте скрипт:

```bash
./setup.sh


## Установка

1. Убедитесь, что у вас установлен Python 3.8 или новее
   ```bash
   python --version  # Должен показать Python 3.8 или выше
   ```
   
   Проект требует Python 3.8+ так как использует:
   - Аннотации типов со стандартными коллекциями (List, Dict и т.д.)
   - Классы данных (dataclasses)
   - f-строки

2. Установите зависимости:

   ```bash
   # Установка основных зависимостей
   pip install -r requirements.txt

## Использование

Скрипт принимает CSV файлы, содержащие данные о рейтингах продуктов, и генерирует отчеты заданного типа.

### Базовое использование:
```bash
python -m src.main --files data1.csv data2.csv --report average-rating
```

### Формат CSV файла

Входные CSV файлы должны содержать следующие столбцы:
- name: Название продукта
- brand: Название бренда
- price: Цена продукта
- rating: Рейтинг продукта

Пример:
```csv
name,brand,price,rating
iphone 15 pro,apple,999,4.9
galaxy s23 ultra,samsung,1199,4.8
redmi note 12,xiaomi,199,4.6
```

## Добавление новых отчетов

Чтобы добавить новый тип отчета:

1. Создайте новый файл в директории `src/report/`
2. Создайте новый класс, наследующийся от `BaseReport`
3. Реализуйте метод `generate`
4. Добавьте новый класс отчета в словарь `reports` в файле `src/main.py`

## Разработка

- Форматирование кода: `black .`
- Сортировка импортов: `isort .`
- Запуск тестов: `pytest`
- Проверка покрытия: `pytest --cov`

## Пример работы

Ниже показан пример запуска скрипта с реальными данными.

### Команда:
```bash
python -m src.main --files examples/data.csv --report average-rating

## Пример работы

### Результат запуска тестов с покрытием

![Тесты и покрытие кода](examples/screenshots/coverage_screenshot.png)

## Запуск через Docker (опционально)

Вы можете запустить приложение в контейнере Docker.

### Сборка образа:
```bash
docker build -t rating-analysis .

### Команда:
```bash
docker run --rm rating-analysis --files examples/data.csv --report average-rating

## Пример работы

### Результат запуска тестов с покрытием

![Тесты и покрытие кода](examples/screenshots/coverage_screenshot_Docker.png)

