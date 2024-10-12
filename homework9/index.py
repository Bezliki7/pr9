import re

pattern = r'([a-zA-Z_][\w\.-]*)@([\w\.-]+\.[\w\.-]+)'

user_input = input("Введите почту: ")

searchedEmail = re.search(pattern, user_input)

if searchedEmail:
    matched = re.match(pattern, searchedEmail.group(0))
    print(f'username: {matched.group(1)}, domain: {matched.group(2)}')
else:
    print("Почта не найдена или введена неправильно")
