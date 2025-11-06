import argparse
import sys
from typing import List, Type

from rating_analysis.report.average_rating import AverageRatingReport
from rating_analysis.report.base import BaseReport
from rating_analysis.utils.file_reader import read_csv_files


def get_report_class(report_name: str) -> Type[BaseReport]:
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
    if sys.version_info < (3, 8):
        print("Ошибка: Требуется Python версии 3.8 или выше")
        sys.exit(1)


def run(files: List[str], report_name: str):
    """
    Основная логика анализа (для тестирования).
    Разделена от main(), чтобы можно было протестировать.
    """
    try:
        records = read_csv_files(files)
        report_class = get_report_class(report_name)
        report = report_class()
        output = report.generate(records)
        print(output)
        return 0
    except (FileNotFoundError, ValueError) as e:
        print(f"Error: {str(e)}")
        return 1


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
        help="Пути к CSV файлам с данными о рейтингах",
    )
    parser.add_argument("--report", required=True, help="Тип отчета для генерации")
    args = parser.parse_args()
    sys.exit(run(args.files, args.report))


if __name__ == "__main__":
    main()
