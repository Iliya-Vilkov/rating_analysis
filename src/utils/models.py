from dataclasses import dataclass
from typing import List

@dataclass
class Record:
    """Класс для хранения информации о записи из CSV файла."""
    name: str  # название продукта
    brand: str  # бренд
    price: float  # цена
    rating: float  # рейтинг