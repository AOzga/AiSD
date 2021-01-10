# Zaimplementować funkckję combinations(n: int) -> list[list[int]],
# która zwróci wszystkie kombinacje w następujący sposób:
# każda z wartości w zakresie od 1 do n wystąpi dokładnie dwa razy,
# a odległość między tymi elementami będzie równa ich wartości. Przykładowo dla n = 3 powstaną następujące kombinacje:
# 3 1 2 1 3 2
# 2 3 1 2 1 3
from typing import List

def numbers(n: int):
    if n <= 0:
        return
    print(n)
    numbers(n - 1)


def fib(n: int) -> int:
    if n <= 1:
        return n
    else:
        return fib(n - 1) + fib(n - 2)


def pow(number: int, n: int) -> int:
    if n > 1:
        return number * pow(number, n - 1)
    elif n == 0:
        return 1
    else:
        return number


def reverse(txt: str) -> str:
    if txt == "":
        return txt
    else:
        return txt[-1] + reverse(txt[:-1])


def factorial(n: int) -> int:
    if n > 0:
        return n * factorial(n - 1)
    else:
        return 1


def prime(n: int, i: int = 2) -> bool:
    if n == 1:
        return False
    if n == 2:
        return True
    if i * i > n:
        return True
    if n == i:
        return True
    if n % i == 0:
        return False

    return prime(n, i + 1)


def n_sums(n: int, num: int = 0, roznica=0, lista=None) -> list:
    if lista == None:
        lista = []

    if n > 0:
        index = 0
        if num == 0:
            index = 1
        for i in range(index, 10):
            if n % 2 == 1:
                temp = roznica + i
            else:
                temp = roznica - i
            n_sums(n - 1, num + i * pow(10, n - 1), temp, lista)

    elif n == 0 and roznica == 0:
        lista.append(num)
    return lista


def remove_duplicates(txt: str, last: str = "") -> str:
    if txt == "":
        return txt
    else:
        if last is txt[0]:
            return remove_duplicates(txt[1:], last)
        else:
            last = txt[0]
            return txt[0] + remove_duplicates(txt[1:], last)


def combinations(n: int) -> List[List[int]]:
    pass


def balanced_parentheses(n: int, txt="", balans=0) -> str:
    if n == 0:
        if balans == 0:
            print(txt)
        return txt
    if balans == 0 or balans < n / 2:
        balanced_parentheses(n - 1, txt + "(", balans + 1)
    if balans > 0:
        balanced_parentheses(n - 1, txt + ")", balans - 1)


print(balanced_parentheses(4))
