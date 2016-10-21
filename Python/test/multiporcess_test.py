from queue import Queue

q = Queue(10)

q.put("wo")
q.put("ai")
q.put(["am", "das"])
print(q.get())
print(q.get())
print(q.get())
print(q.get())

