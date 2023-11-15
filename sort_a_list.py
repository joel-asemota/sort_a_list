def sort_list(numbers, order):
    if order == 'asc':
        numbers.sort()
    elif order == 'desc':
        numbers.sort(reverse=True)
    elif order == 'none':
        pass
    else:
        print("Invalid order parameter. Please choose 'asc', 'desc', or 'none'.")
        return

    return numbers
numbers = [5, 2, 8, 1, 9]
order = 'asc'
sorted_numbers = sort_list(numbers, order)
print(sorted_numbers)