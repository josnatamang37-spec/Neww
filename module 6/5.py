def get_evens(number):
    new_list = []
    for n in number:
        if n % 2 == 0:
            new_list.append(n)
            return new_list
        original = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        cut_down = get_evens(original)
        print(f"Original list: {original}")
        print(f"Cut down list: {cut_down}")