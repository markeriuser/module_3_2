def send_email(message, recipient, sender="university.help@gmail.com"):
    # Проверка корректности e-mail адреса
    def is_valid_email(email):
        if "@" not in email:
            return False
        at_index = email.index("@")
        local_part = email[:at_index]
        domain_part = email[at_index + 1:]

        if "." not in domain_part:
            return False

        # Проверка на допустимые домены
        valid_domains = [".com", ".ru", ".net"]
        domain_len = len(domain_part)

        for domain in valid_domains:
            if domain_part[domain_len - len(domain):] == domain:
                return True

        return False

    if not (is_valid_email(sender) and is_valid_email(recipient)):
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}.")
    elif sender == recipient:
        print("Нельзя отправить письмо самому себе!")
    elif sender == "university.help@gmail.com":
        print(f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}.")
    else:
        print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.")

send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')
