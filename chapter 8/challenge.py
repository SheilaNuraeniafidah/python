fo = open("d:/semester 1/pemrograman terstruktur/python/readme_English.txt", "r")
#init
num_char = 0
num_vowals = 0
num_cons = 0
num_nonletter = 0
while True:
    data = fo.read(1)
    #num_char increment
    num_char += 1
    #if data vowals then num_vowals increasing
    if data in ['A', 'I','U','E','O','a','i','u','e','o']:
        num_vowals += 1
    #if data consonant then num_cons increasing
    if data in['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']:
        num_cons += 1
    #if data not a letter
    else:
        num_nonletter += 1
    #if pointer reaches end of file then break
    if not data :
        break
#output
print("number of character is:", num_char)
print("number of vowals:", num_vowals)
print("number of consonant:", num_cons)
print ("number of non letter:", num_nonletter)


