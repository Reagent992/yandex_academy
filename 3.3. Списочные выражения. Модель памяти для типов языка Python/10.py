# RLE наоборот
# Верно.
rle = [('a', 2), ('b', 3), ('c', 1)]

f = ''.join([x * y for x, y in rle])
print(f)
