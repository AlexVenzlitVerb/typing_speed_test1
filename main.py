import time

print("Это программа, которая замеряет скорость печати.")
print("Вам будет показана случайная фраза, которую вам предстоит напечатать самостоятельно. Готовы?")
input("Нажмите Enter, если готовы:")

phrase1 = "В чащах юга жил бы цитрус? Да, но фальшивый экземпляр!"
phrase2 = "Широкая электрификация южных губерний даст мощный толчок подъёму сельского хозяйства."
phrase3 = "Съешь ещё этих мягких французских булок да выпей же чаю."

import random
phrases = random.choice([phrase1, phrase2, phrase3])
print(phrases)
start_time = int(time.time())

user_input = input("Напечатайте фразу выше: ")
end_time = int(time.time())

# Расчет времени и скорости
elapsed_time = end_time - start_time
symbols_per_minute = len(phrase1) // elapsed_time * 60

print(f"Ваша скорость печати: {symbols_per_minute} символов в минуту.")
print(f"Время, затраченное на печать: {elapsed_time} секунд.")
