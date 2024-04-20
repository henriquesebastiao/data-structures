class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    def __init__(self):
        self.head = Node("head")
        self.size: int = 0

    # Representação da pilha em string
    def __str__(self):
        cur = self.head.next
        out = ""
        while cur:
            out += str(cur.value) + " -> "
            cur = cur.next
        return out[:-4]

    def get_size(self) -> int:
        return self.size

    # Verifica se a pilha está vazia
    def is_empty(self) -> bool:
        return self.size == 0

    # Adiciona um valor na pilha
    def push(self, value):
        node = Node(value)
        node.next = self.head  # Faz o novo nó apontar para o head atual
        self.head = node  # Atualiza o head para o novo nó
        self.size += 1

    # Remove um valor da pilha e o retorna
    def pop(self):
        if self.is_empty():
            raise Exception("Popping from an empty stack")
        delete = self.head.next
        self.head.next = self.head.next.next
        self.size -= 1
        return delete.value

    # Retorna o item no topo da pilha
    def top(self):
        if self.is_empty():
            raise Exception("A lista está vazia")
        return self.head.next.value


# Testando implementação
if __name__ == "__main__":
    stack = Stack()
    for i in range(1, 11):
        stack.push(i)
    print(f"Stack: {stack}")

    for _ in range(1, 6):
        remove = stack.pop()
        print(f"Pop: {remove}")
    print(f"Stack: {stack}")
