def count_by_extension(path: list[str]) -> dict[str, int]:
    counts = {}
    for path in paths:
        filename = path.split('/')[-1]
        
        if '.' in filename:
            rassh = filename.rsplit('.', 1)[1].lower()
        else:
            rassh = ''
            counts[ext] = counts.get(ext, 0) + 1
    
    return counts

def deepest_path(paths: list[str]) -> str:
    if not paths:
        return ''
    return sorted(paths, key=lambda p: (-p.count('/'), p))[0]

def human_size(n_butes: int) -> str:
    if n_butes < 1024:
        return f'{n_butes} Б'
    
    units = ['КБ', 'МБ', 'ГБ', 'ТБ']
    size = float(n_butes)
    
    for unit in units:
        size /= 1024.0
        if size < 1024 or unit == units[-1]:
            return f'{size.1f} {unit}'