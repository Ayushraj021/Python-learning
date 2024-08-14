def func(sample, res, key, val):
    if key in sample:
        res = True
    else:
        sample.update({key: val})
        res = False
    res = None

sample = {"XS": 1, "X": 0, "XL": 3, "XXL": 4}
res = None
func(sample, res, "X", 2)
print(sample["X"], res)
