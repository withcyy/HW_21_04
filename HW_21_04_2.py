class DynamicSizeStack:
    def __init__(self):
        self.stack = []

    def push(self, string):
        self.stack.append(string)
        print("String pushed to the stack")

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
    print("5. Clear the stack")
    print("6. Peek at the top string in the stack")
    print("0. Exit")

    choice = input("Enter (1-0): ")
    return choice


stack = DynamicSizeStack(max_size)

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
        stack.clear()
    elif choice == '6':
        stack.peek()
    elif choice == '0':
        print("end")
        break
    else:
        print("Error!!!")