import json
def csv_to_records(text: str) -> list[dict]:
    lines = text.strip().split('\n')
    
    if not lines or not lines[0]:
        return []
    
    headers = [h.strip() for h in lines[0].split(',')]
    records = []
    
    for line in lines[1:]:
        if not line.strip():
            continue
        values = [v.strip() for v in line.strip(',')]
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
            if current_key is noy None:
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
        
        