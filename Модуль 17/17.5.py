# Итак, рассмотрим бинарное дерево
# Основное его свойство заключается в том, что у каждого узла может быть не более 2 потомков
# соответственно, левый и/или правый.
# В нашей структуре данных, в каждом узле бинарного дерева мы будем хранить указатель на левого и правого потомка.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None

# Мы создали класс узла, а в конструкторе записали значение, которое должно храниться в нём.
# Также инициализировали левого и правого потомка.
# Напишем разные методы для вставки на место левого потомка и на место правого потомка.


    def insert_left(self, next_value):
        if self.left_child is None:
            self.left_child = BinaryTree(next_value)
        else:
            new_child = BinaryTree(next_value)
            new_child.left_child = self.left_child
            self.left_child = new_child
        return self

# Поясним, что здесь произошло.
# Если в текущем узле нет левого потомка, то новый узел вставляем на его место.
# Если левый потомок уже существует — он становится таким же левым потомком, но уже нового узла.
# Иными словами, он остается левым, но его глубина увеличивается. Аналогично поступим с правым.


    def insert_right(self, next_value):
        if self.right_child is None:
            self.right_child = BinaryTree(next_value)
        else:
            new_child = BinaryTree(next_value)
            new_child.right_child = self.right_child
            self.right_child = new_child
        return self

# В обоих случаях мы возвращаем ссылку на текущий узел.
# Это нам необходимо, чтобы создавать цепочки действий.
# Рассмотрим на примере:


A_node = BinaryTree('A').insert_left('B').insert_right('C')

# В одной строчке мы создали корневой узел дерева, вставили левого потомка и затем — сразу правого.
# Получая ссылки на потомков через атрибуты left_child и right_child,
# можно проделать ту же самую цепочку действий, чтобы расширить дерево.
