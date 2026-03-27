import csv

import pandas as pd
from requests import Response


def verify_status_code(response: Response) -> tuple[bool, str]:
    if response.status_code == 200:
        return True, ""
    elif response.status_code == 404:
        return False, "Сторінку не знайдено"
    else:
        return False, f"Трапилась помилка. Статус помилки: {response.status_code}"


def save_to_csv(filename: str, data: list[dict], fieldnames: list[str]) -> None:
    with open(filename, "w", encoding="utf-8", newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)

def save_to_excel(filename: str, data: list[dict]) -> None:
    df = pd.DataFrame(data)

    df.to_excel(filename, index=False)