def splitter(data, pred):
    yes, no = [], []
    for d in data:
        if pred(d):
            yes.append(d)
        else:
            no.append(d)
    return [yes, no]


data = map(str, range(14))
pred = lambda i: int(i) % 2 == 0
print(splitter(data, pred))

