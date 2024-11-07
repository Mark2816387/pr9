import re

def parse_email(email):
    pattern = r'^([a-zA-Z0-9_.+-]+)@([a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)$'
    
    match = re.match(pattern, email)
    if match:
        username = match.group(1)
        domain = match.group(2)
        return f"Username: {username}\nDomain: {domain}"
    else:
        return "Ошибка: Некорректный формат email"

email = input("Введите email: ")
print(parse_email(email))
