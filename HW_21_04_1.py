class FixedSizeStack:
    def __init__(self, max_size):
        self.max_size = max_size
        self.stack = []

    def push(self, string):
        if len(self.stack) < self.max_size:
            self.stack.append(string)
            print("String pushed to the stack")
        else:
            print("Stack is full")

    def pop(self):
        if self.stack:
            print("Popped string:", self.stack.pop())
        else:
            print("Stack is empty")

    def count(self):
        print("Number of strings in the stack:", len(self.stack))

    def is_empty(self):
        if not self.stack:
            print("Stack is empty")
        else:
            print("Stack is not empty")

    def is_full(self):
        if len(self.stack) == self.max_size:
            print("Stack is full")
        else:
            print("Stack is not full")

    def clear(self):
        self.stack.clear()
        print("Stack cleared")

    def peek(self):
        if self.stack:
            print("Top string in the stack:", self.stack[-1])
        else:
            print("Stack is empty")

def show_menu():
    print("1. Push a string to the stack")
    print("2. Pop a string from the stack")
    print("3. Count the number of strings in the stack")
    print("4. Check if the stack is empty")
    print("5. Check if the stack is full")
    print("6. Clear the stack")
    print("7. Peek at the top string in the stack")
    print("0. Exit")

    choice = input("Enter (1-0): ")
    return choice

max_size = 5
stack = FixedSizeStack(max_size)

while True:
    choice = show_menu()

    if choice == '1':
        string = input("Enter the string to push to the stack: ")
        stack.push(string)
    elif choice == '2':
        stack.pop()
    elif choice == '3':
        stack.count()
    elif choice == '4':
        stack.is_empty()
    elif choice == '5':
        stack.is_full()
    elif choice == '6':
        stack.clear()
    elif choice == '7':
        stack.peek()
    elif choice == '0':
        print("end")
        break
    else:
        print("Error!!!")