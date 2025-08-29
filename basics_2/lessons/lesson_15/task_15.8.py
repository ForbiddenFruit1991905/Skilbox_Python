# Пример 1:

# import networkx as nx
# import matplotlib.pyplot as plt
#
# # Создание пустого графа
# graph = nx.Graph()
#
# # Добавление вершин
# graph.add_node("A")
# graph.add_nodes_from(["B", "C", "D"])
#
# # Добавление рёбер
# graph.add_edge("A", "B")
# graph.add_edges_from([("B", "C"), ("C", "D"), ("D", "A")])
#
# # Получение списка вершин и рёбер
# nodes = graph.nodes()
# edges = graph.edges()
#
# # Визуализация графа
# nx.draw(graph, with_labels=True, node_color='lightblue', edge_color='gray')
# plt.show()


# Пример 2:

# import igraph as ig
#
# # Создание пустого графа
# graph = ig.Graph()
#
# # Добавление вершин
# graph.add_vertices(4)
#
# # Добавление рёбер
# graph.add_edges([(0, 1), (1, 2), (2, 3), (3, 0)])
#
# # Получение списка вершин и рёбер
# nodes = graph.vs
# edges = graph.es
#
# # Визуализация графа
# layout = graph.layout("circle")
# ig.plot(graph, layout=layout, vertex_color='lightblue', edge_color='gray')




import hashlib
data = "Hello, World!"
hash_object = hashlib.sha256(data.encode())
hex_digest = hash_object.hexdigest()
print(hex_digest) # Выводит хеш-значение SHA-256



import mmh3
data = "Hello, World!"
hash_value = mmh3.hash(data)
print(hash_value)  # Выводит хеш-значение MurmurHash



# import pyhash
# data = "Hello, World!"
# crc32_hasher = pyhash.crc32()
# hash_value = crc32_hasher(data)
# print(hash_value)  # Выводит хеш-значение CRC32


class HashTable:
    def __init__(self):
        # Создаём пустой список, который будет использоваться в качестве основы хеш-таблицы
        self.table = [None] * 10 # Изначально устанавливаем размер таблицы — 10 элементов

    def _hash_function(self, key):
        # Хеш-функция преобразует ключ в индекс таблицы
        # Простейшая хеш-функция — остаток от деления на размер таблицы
        return hash(key) % len(self.table)

    def _get_index(self, key):
        # Получаем индекс элемента в таблице по ключу
        hash_value = self._hash_function(key)
        # Если по этому индексу ещё нет элемента или ключи совпадают, возвращаем индекс
        if self.table[hash_value] is None or self.table[hash_value][0] == key:
            return hash_value
        # В противном случае применяем метод открытой адресации для разрешения коллизий
        else:
            index = (hash_value + 1) % len(self.table) # Используем линейное пробирование
            while self.table[index] is not None and self.table[index][0] != key:
                index = (index + 1) % len(self.table)
            return index

    def insert(self, key, value):
        # Вставляем элемент в хеш-таблицу
        index = self._get_index(key)
        self.table[index] = (key, value)

    def search(self, key):
        # Ищем элемент в хеш-таблице по ключу
        index = self._get_index(key)
        if self.table[index] is not None and self.table[index][0] == key:
            return self.table[index][1] # Возвращаем значение элемента, если он найден
        else:
            return None # Возвращаем None, если элемент не найден

    def delete(self, key):
        # Удаляем элемент из хеш-таблицы по ключу
        index = self._get_index(key)
        if self.table[index] is not None and self.table[index][0] == key:
            self.table[index] = None # Просто удаляем элемент, присваивая ему значение None

# Создаём экземпляр хеш-таблицы
hash_table = HashTable()

# Вставляем элементы в хеш-таблицу
hash_table.insert("apple", 1)
hash_table.insert("banana", 2)
hash_table.insert("orange", 3)

# Ищем элементы в хеш-таблице
print(hash_table.search("apple")) # Вывод: 1
print(hash_table.search("banana")) # Вывод: 2
print(hash_table.search("grape")) # Вывод: None

# Удаляем элемент из хеш-таблицы
hash_table.delete("banana")

# Проверяем, что элемент удалён
print(hash_table.search("banana")) # Вывод: None



from pygtrie import Trie

# Создание экземпляра дерева префиксов
trie = Trie()

# Вставка элементов в дерево
trie["apple"] = 1
trie["banana"] = 2
trie["orange"] = 3

# Проверка наличия элементов
print("apple" in trie)  # Вывод: True
print("pear" in trie)  # Вывод: False

# Получение значения элемента
print(trie["banana"])  # Вывод: 2

# Удаление элемента
del trie["banana"]
print("banana" in trie)  # Вывод: False

# Поиск всех элементов с заданным префиксом
prefix_items = trie.items("a")
print(list(prefix_items)) # Вывод: [(('a', 'p', 'p', 'l', 'e'), 1)]

# Автодополнение
prefix = "app"
matching_suggestions = list(trie.iterkeys(prefix))
print(matching_suggestions)  # Вывод: [('a', 'p', 'p', 'l', 'e')]



import marisa_trie

# Создание экземпляра дерева префиксов
trie = marisa_trie.Trie(["apple", "banana", "orange"])

# Проверка наличия элементов
print("apple" in trie) # Вывод: True
print("pear" in trie) # Вывод: False

# Получение значения элемента
print(trie["banana"]) # Вывод: 1


# Поиск всех элементов с заданным префиксом
prefixes = trie.prefixes("app")
print(list(prefixes)) # Вывод: ['app', 'apple']

# Автодополнение
suggestions = trie.keys("app")
print(list(suggestions)) # Вывод: ['apple']