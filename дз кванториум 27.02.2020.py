# 1
try:
	a = input("Введите 1-е число: ")
	b = input("Введите 2-е число: ")
	print("Результат =", int(a)/int(b))
except ValueError:
	print("Ты ввел не число, исправь это пожалуйста!!!")
except ZeroDivisionError:
	print("На ноль делить нельзя!")


# 2

try:
	a = input("\nВведите 1-е число: ")
	b = input("Введите 2-е число: ")
	print("Результат =", int(a)/int(b))
except (ValueError, ZeroDivisionError):
	print("Что-то пошло не так...\nА что именно, подумай сам!")