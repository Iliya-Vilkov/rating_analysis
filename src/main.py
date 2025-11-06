import argparse
from typing import List, Type

from src.report.average_rating import AverageRatingReport
from src.report.base import BaseReport
from src.utils.file_reader import read_csv_files


def get_report_class(report_name: str) -> Type[BaseReport]:
    """Получение класса отчета по его имени.

    Аргументы:
        report_name: Название отчета для генерации

    Возвращает:
        Type[BaseReport]: Класс отчета для использования

    Вызывает:
        ValueError: Если тип отчета не поддерживается
    """
    reports = {
        "average-rating": AverageRatingReport,
    }

    if report_name not in reports:
        raise ValueError(
            f"Неподдерживаемый тип отчета: {report_name}. "
            f"Доступные отчеты: {', '.join(reports.keys())}"
        )

    return reports[report_name]


def check_python_version():
    """Проверка соответствия версии Python требованиям."""
    import sys
    if sys.version_info < (3, 8):
        print("Ошибка: Требуется Python версии 3.8 или выше")
        sys.exit(1)


def main():
    """Основная точка входа в скрипт."""
    check_python_version()
    parser = argparse.ArgumentParser(
        description="Генерация отчетов на основе данных о рейтингах продуктов"
    )
    parser.add_argument(
        "--files",
        nargs="+",
        required=True,
        help="Пути к CSV файлам с данными о рейтингах"
    )
    parser.add_argument(
        "--report",
        required=True,
        help="Тип отчета для генерации"
    )

    args = parser.parse_args()

    try:
        # Read data from files
        records = read_csv_files(args.files)

        # Get appropriate report class and generate report
        report_class = get_report_class(args.report)
        report = report_class()
        output = report.generate(records)

        # Print report
        print(output)

    except (FileNotFoundError, ValueError) as e:
        print(f"Error: {str(e)}")
        exit(1)


if __name__ == "__main__":
    main()