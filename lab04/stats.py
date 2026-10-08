def parse_record(line: str) -> dict:
    parts = line.split(';')

    if len(parts) != 3:
        raise ValueError(f"Ожидалось 3 поля, получено {len(parts)}")
    city = parts[0].strip()
    temp_str = parts[1].strip()
    date = parts[2].strip()
    if not city or not date:
        raise ValueError("Город или дата не могут быть пустыми")
    try:
        temp = float(temp_str)
    except ValueError:
        raise ValueError(f"Температура '{temp_str}' не является числом")

    return {
        "city": city,
        "temperature": temp,
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


def average_by_city(records: list[dict]) -> dict:
    city_totals = {}
    city_counts = {}

    for rec in records:
        city = rec["city"]
        temp = rec["temperature"]

        city_totals[city] = city_totals.get(city, 0.0) + temp
        city_counts[city] = city_counts.get(city, 0) + 1

    averages = {}
    for city in city_totals:
        avg = city_totals[city] / city_counts[city]
        averages[city] = round(avg, 1)

    return averages


def warmest_city(records: list[dict]) -> str:
    if not records:
        return ""

    averages = average_by_city(records)

    if not averages:
        return ""

    sorted_cities = sorted(averages.keys(), key=lambda c: (-averages[c], c))

    return sorted_cities[0]