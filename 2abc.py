#1 Проверка пароля
n = int(input("Введите пароль"))
if len(str(n))<8:
    print("Пароль слишком короткий")
else:
    print("Пароль принят")

#2 Проверка связи
status = "online"
if status == "online":
    print("Связь установлена")
else:
    print("Связь потеряна")

#3 Уровень угрозы
n = int(input("Введите уровень угрозы от 1 до 100"))
if n<30 and n>1:
    print("Низкий уровень угрозы")
elif n>31 and n<70:
    print("Средний уровень угрозы")
elif n>71 and n<100:
    print("Высокий уровень угрозы")
else:
    print("Ошибка ввода")

#4 Проверка целостности файла
checksum_original = "123"
checksum_current = "123"
status = "Файл не изменен" if checksum_current==checksum_original else "Файл поврежден"
print(status)

#5 Тип события
event_code = input("Введите тип события(ERR, WRN, INF)")
match event_code:
    case "ERN":
        print("Ошибка системы")
    case "WRN":
        print("Предупреждение")
    case "INF":
        print("Информационное сообщение")
    case _:
        print("Неизвестный код")