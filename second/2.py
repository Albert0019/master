def filter_strings(filter_func, str_list: list) -> list:
    return [s for s in str_list if filter_func(s)]

# Test
str_list = ["hello", "world", "a test", "apple", "12345", "abc"]

# Exclude strings containing spaces
filtered_list1 = filter_strings(lambda s: ' ' not in s, str_list)
print(filtered_list1)  # ['hello', 'world', 'apple', '12345', 'abc']

# Exclude strings starting with the letter "a"
filtered_list2 = filter_strings(lambda s: not s.startswith('a'), str_list)
print(filtered_list2)  # ['hello', 'world', '12345']

# Exclude strings shorter than 5 characters
filtered_list3 = filter_strings(lambda s: len(s) >= 5, str_list)
print(filtered_list3)  # ['hello', 'world', 'a test']