import pytest

from src.utils.file_reader import read_csv_files
from src.utils.models import Record


def test_read_csv_files_reads_valid_file(tmp_path):
    """
    Тест проверяет, что функция корректно читает один валидный CSV-файл.
    Проверяет:
    - Длина списка записей равна 1
    - Элемент — экземпляр Record
    - Поля заполнены правильно
    """
    csv_content = "name,brand,price,rating\nProduct1,BrandA,100,4.5"
    csv_file = tmp_path / "test.csv"
    csv_file.write_text(csv_content)

    records = read_csv_files([str(csv_file)])

    assert len(records) == 1
    assert isinstance(records[0], Record)
    assert records[0].name == "Product1"
    assert records[0].brand == "BrandA"
    assert records[0].price == 100.0
    assert records[0].rating == 4.5


def test_read_csv_files_handles_multiple_files(tmp_path):
    """
    Тест проверяет чтение нескольких CSV-файлов.
    Ожидается, что все записи из всех файлов будут объединены в один список.
    """
    csv1_content = "name,brand,price,rating\nProduct1,BrandA,100,4.5"
    csv2_content = "name,brand,price,rating\nProduct2,BrandB,200,4.7"

    csv1_file = tmp_path / "test1.csv"
    csv2_file = tmp_path / "test2.csv"

    csv1_file.write_text(csv1_content)
    csv2_file.write_text(csv2_content)

    records = read_csv_files([str(csv1_file), str(csv2_file)])

    assert len(records) == 2


def test_read_csv_files_raises_on_missing_file():
    """
    Тест проверяет, что при передаче несуществующего файла
    возбуждается исключение FileNotFoundError.
    """
    with pytest.raises(FileNotFoundError):
        read_csv_files(["nonexistent.csv"])


def test_read_csv_files_raises_on_invalid_format(tmp_path):
    """
    Тест проверяет обработку CSV-файла с некорректным форматом
    (отсутствуют обязательные столбцы price и rating).
    Ожидается возбуждение ValueError.
    """
    csv_content = "name,brand\nProduct1,BrandA"
    csv_file = tmp_path / "invalid.csv"
    csv_file.write_text(csv_content)

    with pytest.raises(ValueError):
        read_csv_files([str(csv_file)])
