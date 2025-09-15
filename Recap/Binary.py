n=12
bin(n)
print(bin(n))
l=n.bit_length()
print("Length:",l)


def bit_length(n):
    s=bin(n)
    s=s.lstrip("0b")
    return len(s)

print(bit_length(n))
