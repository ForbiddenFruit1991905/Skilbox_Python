# def foo(x):
#     if x <= 0:
#         return 0
#     # else:
#     return foo(x - 1)
#
# result = foo(3)
# print(result)
#
#
# def foo(x):
#     if x <= 0:
#         print(x)
#     else:
#         foo(x - 1)
#
# foo(3)


# def foo(x):
#     if x == 0:
#         print("Вызов foo(0) возвращает 0")
#         return 0
#     else:
#         print(f"Вызов foo({x - 1}) начинается и добавляется в стек")
#         new_result = foo(x - 1)
#         print(f"Вызов foo({x - 1}) завершился и удаляется из стека")
#         result = x + new_result
#         return result
#
# print(f"Вызов foo(2) начинается и добавляется в стек")
# result = foo(2)
# print(f"Вызов foo(2) завершается и удаляется из стека")
# print("Итоговый ответ — ", result)


def find_fibonacci(N):
	if N == 1 or N == 2:
		return 1
	return find_fibonacci(N - 1) + find_fibonacci(N - 2)

n = 3
result = find_fibonacci(n)
print(result)