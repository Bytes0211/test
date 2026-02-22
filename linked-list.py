"""
linked_list.py

Demonstrates how a singly linked list works in Python.
A linked list is a linear data structure where each element (node) holds
a value and a reference (pointer) to the next node in the sequence.
"""


class Node:
    """Represents a single node in the linked list.

    Each node stores a piece of data and a reference to the next node.
    """

    def __init__(self, data):
        self.data = data   # The value stored in this node
        self.next = None   # Pointer to the next node (None means end of list)


class LinkedList:
    """A singly linked list data structure.

    Maintains a reference to the first node (head). All traversal
    and manipulation starts from the head.
    """

    def __init__(self):
        self.head = None  # Empty list starts with no head node

    def append(self, data):
        """Add a new node with the given data to the END of the list.

        Time complexity: O(n) — must walk to the last node first.
        """
        new_node = Node(data)

        if self.head is None:
            # List is empty; the new node becomes the head
            self.head = new_node
            return

        # Walk to the last node (the one whose next is None)
        current = self.head
        while current.next is not None:
            current = current.next

        # Attach the new node after the last node
        current.next = new_node

    def prepend(self, data):
        """Add a new node with the given data to the FRONT of the list.

        Time complexity: O(1) — no traversal needed.
        """
        new_node = Node(data)
        # Point the new node to the current head
        new_node.next = self.head
        # The new node is now the head
        self.head = new_node

    def delete(self, data):
        """Remove the first node whose data matches the given value.

        Time complexity: O(n) — may need to scan the entire list.
        """
        if self.head is None:
            print("List is empty — nothing to delete.")
            return

        # Special case: the head node itself holds the target value
        if self.head.data == data:
            self.head = self.head.next  # Move head forward, discarding old head
            return

        # Walk the list looking for the node just BEFORE the target
        current = self.head
        while current.next is not None:
            if current.next.data == data:
                # Bypass the target node by linking around it
                current.next = current.next.next
                return
            current = current.next

        # If we reach here, the value was not found
        print(f"Value '{data}' not found in the list.")

    def traverse(self):
        """Print every node's data in order from head to tail.

        Time complexity: O(n) — visits every node once.
        """
        if self.head is None:
            print("List is empty.")
            return

        elements = []
        current = self.head
        while current is not None:
            elements.append(str(current.data))
            current = current.next  # Move to the next node

        # Display as: 1 -> 2 -> 3 -> None
        print(" -> ".join(elements) + " -> None")

    def search(self, data):
        """Search for a node by value and return it, or None if not found.

        Time complexity: O(n) — may scan the entire list.
        """
        current = self.head
        position = 0  # Track index for informational output

        while current is not None:
            if current.data == data:
                print(f"Found '{data}' at position {position}.")
                return current  # Return the matching node
            current = current.next
            position += 1

        # Value was not found anywhere in the list
        print(f"'{data}' not found in the list.")
        return None


def main():
    """Demonstrate basic linked list operations with example data."""

    print("=== Linked List Demo ===\n")

    ll = LinkedList()

    # --- append: build the list by adding nodes to the end ---
    print("Appending 10, 20, 30, 40...")
    ll.append(10)
    ll.append(20)
    ll.append(30)
    ll.append(40)
    ll.traverse()   # Expected: 10 -> 20 -> 30 -> 40 -> None

    # --- prepend: add a node to the front ---
    print("\nPrepending 5...")
    ll.prepend(5)
    ll.traverse()   # Expected: 5 -> 10 -> 20 -> 30 -> 40 -> None

    # --- search: find a node by value ---
    print("\nSearching for 20...")
    ll.search(20)   # Should find it at position 2

    print("Searching for 99...")
    ll.search(99)   # Should report not found

    # --- delete: remove a node by value ---
    print("\nDeleting 20...")
    ll.delete(20)
    ll.traverse()   # Expected: 5 -> 10 -> 30 -> 40 -> None

    print("\nDeleting head node (5)...")
    ll.delete(5)
    ll.traverse()   # Expected: 10 -> 30 -> 40 -> None

    print("\nAttempting to delete a value not in the list (99)...")
    ll.delete(99)   # Should print 'not found' message

    print("\nFinal list state:")
    ll.traverse()


if __name__ == "__main__":
    main()
