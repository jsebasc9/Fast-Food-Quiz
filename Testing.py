dictionary1 = {"a": 1, "b": 2}
dictionary2 = {"a": 3, "b": 2}
common_pairs = dict()
for key in dictionary1:
    if (key in dictionary2 and dictionary1[key] == dictionary2[key]):
        common_pairs[key] = dictionary1[key]
print(common_pairs)