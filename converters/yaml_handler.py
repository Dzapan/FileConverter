from pathlib import Path
from typing import Any

import yaml


def load_yaml(file_path: Path) -> Any:
    try:
        with file_path.open("r", encoding="utf-8") as file:
            return yaml.safe_load(file)

    except FileNotFoundError as error:
        raise ValueError(
            f"Nie znaleziono pliku: {file_path}"
        ) from error

    except PermissionError as error:
        raise ValueError(
            f"Brak dostępu do pliku: {file_path}"
        ) from error

    except yaml.YAMLError as error:
        raise ValueError(
            f"Niepoprawna składnia YAML: {error}"
        ) from error


def save_yaml(data: Any, file_path: Path) -> None:
    try:
        with file_path.open("w", encoding="utf-8") as file:
            yaml.safe_dump(
                data,
                file,
                allow_unicode=True,
                sort_keys=False
            )

    except PermissionError as error:
        raise ValueError(
            f"Brak uprawnień do zapisu: {file_path}"
        ) from error

    except yaml.YAMLError as error:
        raise ValueError(
            f"Nie udało się zapisać YAML: {error}"
        ) from error