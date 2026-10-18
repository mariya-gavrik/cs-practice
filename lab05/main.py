import logstats

def main():
    path = input().strip()
    total_parsed = 0
    error_count = 0
    broken_count = 0
    counts = {}
    
    try:
        with open(path, encoding = 'utf-8') as log:
            for line in log:
                if not line.strip():
                    continue
                try:
                    event = logstats.parse_event(line)
                    level = event['level']
                    counts[level] = counts.get(level, 0) + 1
                    total_parsed += 1
                    
                    if level == 'ERROR':
                        error_count += 1
                except ValueError:
                    counts['BROKEN'] = counts.get('BROKEN', 0) + 1
                    broken_count += 1
                    total_parsed += 1
        
        print(total_parsed)
        print(error_count)
        print(broken_count)
        
        with open(path, encoding = 'utf-8') as log:
            errors = logstats.top_errors(log, 3)
        report_text = logstats.format_report(counts, errors)
        with open('report.txt', 'w', encoding = 'utf-8') as f:
            f.write(report_text)
    except FileNotFoundError:
        print(f'Файл {path} не найден')

if __name__ == '__main__':
    main()
        