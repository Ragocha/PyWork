def binary_search(list, item):
    """ Данная функция реализует бинарный поиск.
        Параметры функции: A - список, item - искомое занчение.
        Функция вернет номер искомого значениея (его индекс).
        Функция начинает проверять среднее значение, если искомое значение больше среднего,
         то значения меньше среднего откидываются и функция повторяется (и наоборот).
         Если значение так и не было найдено, функция вернет "No the number".
    """
    #hi
    low = 0
    higt = len(list) - 1
    while low <= higt:
        mid = round((low + higt) / 2)
        gusse = list[mid]
        if gusse < item:
            low = mid + 1
        elif gusse > item:
            higt = mid - 1
        else:
            return mid
    else:
        return None


def test_binary_search(f):
    print("testcase #1: ", end=" ")
    A = [1, 2, 3, 4, 5]
    item = 5
    number_test_item = 4
    f(A, item)
    print("Ok" if f(A, item) == number_test_item else "Fail")

    print("testcase #2: ", end=" ")
    A = [1, 2, 3, 4, 5]
    item = -1
    number_test_item = None
    f(A, item)
    print("Ok" if f(A, item) == number_test_item else "Fail")

    print("testcase #3: ", end=" ")
    A = [1, 2, 3, 4, 5]
    item = 2
    number_test_item = 1
    f(A, item)
    print("Ok" if f(A, item) == number_test_item else "Fail")


test_binary_search(binary_search)
