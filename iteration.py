# for (let i = 0; i < array.length; i++) {
# 
# }

for i in range(10):
    pass

# Pythonic
array = []
for item in array:
    pass

# Have __iter__ therefore are iterables
# print(list, dir(list))
# print(dict, dir(dict))
# print(tuple, dir(tuple))
# print(str, dir(str))

# iter() when used on an iterable returns an interator
print(iter(""))

string_iterator = iter("Hello world")

while True:
    try:
        a = next(string_iterator)
        print(a)
    except StopIteration:
        print("End of")
        break

print("Finished!")
