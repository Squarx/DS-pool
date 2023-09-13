from my_class import Web1

t = Web1(207)
n = t.split_lst(4)
cnt = 1
for i in n:
    print(f'Arr{cnt}')
    print(i)
    cnt += 1
