from pathlib import Path

from arguments import parse_arguments
from converters.json_handler import load_json, save_json


def main() -> None:
    arguments = parse_arguments()

    try:
        data = load_json(Path(arguments.input))

        save_json(
            data,
            Path(arguments.output)
        )

        print(f"Zapisano plik: {arguments.output}")

    except ValueError as error:
        print(f"Błąd: {error}")


if __name__ == "__main__":
    main()