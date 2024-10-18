class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


# Завдання 1: Знаходження найбільшого значення у двійковому дереві пошуку

def find_max_value(root):
    if root is None:
        return None
    
    current = root
    while current.right:
        current = current.right
    return current.value

# Приклад використання
root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(20)
root.right.right = TreeNode(30)

print("Найбільше значення:", find_max_value(root))  # Виведе: Найбільше значення: 30


# Завдання 2: Знаходження найменшого значення у двійковому дереві пошуку

def find_min_value(root):
    if root is None:
        return None
    
    current = root
    while current.left:
        current = current.left
    return current.value

# Приклад використання
print("Найменше значення:", find_min_value(root))  # Виведе: Найменше значення: 5


# Завдання 3: Знаходження суми всіх значень у двійковому дереві пошуку

def sum_tree_values(root):
    if root is None:
        return 0
    return root.value + sum_tree_values(root.left) + sum_tree_values(root.right)

# Приклад використання
print("Сума всіх значень:", sum_tree_values(root))  # Виведе: Сума всіх значень: 65
