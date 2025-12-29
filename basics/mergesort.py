
def mergesort(array):
    if len(array) <= 1:
        return array

    m = len(array) // 2
    print("m:", m)
    print("array:", array)

    left = mergesort(array[:m])
    right = mergesort(array[m:])

    return merge(left, right)


def merge(left, right):
    merged = []
    while len(left) > 0 and len(right) > 0:
        if left[0] <= right[0]:
            merged.append(left.pop(0))
        else:
            merged.append(right.pop(0))

    if len(left) > 0:
        merged += left
    if len(right) > 0:
        merged += right

    print("Merging...")
    print("left:", left)
    print("right:", right)
    print("merged:", merged)
    return merged


if __name__ == "__main__":
    input_str = input("Enter numbers, separated by ',': ")
    input_list = input_str.split(",")
    print("input_list:", input_list)

    value_list = []
    for x in input_list:
        try:
            value_list.append(int(x))
        except ValueError:
            print("Invalid input.")
            quit(1)
    print("value_list:", value_list)

    sorted_list = mergesort(value_list)
    print(sorted_list)

