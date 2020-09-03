a = [1,2,3,2,1,5,6,5,5,5,8,8]
seen = set()
uniq = [x for x in a if x not in seen and not seen.add(x)]
print(uniq)