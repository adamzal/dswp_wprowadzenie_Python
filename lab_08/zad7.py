from random import randint
from collections import Counter, deque
from zad6 import create_kolo_fortuny

def spin_until_stop(kolo_fortuny):
    first_element = kolo_fortuny[0]
    rotations = 0
    while True:
        rotations += 1
        kolo_fortuny.rotate(1)
        print(list(kolo_fortuny))
        if kolo_fortuny[0] == first_element:
            break
    print(f"Zatrzymano koło fortuny po {rotations} obrotach.")


args = [randint(0, 9) for _ in range(10)]
kolo_fortuny = create_kolo_fortuny(*args)
print(list(kolo_fortuny))
spin_until_stop(kolo_fortuny)