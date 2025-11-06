from abc import ABC, abstractmethod
from typing import List

from rating_analysis.utils.models import Record


class BaseReport(ABC):
    """Базовый класс для всех отчетов."""

    @abstractmethod
    def generate(self, data: List[Record]) -> str:
        """Генерация отчета на основе данных.

        Аргументы:
            data: Список объектов Record для анализа

        Возвращает:
            str: Отформатированную строку отчета
        """
        pass
