name="computer"
distance=2
for i in list(name):
    if distance >= ord("2"):
        new=ord(i)+distance-ord("2")
        print(chr(96+new))
    else:
        print(chr(ord(i)+distance))