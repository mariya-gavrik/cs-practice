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
