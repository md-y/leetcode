from typing import Optional


class Node:
    def __init__(self, val: int):
        self.val = val
        self.prev: Optional[Node] = None
        self.next: Optional[Node] = None
        self.keys: dict[str, bool] = {}


class AllOne:
    def __init__(self):
        self.key_lookup: dict[str, Node] = {}

        self.min: Optional[Node] = None
        self.max: Optional[Node] = None

    def inc(self, key: str) -> None:
        if key not in self.key_lookup:
            if not self.min:
                self.min = Node(1)
                self.max = self.min
            elif self.min.val != 1:
                self.insert_before(self.min, Node(1))
            self.min.keys[key] = True
            self.key_lookup[key] = self.min
        else:
            node = self.key_lookup[key]
            if not node.next or node.next.val != node.val + 1:
                self.insert_after(node, Node(node.val + 1))
            self.key_lookup[key] = node.next
            node.next.keys[key] = True
            self.pop_key(node, key)

    def dec(self, key: str) -> None:
        if key not in self.key_lookup:
            return

        node = self.key_lookup[key]
        if node.val == 1:
            self.key_lookup.pop(key)
            self.pop_key(node, key)
        else:
            if not node.prev or node.prev.val != node.val - 1:
                self.insert_before(node, Node(node.val - 1))
            self.key_lookup[key] = node.prev
            node.prev.keys[key] = True
            self.pop_key(node, key)

    def getMaxKey(self) -> str:
        if not self.max or not self.max.keys:
            return ""
        return next(iter(self.max.keys))

    def getMinKey(self) -> str:
        if not self.min or not self.min.keys:
            return ""
        return next(iter(self.min.keys))

    def insert_before(self, current_node: Node, new_node: Node):
        if current_node.prev:
            current_node.prev.next = new_node

        new_node.prev = current_node.prev
        current_node.prev = new_node
        new_node.next = current_node

        if current_node == self.min:
            self.min = new_node

        return new_node

    def insert_after(self, current_node: Node, new_node: Node):
        if current_node.next:
            current_node.next.prev = new_node

        new_node.next = current_node.next
        current_node.next = new_node
        new_node.prev = current_node

        if current_node == self.max:
            self.max = new_node

        return new_node

    def pop_node(self, node: Node):
        if node == self.min:
            if node.next:
                node.next.prev = None
                self.min = node.next
            else:
                self.min = None
        elif node == self.max:
            if node.prev:
                node.prev.next = None
                self.max = node.prev
            else:
                self.max = None
        else:
            node.prev.next = node.next
            node.next.prev = node.prev

    def pop_key(self, node: Node, key: str):
        node.keys.pop(key)
        if not node.keys:
            self.pop_node(node)

