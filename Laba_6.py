import argparse


def check_positive(value):
    """Проверка на положительное целочисленное

    Args:
        value: Вводимое значение из командной строки

    Returns:
        int: положительное целочисленное
    """
    ivalue = int(value)
    if ivalue <= 0:
        raise argparse.ArgumentTypeError("%s is an invalid positive\
                                         int value" % value)
    return ivalue


parser = argparse.ArgumentParser(description="Монотонно убывающие и\
                                              возрастающие последовательности")
parser.add_argument("n", type=check_positive)
args = parser.parse_args()


def syracuse_sequence(n: int) -> list[int]:
    """Сиракузская последовательность

    Args:
        n (int): Натуральное число

    Returns:
        list[int]: Список сиракузской последовательности
    """
    list_n = [n]
    for n in list_n:
        if n % 2 == 0:
            list_n.append(n // 2)
        elif n % 2 == 1 and n != 1:
            list_n.append(3*n + 1)
    return list_n


def syracuse_max(list_n: list[int]) -> int:
    """Поиск максимального числа в сиракузской последовательности

    Args:
        list_n (list[int]): Список сиракузской последовательности

    Returns:
        int: Максимальное число сиракузской последовательности
    """
    n_max = list_n[0]
    for n in list_n:
        n_max = n if n > n_max else n_max
    return n_max


def main(n):
    list_n = syracuse_sequence(n)
    for i in list_n:
        print(i, end=" ")
    print()
    n_max = syracuse_max(list_n)
    print(n_max)


if __name__ == "__main__":
    main(args.n)
