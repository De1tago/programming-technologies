class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if key < root.val:
            root.left = insert(root.left, key)
        else:
            root.right = insert(root.right, key)
    return root

# Функция для расчета высоты дерева
def tree_height(node):
    if node is None:
        return 0
    else :
        # Расчет высоты каждой ветви
        left_height = tree_height(node.left)
        right_height = tree_height(node.right)

        # Возвращаем большую высоту
        if left_height > right_height :
            return left_height+1
        else:
            return right_height+1

# Функция для расчета суммы листьев
def leaf_sum(node):
    if node is None:
        return 0
    if node.left is None and node.right is None:
        return node.val
    return leaf_sum(node.left) + leaf_sum(node.right)

# Функция для вывода узлов k-того уровня
def print_nodes_at_level_k(node, k):
    if node is None:
        return
    if k == 1:
        print(node.val)
    elif k > 1:
        print_nodes_at_level_k(node.left, k-1)
        print_nodes_at_level_k(node.right, k-1)

def print_nodes(node):
    if node is not None:
       print_nodes(node.left) 
       print(node.val)
       print_nodes(node.right)
          

# Пример использования
root = None
root = insert(root, 5)
insert(root, 3)
insert(root, 2)
insert(root, 4)
insert(root, 7)
insert(root, 6)
insert(root, 8)

print("Высота дерева:", tree_height(root))
print("Сумма листьев:", leaf_sum(root))
print("Узлы 2-ого уровня:")
print_nodes_at_level_k(root, 2)
print_nodes(root)

