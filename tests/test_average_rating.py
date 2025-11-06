import pytest

from src.report.average_rating import AverageRatingReport
from src.utils.models import Record


@pytest.fixture
def sample_data():
    return [
        Record(name="Product 1", brand="BrandA", price=100, rating=4.5),
        Record(name="Product 2", brand="BrandA", price=200, rating=4.7),
        Record(name="Product 3", brand="BrandB", price=150, rating=4.0),
    ]


def test_average_rating_report_generates_correct_averages(sample_data):
    """Тест проверяет правильность расчета средних значений в отчете."""
    report = AverageRatingReport()
    output = report.generate(sample_data)

    # Проверяем, что BrandA появляется первым (более высокий средний рейтинг)
    assert "BrandA" in output
    assert output.index("BrandA") < output.index("BrandB")

    # Проверяем правильность средних значений
    assert "4.6" in output  # Среднее для BrandA (4.5 + 4.7) / 2
    assert "4.0" in output  # Среднее для BrandB


def test_average_rating_report_handles_empty_data():
    """Тест проверяет обработку пустых данных."""
    report = AverageRatingReport()
    output = report.generate([])
    assert output == "Нет данных"