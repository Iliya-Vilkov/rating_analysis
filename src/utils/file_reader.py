import csv
from pathlib import Path
from typing import List

from src.utils.models import Record


def read_csv_files(file_paths: List[str]) -> List[Record]:
    """Чтение и парсинг CSV файлов в объекты Record.

    Аргументы:
        file_paths: Список путей к CSV файлам

    Возвращает:
        List[Record]: Список обработанных записей из всех файлов

    Вызывает:
        FileNotFoundError: Если какой-либо файл не существует
        ValueError: Если формат CSV файла некорректен
    """
    records = []

    for file_path in file_paths:
        path = Path(file_path)
        if not path.exists():
            raise FileNotFoundError(f"File not found: {file_path}")

        with path.open("r", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            try:
                for row in reader:
                    record = Record(
                        name=row["name"],
                        brand=row["brand"],
                        price=float(row["price"]),
                        rating=float(row["rating"])
                    )
                    records.append(record)
            except (KeyError, ValueError) as e:
                raise ValueError(
                    f"Неверный формат CSV в файле {file_path}: {str(e)}"
                )

    return records
