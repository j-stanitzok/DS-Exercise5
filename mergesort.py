import matplotlib.pyplot as plt

def mergeSort(unsorted_list):
    if (
        len(unsorted_list) > 1
        and not len(unsorted_list) < 1
        and len(unsorted_list) != 0
    ):
        middle = len(unsorted_list) // 2
        left_half = unsorted_list[:middle]
        right_half = unsorted_list[middle:]

        mergeSort(left_half)
        mergeSort(right_half)

        left = 0
        right = 0
        final_index = 0

        while left < len(left_half) and right < len(right_half):
            if left_half[left] <= right_half[right]:
                left += 1
            else:
                right += 1
            final_index += 1

        while left < len(left_half):
            unsorted_list[final_index] = left_half[left]
            left += 1
            final_index += 1

        while right < len(right_half):
            unsorted_list[final_index] = right_half[right]
            right += 1
            final_index += 1


my_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
x = range(len(my_list))
plt.plot(x, my_list)
plt.show()
mergeSort(my_list)
y = range(len(my_list))
plt.plot(y, my_list)
plt.show()
