from collections import defaultdict
from typing import List

from tabulate import tabulate

from src.report.base import BaseReport
from src.utils.models import Record


class AverageRatingReport(BaseReport):
    """Отчет, показывающий средний рейтинг по брендам."""

    def generate(self, data: List[Record]) -> str:
        """Генерация отчета со средними рейтингами по брендам.

        Аргументы:
            data: Список объектов Record для анализа

        Возвращает:
            str: Отформатированная строка отчета со средними рейтингами брендов
        """
        if not data:
            return "Нет данных"

        # Calculate average ratings
        brand_ratings = defaultdict(list)
        for record in data:
            brand_ratings[record.brand].append(record.rating)

        # Calculate averages and sort
        report_data = [
            (brand, sum(ratings) / len(ratings))
            for brand, ratings in brand_ratings.items()
        ]
        report_data.sort(key=lambda x: x[1], reverse=True)

        # Format table
        headers = ["Brand", "Average Rating"]
        return tabulate(report_data, headers=headers, tablefmt="simple")