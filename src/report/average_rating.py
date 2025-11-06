from collections import defaultdict
from typing import List

from tabulate import tabulate

from src.report.base import BaseReport
from src.utils.models import Record


class AverageRatingReport(BaseReport):
    """Отчет, показывающий средний рейтинг по брендам."""

    def generate(self, data: List[Record]) -> str:
        """Генерация отчета со средними рейтингами по брендам."""
        if not data:
            return "Нет данных"

        # Сбор данных по брендам
        brand_ratings = defaultdict(list)
        for record in data:
            brand_ratings[record.brand].append(record.rating)

        # Расчёт средних (как числа для сортировки)
        report_data = [
            (brand, sum(ratings) / len(ratings))
            for brand, ratings in brand_ratings.items()
        ]
        report_data.sort(key=lambda x: x[1], reverse=True)

        # Форматируем средние в строки с одним знаком после запятой
        formatted_data = [
            (brand, f"{avg:.1f}")  # ← Вот ключ: превращаем в строку "4.0"
            for brand, avg in report_data
        ]

        headers = ["Brand", "Average Rating"]
        return tabulate(formatted_data, headers=headers, tablefmt="simple",
                        disable_numparse=True)
