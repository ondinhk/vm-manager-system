import csv


def check_duplicate_ips(csv_file):
    ip_set = set()
    duplicate_ips = set()
    with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            ip = row[0].strip()
            if ip in ip_set:
                duplicate_ips.add(ip)
            else:
                ip_set.add(ip)
    return duplicate_ips


csv_file_path = 'output.csv'
duplicates = check_duplicate_ips(csv_file_path)
if duplicates:
    print(f'Duplicate IP addresses found: {duplicates}')
else:
    print('No duplicate IP addresses found.')
