# tests/test_main.py
from unittest.mock import patch, Mock
from src.main import run


@patch("src.main.read_csv_files")
@patch("src.main.get_report_class")
def test_run_success(mock_get_report_class, mock_read_files, capsys):
    """Тест успешной генерации отчёта."""
    # Подготовка данных
    mock_read_files.return_value = [
        Mock(name="Product 1", brand="BrandA", price=100, rating=4.5)
    ]

    # Мок экземпляра отчёта
    mock_report_instance = Mock()
    mock_report_instance.generate.return_value = "Brand      Average Rating\nBrandA                4.5"

    # Мок класса отчёта (вызываемый объект, возвращающий экземпляр)
    mock_report_class = Mock()
    mock_report_class.return_value = mock_report_instance

    # get_report_class() возвращает "класс" (вызываемый мок)
    mock_get_report_class.return_value = mock_report_class

    # Вызов тестируемой функции
    exit_code = run(files=["data.csv"], report_name="average-rating")

    # Проверки
    assert exit_code == 0
    captured = capsys.readouterr()
    assert "BrandA" in captured.out
    assert "4.5" in captured.out


@patch("src.main.read_csv_files")
def test_run_file_not_found(mock_read_files, capsys):
    """Тест обработки отсутствующего файла."""
    mock_read_files.side_effect = FileNotFoundError("data.csv")
    exit_code = run(files=["data.csv"], report_name="average-rating")
    assert exit_code == 1
    captured = capsys.readouterr()
    assert "Error: data.csv" in captured.out


@patch("src.main.read_csv_files")
@patch("src.main.get_report_class")
def test_run_unsupported_report(mock_get_report_class,
                                mock_read_files,
                                capsys):
    """Тест обработки неподдерживаемого типа отчёта."""
    mock_read_files.return_value = []  # Не падаем при чтении
    mock_get_report_class.side_effect = ValueError("Неподдерживаемый тип "
                                                   "отчета")

    exit_code = run(files=["data.csv"], report_name="unknown")
    assert exit_code == 1
    captured = capsys.readouterr()
    assert "Error: Неподдерживаемый тип отчета" in captured.out
