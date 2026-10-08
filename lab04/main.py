import sys
from stats import read_valid, average_by_city, warmest_city


def main():
    input_data = sys.stdin.read()
    lines = input_data.splitlines()

    valid_records = read_valid(lines)

    total_lines = len(lines)
    valid_count = len(valid_records)
    skipped_count = total_lines - valid_count
    print(valid_count)
    
    print(skipped_count)

    if valid_records:
        best_city = warmest_city(valid_records)
        averages = average_by_city(valid_records)
        print(averages[best_city])
    else:
        print(0.0)

if __name__ == "__main__":
    main()