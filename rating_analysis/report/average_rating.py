from collections import defaultdict
from typing import List

from tabulate import tabulate

from rating_analysis.report.base import BaseReport
from rating_analysis.utils.models import Record


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

        # Расчёт средних и форматирование в одну строку
        formatted_data = [
            (brand, f"{sum(ratings) / len(ratings):.1f}")
            for brand, ratings in brand_ratings.items()
        ]
        formatted_data.sort(key=lambda x: float(x[1]), reverse=True)

        # Добавляем нумерацию
        numbered_data = [
            (idx + 1, brand, rating)
            for idx, (brand, rating) in enumerate(formatted_data)
        ]

        headers = ["#", "Brand", "Average Rating"]
        return tabulate(
            numbered_data,
            headers=headers,
            tablefmt="grid",
            disable_numparse=True,
        )
