import json
def csv_to_records(text: str) -> list[dict]:
    if not text.strip():
        return []
    lines = text.strip().split('\n')
    
    if not lines or not lines[0]:
        return []
    
    headers = [h.strip() for h in lines[0].split(',')]
    records = []
    
    for line in lines[1:]:
        if not line.strip():
            continue
        values = [v.strip() for v in line.split(',')]
        record = dict(zip(headers, values))
        records.append(record)
    return records

def parse_settings(lines: list[str]) -> dict:
    result = {}
    current_key = None
    
    for line in lines:
        line = line.split('#')[0].strip()
        if not line:
            continue
        
        if line.startswith('- '):
            if current_key is not None:
                if not isintance(result[current_key], list):
                    result[current_key] = []
                    val_str = line[2:].strip()
                    result[current_key].append(_convert_type(val_str))
                    continue
                    
        if ':' in line:
            key, val = line.split(':', 1)
            key = key.strip()
            val = val.strip()
            if val == '':
                current_key = key
                result[key] = []
            else:
                result[key] = _convert_type(val)
                current_key = None
        
        return result
    
def _convert_type(val: str):
    val_lower = val.lower()
    if val_lower in ('true', 'yes'):
        return True
    if val_lower in ('false', 'no'):
        return False
    
    try:
        return int(val)
    except ValueError:
        pass
    
    try:
        return float(val.replace(',', '.'))
    except ValueError:
        pass
    
    return val

def merge_by_key(rows: list[dict], extra: dict, key: str = 'id') -> list[dict]:
    merged_rows = []
    for row in rows:
        new_row = row.copy()
        key_val = str(new_row.get(key))
        if key_val in extra:
            merged_data = {**extra[key_val], **new_row}
            merged_rows.append(merged_data)
        else:
            merged_rows.append(new_row)
        
        return merged_rows

def records_to_json(records: list[dict]) -> str:
    return json.dumps(
        records,
        ensure_ascii = False,
        indent = 2,
        sort_keys = True
    )
    
        
        