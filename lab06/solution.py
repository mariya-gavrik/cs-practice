def count_by_extension(path: list[str]) -> dict[str, int]:
    counts = {}
    for path in paths:
        filename = path.split('/')[-1]
        
        if '.' in filename:
            rassh = filename.rsplit('.', 1)[1].lower():
        else:
            rassh = ''
            counts[ext] = counts.get(ext, 0) + 1
    
    return counts