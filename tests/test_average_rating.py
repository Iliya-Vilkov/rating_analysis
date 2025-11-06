import pytest
from src.report.average_rating import AverageRatingReport
from src.utils.models import Record


@pytest.fixture
def sample_data():
    """
    Возвращает тестовые данные с тремя продуктами:
    - Два от BrandA с рейтингами 4.5 и 4.7
    - Один от BrandB с рейтингом 4.0
    """
    return [
        Record(name="Product 1", brand="BrandA", price=100, rating=4.5),
        Record(name="Product 2", brand="BrandA", price=200, rating=4.7),
        Record(name="Product 3", brand="BrandB", price=150, rating=4.0),
    ]


def test_average_rating_report_generates_correct_averages(sample_data):
    """
    Тест проверяет:
    - Средний рейтинг для BrandA = 4.6
    - Средний рейтинг для BrandB = 4.0
    - BrandA отображается раньше BrandB (сортировка по убыванию)
    """
    report = AverageRatingReport()
    output = report.generate(sample_data)

    assert "BrandA" in output
    assert output.index("BrandA") < output.index("BrandB")
    assert "4.6" in output
    assert "4.0" in output


def test_average_rating_report_handles_empty_data():
    """
    Тест проверяет, что при пустом списке данных
    отчёт возвращает строку "Нет данных".
    """
    report = AverageRatingReport()
    output = report.generate([])
    assert output == "Нет данных"
