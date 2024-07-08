himport requests
from colorama import Fore, Style, init

init(autoreset=True)

# Nombre del archivo que contiene la lista de dominios
filename = 'Dominios_A_Chequear.txt'

# Encabezado malicioso
malicious_host = 'evil.com'

def check_host_header_injection(url):
    headers = {
        'Host': malicious_host
    }
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 502:
            print(f'{Fore.RED}{url} - Bad Gateway. The backend server is not responding.')
        elif malicious_host in response.text:
            print(f'{Fore.BLUE}{url} - Possible Host Header Injection Detected')
        else:
            print(f'{url} - No Host Header Injection Detected')
    except requests.exceptions.RequestException as e:
        print(f'An error occurred with {url}: {e}')

def read_domains_from_file(filename):
    try:
        with open(filename, 'r') as file:
            domains = [line.strip() for line in file.readlines()]
        return domains
    except FileNotFoundError:
        print(f'File {filename} not found')
        return []

domains = read_domains_from_file(filename)
for domain in domains:
    check_host_header_injection(domain)
