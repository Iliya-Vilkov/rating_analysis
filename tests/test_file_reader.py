import pytest
from pathlib import Path

from src.utils.file_reader import read_csv_files
from src.utils.models import Record


def test_read_csv_files_reads_valid_file(tmp_path):
    # Create a temporary CSV file
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
    # Create two temporary CSV files
    csv1_content = "name,brand,price,rating\nProduct1,BrandA,100,4.5"
    csv2_content = "name,brand,price,rating\nProduct2,BrandB,200,4.7"
    
    csv1_file = tmp_path / "test1.csv"
    csv2_file = tmp_path / "test2.csv"
    
    csv1_file.write_text(csv1_content)
    csv2_file.write_text(csv2_content)

    records = read_csv_files([str(csv1_file), str(csv2_file)])
    assert len(records) == 2


def test_read_csv_files_raises_on_missing_file():
    with pytest.raises(FileNotFoundError):
        read_csv_files(["nonexistent.csv"])


def test_read_csv_files_raises_on_invalid_format(tmp_path):
    # Create a CSV file with invalid format
    csv_content = "name,brand\nProduct1,BrandA"  # Missing required columns
    csv_file = tmp_path / "invalid.csv"
    csv_file.write_text(csv_content)

    with pytest.raises(ValueError):
        read_csv_files([str(csv_file)])