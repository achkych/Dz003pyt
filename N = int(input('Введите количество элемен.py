#z16 Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

# N = int(input('Vvediye kolvo elm spiska A: '))
# A_entered = input("Vvedite cherez probel elm spiska: ").split()
# A_num = list(map(int, A_entered))
# if len(A_num) != N:
#     print('Vvedenno ne to kolvo elm!')
# else:
#     X = int(input('Vveditechislo X, kotor neobhod naiti v spiske: '))
#     count = 0
#     for i in range(N):
#         if A_num[i] == X:
#             count += 1
#     print(f'Chislo {X} vstrechaetsya v spiske {count} раз')

#z18. Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
# N = int(input('Vvediye kolvo elm spiska A: '))
# A_entered = input("Vvedite cherez probel elm spiska: ").split()
# A_num = list(map(int, A_entered))
# if len(A_num) != N or N == 0:
#     print('Vvedenno ne to kolvo elm!')
# else:
#     X = int(input('Vvedite chislo X, s kotor neobhodimo sravnit elm spiska: '))
#     min = X - A_num[0]
#     index = 0
#     for i in range(1, N):
#         count = X - A_num[i]
#         if count < min:
#             min = count
#             index = i
#     print(f'Число {A_num[index]} в списке A наиболее близко по величине к числу {X}, их разница составляет {X - A_num[index]}')
 
 #z20. Скрабл. Nesmog.
#  N = abs(int(input('Введите 1, если играем в английской раскладке, либо 0, если в русской: ')))
# word = input('Введите слово: ').upper()
# if N == 1:
# 	print('За это слово вы получаете', sum([k for i in word for k, v in eng.items() if i in v]), 'очков')
# elif N == 0:
# 	print('За это слово вы получаете', sum([k for i in word for k, v in rus.items() if i in v]), 'очков')
# else:
#     print('Вы играете не по правилам!')