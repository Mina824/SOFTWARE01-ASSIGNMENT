def list_of_even_integers(num):
    even_num = []
    for i in num:
        if i % 2 == 0:
            even_num.append(i)

    return even_num

def main_program():
    my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    even_list = list_of_even_integers(my_list)

    print("Original list:", my_list)
    print("Cut down list:", even_list)
main_program()
