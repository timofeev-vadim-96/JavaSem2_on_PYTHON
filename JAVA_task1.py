# 1.Реализуйте алгоритм сортировки пузырьком числового массива, результат после каждой
# итерации запишите в лог-файл.
# (через FileWriter).
import random
arr = [random.randint(0,100) for x in range(15)]
def BubbleSorting(inputArray):
    try:
        with open('log.txt', 'w') as data:
            for i in range(len(inputArray)):
                for j in range(1, len(inputArray)-i):
                    if (inputArray[j] < inputArray[j - 1]):
                        temp = inputArray[j]
                        inputArray[j] = inputArray[j - 1]
                        inputArray[j - 1] = temp
                data_str = ', '.join(map(str, arr))
                data.writelines(data_str + '\n')
            return inputArray
    except:
        print('Задача провалена')
print(BubbleSorting(arr))