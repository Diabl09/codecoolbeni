import random

def listoverlap(list1, list2):
    a_set = set(list1)
    b_set = set(list2)
    compare_list = list(a_set & b_set)
    return compare_list

#def random_lists_segment(random_list1, random_list2):
   # a_set = set(random_list1)
   # b_set = set(random_list2)
   # compare_set = (a_set & b_set)
   # print(compare_set)

def main():
    #random_list1 = random.sample(range(50), 12)
    #random_list2 = random.sample(range(50), 11)
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    compare_list = listoverlap(a, b)
    print(compare_list)
    #random_lists_segment(random_list1, random_list2)
    return


if __name__ == '__main__':
    main()
