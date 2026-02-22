"""
stack.py

Demonstrates how a stack data structure works in Python.
A stack is a linear data structure that follows the Last-In, First-Out (LIFO)
principle — the most recently added element is the first one to be removed.
Think of it like a stack of plates: you add to the top and remove from the top.
"""

from __future__ import annotations


class Node:
    """Represents a single node in the stack.

    Each node stores a piece of data and a reference to the node below it.
    """

    def __init__(self, data):
        self.data = data  # The value stored in this node
        self.next: Node | None = (
            None  # Pointer to the node below (None means bottom of stack)
        )


class Stack:
    """A stack data structure implemented with a linked list.

    Maintains a reference to the top node. All operations (push, pop, peek)
    occur at the top of the stack.
    """

    def __init__(self):
        self.top = None  # Empty stack starts with no top node
        self.size = 0  # Track the number of elements in the stack

    def push(self, data):
        """Add a new node with the given data to the TOP of the stack.

        Time complexity: O(1) — no traversal needed.
        """
        new_node = Node(data)
        # Point the new node down to the current top
        new_node.next = self.top
        # The new node is now the top
        self.top = new_node
        self.size += 1

    def pop(self):
        """Remove and return the data from the TOP of the stack.

        Time complexity: O(1) — no traversal needed.
        """
        if self.top is None:
            print("Stack is empty — nothing to pop.")
            return None

        # Grab the data from the top node
        popped_data = self.top.data
        # Move top down to the next node, discarding the old top
        self.top = self.top.next
        self.size -= 1
        return popped_data

    def peek(self):
        """Return the data from the TOP of the stack without removing it.

        Time complexity: O(1) — just looks at the top node.
        """
        if self.top is None:
            print("Stack is empty — nothing to peek.")
            return None

        return self.top.data

    def is_empty(self):
        """Check whether the stack contains any elements.

        Time complexity: O(1) — just checks the top reference.
        """
        return self.top is None

    def get_size(self):
        """Return the number of elements currently in the stack.

        Time complexity: O(1) — uses a maintained counter.
        """
        return self.size

    def search(self, data):
        """Search for a value in the stack and return its depth from the top.

        Depth 0 means the value is at the top of the stack.

        Time complexity: O(n) — may scan the entire stack.
        """
        current = self.top
        depth = 0  # Track how far from the top we are

        while current is not None:
            if current.data == data:
                print(f"Found '{data}' at depth {depth} from the top.")
                return depth
            current = current.next
            depth += 1

        # Value was not found anywhere in the stack
        print(f"'{data}' not found in the stack.")
        return -1

    def traverse(self):
        """Print every node's data in order from top to bottom.

        Time complexity: O(n) — visits every node once.
        """
        if self.top is None:
            print("Stack is empty.")
            return

        elements = []
        current = self.top
        while current is not None:
            elements.append(str(current.data))
            current = current.next  # Move to the node below

        # Display as: TOP -> 3 -> 2 -> 1 -> BOTTOM
        print("TOP -> " + " -> ".join(elements) + " -> BOTTOM")


def main():
    """Demonstrate basic stack operations with example data."""

    print("=== Stack Demo ===\n")

    stack = Stack()

    # --- push: add elements to the top of the stack ---
    print("Pushing 10, 20, 30, 40...")
    stack.push(10)
    stack.push(20)
    stack.push(30)
    stack.push(40)
    stack.traverse()  # Expected: TOP -> 40 -> 30 -> 20 -> 10 -> BOTTOM

    # --- peek: look at the top element without removing it ---
    print(f"\nPeeking at top: {stack.peek()}")  # Expected: 40
    stack.traverse()  # Stack should be unchanged

    # --- size: check how many elements are in the stack ---
    print(f"\nStack size: {stack.get_size()}")  # Expected: 4

    # --- search: find a value by scanning from the top ---
    print("\nSearching for 20...")
    stack.search(20)  # Should find it at depth 2

    print("Searching for 99...")
    stack.search(99)  # Should report not found

    # --- pop: remove elements from the top ---
    print(f"\nPopping: {stack.pop()}")  # Expected: 40
    stack.traverse()  # Expected: TOP -> 30 -> 20 -> 10 -> BOTTOM

    print(f"\nPopping: {stack.pop()}")  # Expected: 30
    stack.traverse()  # Expected: TOP -> 20 -> 10 -> BOTTOM

    # --- is_empty: check if the stack has elements ---
    print(f"\nIs stack empty? {stack.is_empty()}")  # Expected: False

    # --- pop remaining elements ---
    print(f"\nPopping: {stack.pop()}")  # Expected: 20
    print(f"Popping: {stack.pop()}")  # Expected: 10
    stack.traverse()  # Expected: Stack is empty.

    print(f"\nIs stack empty? {stack.is_empty()}")  # Expected: True

    print("\nAttempting to pop from an empty stack...")
    stack.pop()  # Should print 'empty' message

    print("\nAttempting to peek at an empty stack...")
    stack.peek()  # Should print 'empty' message

    print(f"\nFinal stack size: {stack.get_size()}")  # Expected: 0


if __name__ == "__main__":
    main()
