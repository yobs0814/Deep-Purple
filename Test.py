a = [ 0 * 1 for i in range(100)]

import chess


b = chess.Board()
#b.push_san("e4")
print(b)
c1 = b.copy()
c = c1.__repr__()
for i in range(7,len(c)):
    print(i,c[i])

c2 = c[7:]


print(c2)

c3 = c[:-14]
c4 = c[:-15]
print(c3)
print(c4)

c5 = c[7:-15]

print(c5)