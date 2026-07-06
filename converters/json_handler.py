import json
from pathlib import Path
from typing import Any


def load_json(file_path: Path) -> Any:
    try:
        with file_path.open("r", encoding="utf-8") as file:
            return json.load(file)

    except FileNotFoundError as error:
        raise ValueError(
            f"Nie znaleziono pliku: {file_path}"
        ) from error

    except PermissionError as error:
        raise ValueError(
            f"Brak dostępu do pliku: {file_path}"
        ) from error

    except json.JSONDecodeError as error:
        raise ValueError(
            f"Niepoprawny JSON. "
            f"Linia {error.lineno}, "
            f"kolumna {error.colno}: "
            f"{error.msg}"
        ) from error


def save_json(data: Any, file_path: Path) -> None:
    try:
        with file_path.open("w", encoding="utf-8") as file:
            json.dump(
                data,
                file,
                ensure_ascii=False,
                indent=4
            )

    except PermissionError as error:
        raise ValueError(
            f"Brak uprawnień do zapisu: {file_path}"
        ) from error

    except OSError as error:
        raise ValueError(
            f"Nie udało się zapisać pliku: {error}"
        ) from error