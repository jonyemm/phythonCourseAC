import random
def num_pieces(num,lenght):
    ot = list(range(1,lenght+1))[::-1]
    all_list = []
    for i in range(lenght-1):
        n = random.randint(1, num-ot[i])
        all_list.append(n)
        num -= n
    all_list.append(num) 
    return all_list

milista = num_pieces(1000000,17)
print(milista)