from unittest.mock import Mock, patch

from src.main import run


@patch("src.main.read_csv_files")
@patch("src.main.get_report_class")
def test_run_success(mock_get_report_class, mock_read_files, capsys):
    """
    Тест проверяет успешную генерацию отчёта.
    Проверяет:
    - Код возврата равен 0
    - Вывод содержит бренд и значение рейтинга
    """
    mock_read_files.return_value = [
        Mock(name="Product 1", brand="BrandA", price=100, rating=4.5)
    ]

    mock_report_instance = Mock()
    mock_report_instance.generate.return_value = (
        "Brand      Average Rating\n" "BrandA                4.5"
    )

    mock_report_class = Mock()
    mock_report_class.return_value = mock_report_instance

    mock_get_report_class.return_value = mock_report_class

    exit_code = run(files=["data.csv"], report_name="average-rating")

    assert exit_code == 0
    captured = capsys.readouterr()
    assert "BrandA" in captured.out
    assert "4.5" in captured.out


@patch("src.main.read_csv_files")
def test_run_file_not_found(mock_read_files, capsys):
    """
    Тест проверяет обработку ситуации, когда файл не найден.
    Ожидается:
    - Код возврата 1
    - Сообщение об ошибке в выводе
    """
    mock_read_files.side_effect = FileNotFoundError("data.csv")

    exit_code = run(files=["data.csv"], report_name="average-rating")

    assert exit_code == 1
    captured = capsys.readouterr()
    assert "Error: data.csv" in captured.out


@patch("src.main.read_csv_files")
@patch("src.main.get_report_class")
def test_run_unsupported_report(mock_get_report_class, mock_read_files, capsys):
    """
    Тест проверяет обработку запроса на несуществующий тип отчёта.
    Ожидается:
    - Код возврата 1
    - Сообщение об ошибке в выводе
    """
    mock_read_files.return_value = []
    mock_get_report_class.side_effect = ValueError("Неподдерживаемый тип отчета")

    exit_code = run(files=["data.csv"], report_name="unknown")

    assert exit_code == 1
    captured = capsys.readouterr()
    assert "Error: Неподдерживаемый тип отчета" in captured.out
