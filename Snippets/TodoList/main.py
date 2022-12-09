class Item:
    def __init__(self, name, done=False):
        self.name = name
        self.done = done

    def __lt__(self, other):
        return self.done < other.done

    def __str__(self):
        return f"Item {self.name} done={self.done}"

class TodoList:

    def __init__(self):
        self.items = []
    
    def __iter__(self):
        return iter(self.items)
    
    def __str__(self):
        return f"<TodoList with {len(self.items)} items>"


t = TodoList()
t.items.append(Item("send notification", done=True))
t.items.append(Item("test sirens"))
t.items.append(Item("test sms"))

print(t)

for task in sorted(t):
    print(task)
