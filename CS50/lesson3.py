#Функция print() печатает строку
print("Hello, CS50")

#Бесконечный цикл
#while True:
#	print("РHello, World!")
	
#Цикл for от 0 до 9
for i in range(10):
	print("i = ", i)

#Переменные(variables)
name = "your name"
print("Hello", name)

#Цикл while
counter = 1
while counter <= 10:
	print("Hello")
	counter += 1


#=========================================#
x, y = input("Введите 2 числа: ").split()
x = int(x)
y = int(y)
print("{} + {} = {}".format(x, y, x +y ))
print("{} + {} = {}".format(x, y, x - y))
print("{} + {} = {}".format(x, y, x * y))
print("{} + {} = {}".format(x, y, x / y))
#=========================================#

#Комментарии
#Однострочный комментарий с помощью #
#'''Возможность 
#       делать
#          многострочный
#             комментарий'''
             
#===========================================#

#Boolean expressions(Булево выражене)
x = input("Ввидите число: ")
x = int(x)

if (x >= 1) and (x <= 3):
	print("{} - Маленькое число:".format(x))
elif (x >= 4) and (x <= 6):
	print("{} - Средние число!".format(x))
elif (x >= 7) and (x <= 10):
	print("{} - Большое число!".format(x))
else:
	print("{} - Такое число не потходит!")
	
#=============================================#


#Получение частного(деление) 1.0 / 10.0 c отобра-ем опрелел-го кол-ва \
#знаков после точки. {:.2f} - 2 цифры после точки

print("1.0 / 10.0 = {:.2f}".format(1.0 / 10.0)) 










