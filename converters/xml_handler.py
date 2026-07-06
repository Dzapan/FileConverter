from pathlib import Path
from typing import Any
import xml.etree.ElementTree as ET


def element_to_object(element: ET.Element) -> Any:
    children = list(element)

    if not children:
        if element.text is None:
            return ""

        return element.text.strip()

    result = {}

    for child in children:
        value = element_to_object(child)

        if child.tag in result:
            if not isinstance(result[child.tag], list):
                result[child.tag] = [result[child.tag]]

            result[child.tag].append(value)
        else:
            result[child.tag] = value

    return result


def load_xml(file_path: Path) -> dict[str, Any]:
    try:
        tree = ET.parse(file_path)
        root = tree.getroot()

        return {
            root.tag: element_to_object(root)
        }

    except FileNotFoundError as error:
        raise ValueError(
            f"Nie znaleziono pliku: {file_path}"
        ) from error

    except PermissionError as error:
        raise ValueError(
            f"Brak dostępu do pliku: {file_path}"
        ) from error

    except ET.ParseError as error:
        raise ValueError(
            f"Niepoprawna składnia XML: {error}"
        ) from error


def object_to_element(
    parent: ET.Element,
    key: str,
    value: Any
) -> None:
    if isinstance(value, dict):
        element = ET.SubElement(parent, key)

        for child_key, child_value in value.items():
            object_to_element(
                element,
                str(child_key),
                child_value
            )

    elif isinstance(value, list):
        for item in value:
            object_to_element(parent, key, item)

    else:
        element = ET.SubElement(parent, key)
        element.text = "" if value is None else str(value)


def save_xml(data: Any, file_path: Path) -> None:
    try:
        if isinstance(data, dict) and len(data) == 1:
            root_name, root_data = next(iter(data.items()))
            root = ET.Element(str(root_name))

            if isinstance(root_data, dict):
                for key, value in root_data.items():
                    object_to_element(
                        root,
                        str(key),
                        value
                    )
            else:
                root.text = str(root_data)

        else:
            root = ET.Element("root")

            if isinstance(data, dict):
                for key, value in data.items():
                    object_to_element(
                        root,
                        str(key),
                        value
                    )
            else:
                object_to_element(root, "item", data)

        tree = ET.ElementTree(root)
        ET.indent(tree, space="    ")

        tree.write(
            file_path,
            encoding="utf-8",
            xml_declaration=True
        )

    except PermissionError as error:
        raise ValueError(
            f"Brak uprawnień do zapisu: {file_path}"
        ) from error

    except OSError as error:
        raise ValueError(
            f"Nie udało się zapisać XML: {error}"
        ) from error