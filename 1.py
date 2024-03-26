arr = [('a', '1'), ('b', '2'), ('c', '3')]

print('{0} {1}'.format(i, *map(''.join, zip(*arr))))