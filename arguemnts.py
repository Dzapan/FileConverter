import argparse


def parse_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Konwerter plików JSON, YAML i XML."
    )

    parser.add_argument(
        "-i",
        "--input",
        required=True,
        help="Ścieżka do pliku wejściowego."
    )

    parser.add_argument(
        "-o",
        "--output",
        required=True,
        help="Ścieżka do pliku wynikowego."
    )

    return parser.parse_args()