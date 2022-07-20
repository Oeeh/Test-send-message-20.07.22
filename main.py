import smtplib

# ввод данных почты в почте
def send_email(message):
    sender = "yura1c@mail.ru"
    password = "aw!^u!(fak"

    # Передаю пораметры сервера почты и порт почты
    server = smtplib.SMTP("smtp.mail.ru", 465)
    # Запуск шифрованного обмена по ТЛС
    server.starttls()

    # авторизовываемся в почте 
    try:
        # Логин и пароль переменных
        server.login(sender, password)
        # Отправка "Отправитель","Получатель", "Переменную с сообщением", можно добавить файл со списком почт для отправки(рассылки)
        server.sendmail(sender, sender, message)

        # Ответ что ошибок нет и сообщение доставленно!
        return "The message was sent successfully!"
    # Обрабатываем ошибки и завершать работу функции с принтом об ошибке
    except Exception as _ex:
        return f"{_ex}\nCheck your login or password please!"







def main():
    # текст с сообщением или другое сюда
    message = input("Type your message: ")
    print(send_email(message=message))



    if __name__ == "__main__":
        main()
