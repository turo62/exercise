list1 = ["a","b","c","d"]
list2 = [["1","2","3"],["4","5"],["7","8"]]
max_column_count = len(list2)
expected_result = [list1]
print(max_column_count)
for row in list2:
    if max_column_count > len(row):
        columns = max_column_count - len(row)
        row += [''] * columns
    expected_result.append(row)
    print(row)
print(expected_result)
