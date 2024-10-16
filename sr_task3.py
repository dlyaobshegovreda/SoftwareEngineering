from collections import Counter


def most_frequent_digits(s):
    digit_count = Counter(int(digit) for digit in s)

    most_common_digits = digit_count.most_common(3)

    most_common_digits_sorted = sorted(most_common_digits)

    result_dict = {}

    for digit, count in most_common_digits_sorted:
        result_dict[digit] = count

    return result_dict


input_string = "1234567890123456789012345"
result = most_frequent_digits(input_string)

print("Три самых частых числа и их количество:", result)