from collections import deque
import datetime

d = deque()

start_time = datetime.datetime.now()
for i in range(100000):
    d.append(i)
end_time = datetime.datetime.now()
print("Czas operacji append na deque: ", end_time - start_time)

start_time = datetime.datetime.now()
for i in range(100000):
    d.appendleft(i)
end_time = datetime.datetime.now()
print("Czas operacji appendleft na deque: ", end_time - start_time)

l = []

start_time = datetime.datetime.now()
for i in range(100000):
    l.append(i)
end_time = datetime.datetime.now()
print("Czas operacji append na liście: ", end_time - start_time)

start_time = datetime.datetime.now()
for i in range(100000):
    l.insert(0, i)
end_time = datetime.datetime.now()
print("Czas operacji insert(0) na liście: ", end_time - start_time)