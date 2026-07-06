import sys
from pathlib import Path
from typing import Any

from arguments import parse_arguments
from converters.json_handler import load_json, save_json
from converters.yaml_handler import load_yaml, save_yaml
from converters.xml_handler import load_xml, save_xml


def load_data(file_path: Path) -> Any:
    extension = file_path.suffix.lower()

    if extension == ".json":
        return load_json(file_path)

    if extension in (".yml", ".yaml"):
        return load_yaml(file_path)

    if extension == ".xml":
        return load_xml(file_path)

    raise ValueError(
        f"Nieobsługiwany format wejściowy: "
        f"{extension or 'brak rozszerzenia'}"
    )


def save_data(data: Any, file_path: Path) -> None:
    extension = file_path.suffix.lower()

    if extension == ".json":
        save_json(data, file_path)
        return

    if extension in (".yml", ".yaml"):
        save_yaml(data, file_path)
        return

    if extension == ".xml":
        save_xml(data, file_path)
        return

    raise ValueError(
        f"Nieobsługiwany format wyjściowy: "
        f"{extension or 'brak rozszerzenia'}"
    )


def main() -> int:
    arguments = parse_arguments()

    input_path = Path(arguments.input)
    output_path = Path(arguments.output)

    try:
        if input_path.resolve() == output_path.resolve():
            raise ValueError(
                "Plik wejściowy i wynikowy nie mogą być tym samym plikiem."
            )

        data = load_data(input_path)

        output_path.parent.mkdir(
            parents=True,
            exist_ok=True
        )

        save_data(data, output_path)

        print(f"Poprawnie zapisano plik: {output_path}")
        return 0

    except ValueError as error:
        print(f"Błąd: {error}", file=sys.stderr)
        return 1

    except KeyboardInterrupt:
        print(
            "\nOperacja została przerwana przez użytkownika.",
            file=sys.stderr
        )
        return 130

    except Exception as error:
        print(
            f"Nieoczekiwany błąd: {error}",
            file=sys.stderr
        )
        return 1


if __name__ == "__main__":
    raise SystemExit(main())