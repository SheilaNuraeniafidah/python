#finding data in a list
buah = ['apel','jeruk','mangga','durian','klengkeng']
try:
    print(buah.index('mangga'))
    print(buah.index('pepaya'))
except ValueError:
    print('your index does not include in list')