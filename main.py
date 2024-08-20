class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            return None
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            return None
        return self.items[-1]

    def size(self):
        return len(self.items)

def is_balanced(sequence):
    stack = Stack()
    pairs = {
        ')': '(',
        ']': '[',
        '}': '{'
    }
    
    for char in sequence:
        if char in pairs.values():
            stack.push(char)
        elif char in pairs.keys():
            if stack.is_empty() or stack.pop() != pairs[char]:
                return "Несбалансированно"
    
    return "Сбалансированно" if stack.is_empty() else "Несбалансированно"

# print(is_balanced("(((([{}]))))"))
# print(is_balanced("[([])((([[[]]])))]{()}"))
# print(is_balanced("{{[()]}}"))
# print(is_balanced("}{"))  
# print(is_balanced("{{[(])]}}"))  
# print(is_balanced("[[{())}]"))  

result = input("введите символы:")
print(is_balanced(result))