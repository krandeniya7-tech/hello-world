def mergesort(array):
    if len(array) <= 1:
        return array

    m = len(array) // 2
    print("m:", m)
    print("array:", array)

    left = mergesort(array[:m])
    right = mergesort(array[m:])

    merged = merge(left, right)
    return merged


def merge(left, right):
    merged = []

    while len(left) > 0 and len(right) > 0:
        if left[0] <= right[0]:
            merged.append(left.pop(0))
        else:
            merged.append(right.pop(0))

    if len(left) > 0:
        merged += left
    else:
        merged += right

    return merged


if __name__ == "__main__":
    input_str = input("Enter numbers, separated by ',': ")
    input_list = input_str.split(",")
    value_list = []

    for x in input_list:
        try:
            value_list.append(int(x))
        except ValueError:
            print("Invalid input.")
            quit(1)

    array = value_list.copy()
    print("input_list:", input_list)
    print("value_list:", value_list)
    print("array:", array)

    sorted_array = mergesort(array)
    print(sorted_array)

