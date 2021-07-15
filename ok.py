a1 = int(input())
b1 = int(input())
c1 = int(input())
a2 = int(input())
b2 = int(input())
c2 = int(input())
if a1 >= b1 and a1 >= c1:  # a is greatest

    if b1 >= c1:  # a > b > c(init)
        (c1, a1) = (a1, c1)  # c > b > a(final)
    else:  # a > c > b(init)
        (c1, a1) = (a1, c1)  # c > a > b
        (a1, b1) = (b1, a1)
# до этого код отлично работает
elif b1 >= a1 and b1 >= c1:
    if a1 >= c1:  # b > a > c(init)
        (a1, c1) = (c1, a1)  # b c a
        (b1, c1) = (c1, b1)
    else:  # b > c > a  (c > b > a)
        (c1, b1) = (b1, c1)
elif c1 >= b1 and c1 >= a1:
    # we must (c > b > a)
    if b1 >= a1:  # c b a
        b1 = b1
        a1 = a1
        c1 = c1
    else:  # c a b
        (b1, a1) = (a1, b1)
if a2 >= b2 and a2 >= c2:  # a is greatest

    if b2 >= c2:  # a > b > c(init)
        (c2, a2) = (a2, c2)  # c > b > a(final)
    else:  # a > c > b(init)
        (c2, a2) = (a2, c2)  # c > a > b
        (a2, b2) = (b2, a2)
# до этого код отлично работает
elif b2 >= a2 and b2 >= c2:
    if a2 >= c2:  # b > a > c(init)
        (a2, c2) = (c2, a2)  # b c a
        (b2, c2) = (c2, b2)
    else:  # b > c > a  (c > b > a)
        (c2, b) = (b2, c2)
elif c2 >= b2 and c2 >= a2:
    # we must (c > b > a)
    if b2 >= a2:  # c b a
        b2 = b2
        a2 = a2
        c2 = c2
    else:  # c a b
        (b2, a2) = (a2, b2)
print(a1, b1, c1)
print(a2, b2, c2)
if a1 == a2 and b1 == b2 and c1 == c2:
    print('Boxes are equal')
elif a1 >= a2 and b1 >= b2 and c1 >= c2:
    print('The first box is larger than the second one')
elif a2 >= a1 and b2 >= b1 and c2 >= c1:
    print('The first box is smaller than the second one')
else:
    print('Boxes are incomparable')
