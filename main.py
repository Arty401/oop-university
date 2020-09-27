from random import randint


def task2(n: int):
    def get_count(matrica: list):
        count = 0
        flag = False
        for i in range(len(matrica)):
            flag = False
            for j in range(len(matrica[i])):
                if matrix[j][i]:
                    flag = True
                else:
                    flag = False
                    break
            if flag:
                count += 1
        return count

    def accumulate_elem(matrix):
        new_matrix = []
        for row in range(len(matrix)):
            new_matrix.append([sum(matrix[row]), matrix[row]])
        return new_matrix

    def sort_matrica(matrix):
        return sorted(matrix)

    matrix = [[randint(0, n) for i in range(0, n)] for j in range(0, n)]
    print('Не нулевых столбцов:', get_count(matrix))
    new_matrix = accumulate_elem(matrix)
    print('Отсортированная матрица по характеристике ряда: ')
    for row in sort_matrica(new_matrix):
        print(f'Сумма элементов: {row[0]}  Ряд: {row[1]}')


def task11(n: int):
    matrix = [[randint(0, n) for i in range(0, n)] for j in range(0, n)]
    for row in matrix:
        print(row)
    print()
    max_bot = []
    max_top = []
    i = 0
    while i < n:
        j = 0
        while j < n:
            if i < j:
                max_top.append(matrix[i][j])
            elif i > j:
                max_bot.append(matrix[i][j])
            j += 1
        i += 1
    print("Максимум выше паралельно главной диагонали: ", max(max_top))
    print("Максимум ниже паралельно главной диагонали: ", max(max_bot))
    return max_top, max_bot


def main():
    n = int(input('Введите N: '))
    print("\nTASK 11")
    task11(n)
    print("\nTASK 2")
    task2(n)


if __name__ == '__main__':
    while True:
        main()
