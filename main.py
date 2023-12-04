import csv

# res_card = 0
# total_res = 0
#
# with open('file.csv') as file:
#     file = csv.reader(file)
#     for line in file:
#         wining_numbers = line[0].split('|')[0].split(' ')
#         print(wining_numbers)
#         my_numbers = line[0].split('|')[1].split(' ')
#         print(my_numbers)
#         for n in my_numbers:
#             if n != '':
#                 if n in wining_numbers:
#                     print(n, wining_numbers)
#                     if res_card == 0:
#                         res_card += 1
#                     elif res_card > 0:
#                         print(n, 'nnnnnnnn')
#                         res_card = res_card * 2
#                         print(res_card)
#         total_res += res_card
#         res_card = 0
#
# print(total_res)


res_card = 0
total_res = 0
nr_of_line = 1

with open('file.csv') as file:
    file = csv.reader(file)
    for line in file:
        nr_of_line += 1
    hashmap = {i: 1 for i in range(1, nr_of_line)}
    nr_of_line = 1

with open('file.csv') as file:
    file = csv.reader(file)
    for line in file:
        wining_numbers = line[0].split('|')[0].split(' ')
        my_numbers = line[0].split('|')[1].split(' ')
        for n in my_numbers:
            if n != '':
                if n in wining_numbers:
                    res_card += 1
        for i in range(hashmap[nr_of_line]):
            for j in range(1, res_card + 1):
                if hashmap[nr_of_line + j]:
                    hashmap[nr_of_line + j] += 1

        total_res += hashmap[nr_of_line]
        nr_of_line += 1
        print(hashmap , total_res, 'toatl res')
        res_card = 0



print(total_res)