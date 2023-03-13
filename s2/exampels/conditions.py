a = 20 
b = 40
# write conditionals in block
if a > b:
    print('a is greater than b')
elif a == b:
    print('a is equal to b')
else:
    print('a is less than b')
# write conditionals in one line
print('a is greater than b') if a > b else print('a is equal to b') if a == b else print('a is less than b')