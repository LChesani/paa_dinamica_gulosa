import numpy as np
import time
from functools import cache

# mochila booleana
MAX_BACKPACK = 30


def bool_pack_greedy(weights, values, max_weight):
    reasons = []
    # reason = value / weight - the higher the better
    for i in np.arange(len(weights)):
        reasons.append(values[i] / weights[i])
    
    items_covered = 0
    backpack_itens = []
    current_weight = 0
    while(current_weight < max_weight and items_covered < len(reasons)):
        next_item = max(reasons)
        if current_weight + weights[reasons.index(next_item)] < max_weight:
            backpack_itens.append(reasons.index(next_item))
            current_weight += weights[reasons.index(next_item)]
            reasons[reasons.index(next_item)] = -200
            items_covered += 1
        else:
            reasons[reasons.index(next_item)] = -200
            items_covered += 1
    return backpack_itens


def bool_pack_rec(weights, values, n, c):
    if n < 1 or c < 1:
        return 0
    if weights[n - 1] > c:
        return bool_pack_rec(weights, values, n - 1, c)
    value_no_n = bool_pack_rec(weights, values, n-1, c)
    value_n = values[n-1] + bool_pack_rec(weights, values, n-1, c - weights[n-1])
    return max(value_no_n, value_n)

@cache
def bool_pack_din(weights, values, n, c):
    if n < 1 or c < 1:
        return 0
    if weights[n - 1] > c:
        return bool_pack_rec(weights, values, n - 1, c)
    value_no_n = bool_pack_rec(weights, values, n-1, c)
    value_n = values[n-1] + bool_pack_rec(weights, values, n-1, c - weights[n-1])
    return max(value_no_n, value_n)


def main():
    weights = (1, 2, 5, 7, 8, 20, 12, 3, 5, 2, 3, 4, 7, 8, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    values = (5, 2, 6, 10, 20, 2, 40, 5, 3, 10, 20, 1, 10, 5, 100, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1) 

    print("-------")
    print('GREEDY')
    print("-------")
    a = bool_pack_greedy(weights, values, MAX_BACKPACK)
    value = 0
    for i in a:
        value += values[i]
    print(f'Value on backpack: {value}')

    print("-------")
    print('RECURSIVE NON DINAMIC')
    print("-------")
    a = bool_pack_rec(weights, values, len(weights), MAX_BACKPACK)
    print(f'Value on backpack: {a}')

    print("-------")
    print('RECURSIVE DINAMIC')
    print("-------")
    a = bool_pack_din(weights, values, len(weights), MAX_BACKPACK)
    print(f'Value on backpack: {a}')

    print('-------')
    
    exec_time(weights, values, MAX_BACKPACK)

    

def exec_time(weights, values, max_weight):
    init_greedy = time.time()
    bool_pack_greedy(weights, values, max_weight)
    final_greedy = time.time()
    print(f"Greedy execution time: {final_greedy - init_greedy}")
    init_rec = time.time()
    bool_pack_rec(weights, values, len(weights), max_weight)
    final_rec = time.time()
    print(f'Recursive execution time: {final_rec - init_rec}')
    init_din =time.time()
    bool_pack_din(weights, values, len(weights), MAX_BACKPACK)
    final_din = time.time()
    print(f'Dinamic execution time: {final_din - init_din}')

if __name__== '__main__':
    main()