class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self) -> str:
        return self.data


class LinkedList:
    def __init__(self, nodes=None):
        self.head = None
        if nodes is not None:
            node = Node(data=nodes.pop(0))
            self.head = node
            for item in nodes:
                node.next = Node(data=item)
                node = node.next

    def __repr__(self) -> str:
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append('None')
        return ' -> '.join(nodes)

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def add_first(self, node: Node):
        """Adiciona um novo nó ao início da lista"""
        node.next, self.head = self.head, node

    def add_last(self, node: Node):
        if self.head is None:
            self.head = node
            return
        for current_node in self:
            pass
        current_node.next = node

    def add_after(self, target_node_data, new_node: Node):
        """Adiciona um novo nó no meio da string após um determinado nó"""
        if self.head is None:
            raise Exception('A lista está vazia')

        for node in self:
            if node.data == target_node_data:
                new_node.next = node.next
                node.next = new_node

                return

        raise Exception(f'Nó com o dado: {target_node_data} não existe')

    def add_before(self, target_node_data, new_node: Node):
        """Adiciona um novo nó no meio da string antes de um determinado nó"""
        if self.head is None:
            raise Exception('A lista está vazia')

        if self.head.data == target_node_data:
            return self.add_first(new_node)

        previous_node = self.head
        for node in self:
            if node.data == target_node_data:
                previous_node.next = new_node
                new_node.next = node
                return
            previous_node = node

        raise Exception(f'Nó com dado {target_node_data} não existe')

    def remove(self, target_node_data):
        """Remove um nó específico"""
        if self.head is None:
            raise Exception('A lista está vazia')

        if self.head.data == target_node_data:
            self.head = self.head.next
            return

        previous_node = self.head
        for node in self:
            if node.data == target_node_data:
                previous_node.next = node.next
                return
            previous_node = node

        raise Exception(f'Nó com dado {target_node_data} não existe')


# Testando implementação
if __name__ == '__main__':
    llist = LinkedList(['a', 'b', 'c'])
    print(llist)
    llist.add_first(Node('z'))
    print(llist)
    llist.add_last(Node('x'))
    print(llist)
    llist.add_before('b', Node('u'))
    print(llist)
    llist.add_after('x', Node('y'))
    print(llist)
    llist.remove('z')
    print(llist)
