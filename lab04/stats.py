def parse_record(line: str) -> dict:
    parts = line.split(';')

    if len(parts) != 3:
        raise ValueError(f"Ожидалось 3 поля, получено {len(parts)}")
    city, temp_str, date = parts
    if not city or not date:
        raise ValueError("Город или дата не могут быть пустыми")
    try:
        temp = float(temp_str)
    except ValueError:
        raise ValueError(f"Температура '{temp_str}' не является числом")

    return {
        "city": city,
        "temp": temp,
        "date": date
    }

def read_valid(lines: list[str]) -> list[dict]:
    valid_records = []
    for line in lines:
        if not line.strip():
            continue
            
        try:
            record = parse_record(line)
            valid_records.append(record)
        except ValueError:
            continue

    return valid_records