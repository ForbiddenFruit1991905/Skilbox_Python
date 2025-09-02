# Кэширование запросов
# Вы разрабатываете программу для кэширования запросов к внешнему API. Часто повторяющиеся запросы
# занимают много времени, поэтому вы решаете создать класс LRU Cache (Least Recently Used Cache),
# который будет хранить ограниченное количество запросов и автоматически удалять самые старые при
# достижении лимита. Это позволит значительно ускорить повторяющиеся запросы, так как данные будут
# браться из кэша, а не отправляться повторно.
# Задача
# Создайте класс LRU Cache, который хранит ограниченное количество объектов и, при превышении лимита,
# удаляет самые давние (самые старые) использованные элементы.
# Реализуйте методы добавления и извлечения элементов с использованием декораторов property и setter.
# Советы
# Не забывайте обновлять порядок использованных элементов. В итоге должны удаляться давно использованные
# элементы, а не давно добавленные, так как давно добавленный элемент может быть популярен, и его удаление
# не поможет ускорить новые запросы.
# Ожидаемый вывод в консоли:
# LRU Cache:
# key1 : value1
# key2 : value2
# key3 : value3
# value2
# LRU Cache:
# key3 : value3
# key2 : value2
# key4 : value4


class LRUCache:
    def __init__(self, volume):
        self.volume = volume
        self.dict_cache = {}
        self.order = []

    @property
    def cache(self): # этот метод должен возвращать самый старый элемент
        element_by_key_to_remove = self.order[0]
        result = (element_by_key_to_remove, self.dict_cache[element_by_key_to_remove])
        return result

    @cache.setter
    def cache(self, new_elem): # этот метод должен добавлять новый элемент
        key, value = new_elem
        if key in self.dict_cache:
            self.order.remove(key)
            self.order.append(key)
        else:
            self.dict_cache[key] = value
            self.order.append(key)

        if len(self.order) > self.volume:
            oldest_key, oldest_value = self.cache
            self.order.pop(0)
            self.dict_cache.pop(oldest_key)

    def get(self, key): # Перемещаем ключ в конец списка order
        if key in self.dict_cache:
            self.order.remove(key)
            self.order.append(key)
            return self.dict_cache[key]
        else:
            return None

    def print_cache(self):
        print("LRU Cache:")
        for key in self.order:
            print(key, ":", self.dict_cache[key])


cache = LRUCache(3)
cache.cache = ("key1", "value1")
cache.cache = ("key2", "value2")
cache.cache = ("key3", "value3")
cache.print_cache()
print(cache.get("key2"))
cache.cache = ("key4", "value4")
cache.cache = ("key4", "value4")
cache.print_cache()

# Пример:
# # Создаём экземпляр класса LRU Cache с capacity = 3
# cache = LRUCache(3)
# # Добавляем элементы в кэш
# cache.cache = ("key1", "value1")
# cache.cache = ("key2", "value2")
# cache.cache = ("key3", "value3")
# # # Выводим текущий кэш
# cache.print_cache() # key1 : value1, key2 : value2, key3 : value3
# # Получаем значение по ключу
# print(cache.get("key2")) # value2
# # Добавляем новый элемент, превышающий лимит capacity
# cache.cache = ("key4", "value4")
# # Выводим обновлённый кэш
# cache.print_cache() # key2 : value2, key3 : value3, key4 : value4