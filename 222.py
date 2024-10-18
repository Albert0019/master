def filter_strings(filter_func, string_list):
    return [s for s in string_list if filter_func(s)]
remove_empty = lambda s: s.strip() != ""  # 删除空字符串
remove_starting_with_a = lambda s: not s.lower().startswith("a")  # 删除以字母"A"开头的字符串
remove_short_strings = lambda s: len(s) >= 5  # 删除长度小于5的字符串
string_list = ["apple", "   ", "Bronya", "Zaychik", "我将，点燃大海！", "阿米诺斯", "a","I will have the order!"]
filtered_list = filter_strings(remove_empty, string_list)
filtered_list = filter_strings(remove_starting_with_a, filtered_list)
filtered_list = filter_strings(remove_short_strings, filtered_list)

print("筛选后的字符串列表：", filtered_list)