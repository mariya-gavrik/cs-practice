def parse_event(line: str) -> dict:
    line = line.strip()
    if not line:
        raise ValueError('Пустая строка')
    parts = line.split(maxsplit = 2)
    
    if len(parts) < 3:
        raise ValueError('Частей в строке меньше 3')
    time = parts[0].strip()
    level = parts[1].strip()
    message = parts[2].strip()
    valid_levels = {'DEBUG', 'INFO', 'WARNING', 'ERROR'}
    if level not in valid_levels:
        raise ValueError('Неизвестный уровень:', f'{level}')
    
    return {
        'time': time,
        'level': level
        'message': message
    }

def count_levels(lines: list[str]) -> dict:
    counts = {}
    for line in lines:
        if not line.strip():
            continue
        try:
            event = parse_event(line)
            level = event['level']
            counts[level] = counts.get(level, 0) + 1
        except ValueError:
            counts['BROKEN'] = counts.get('BROKEN', 0) + 1

    return counts


def top_errors(lines: list[str], n: int) -> list[list]:
    error_counts = {}
    for line in lines:
        if not line.strip():
            continue

        try:
            event = parse_event(line)
            if event['level'] == 'ERROR':
                msg = event['message']
                error_counts[msg] = error_counts.get(msg, 0) + 1
        except ValueError:
            continue
    sorted_errors = sorted(error_counts.keys(), key=lambda c: (-c[1], c[0]))
    return [[msg, count] for msg, count in sorted_errors[:n]]


def format_report(counts: dict, errors: list[list]) -> str:
    report_lines = ['Отчет по журналу', '']
    all_levels = sorted(list(counts.keys()))
    for level in all_levels:
        report_lines.append(f'{level}:{counts[level]}')
    report_lines.append('')
    report_lines.append('Частые ошибки:')

    if not errors:
        report_lines.append('Нет ошибок')
    else:
        for msg, count in errors:
            report_lines.append(f'{msg} - {count}')

    return '\n'.join(report_lines) + '\n'