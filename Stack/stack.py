# Stack Implementation with user-defined size

stack = []
MAX_SIZE = 0


# PUSH
def push(element):
    if len(stack) == MAX_SIZE:
        print("Stack Overflow! Stack is full.")
    else:
        stack.append(element)
        print(f"{element} pushed. Stack: {stack}")


# POP
def pop():
    if len(stack) == 0:
        print("Stack Underflow! Stack is empty.")
    else:
        removed = stack.pop()
        print(f"{removed} popped. Stack: {stack}")
        return removed


# PEEK
def peek():
    if len(stack) == 0:
        print("Stack is empty!")
    else:
        print(f"Top element: {stack[-1]}")


# DISPLAY
def display():
    if len(stack) == 0:
        print("Stack is empty!")
    else:
        print("Stack (top → bottom):", stack[::-1])


# ---- Main Program ----

MAX_SIZE = int(input("Enter stack size: "))
print(f"Stack created with max size {MAX_SIZE}\n")

while True:
    print("\n--- MENU ---")
    print("1. Push")
    print("2. Pop")
    print("3. Peek")
    print("4. Display")
    print("5. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        val = int(input("Enter value to push: "))
        push(val)
    elif choice == 2:
        pop()
    elif choice == 3:
        peek()
    elif choice == 4:
        display()
    elif choice == 5:
        print("Exiting program.")
        break
    else:
        print("Invalid choice!")
"""```

---

**Sample Run:**
```
Enter stack size: 3

--- MENU ---
1. Push  2. Pop  3. Peek  4. Display  5. Exit
Enter choice: 1
Enter value to push: 10
10 pushed. Stack: [10]

Enter choice: 1
Enter value to push: 20
20 pushed. Stack: [10, 20]

Enter choice: 1
Enter value to push: 30
30 pushed. Stack: [10, 20, 30]

Enter choice: 1
Enter value to push: 40
Stack Overflow! Stack is full.      ← max size 3 reached

Enter choice: 2
30 popped. Stack: [10, 20]

Enter choice: 2
20 popped. Stack: [10]

Enter choice: 2
10 popped. Stack: []

Enter choice: 2
Stack Underflow! Stack is empty.    ← nothing left to pop"""
