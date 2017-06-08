class Item(object):

    def __init__(self, key, value, prev=None, next=None):
        self.key = key
        self.value = value
        self.next = next
        self.prev = prev

    def get_key(self):
        return self.key

    def get_value(self):
        return self.value

    def put_next(self, next):
        self.next = next

    def put_prev(self, prev):
        self.prev = prev

    def get_next(self):
        return self.next

    def get_prev(self):
        return self.prev


class Cache(object):
    def __init__(self, capacity):
        self.capacity = capacity
        self.first = None
        self.last = None
        self.keys = []
        self.items = {}

    def get(self, key, num=1):
        if key not in self.items: return "not value"
        return self.items[key].get_value()

    def put(self, key, value):
        if len(self.items) == 0:
            new = Item(key, value)
            self.items[key] = new
            self.first = new
            self.last = new
            return

        if key in self.items:
            if self.first.get_key == key: return

            new = Item(key, value)
            print(new)
            print(type(new))
            prev = self.items[key].get_prev
            print(prev)
            print(type(prev))
            print(Item.get_key(prev))
            print(prev.get_value(prev))
            next = self.items[key].get_next
            prev.put_next(next)
        elif len(self.items) >= self.capacity:
            del items[self.last.get_key()]
            self.last = self.last.get_prev()

        new = Item(key, value, None, self.first)
        self.first.put_prev = new
        self.first = new
        self.items[key] = new
        print(self.items[key].get_prev)
        print(self.items[key])


    def remove(self, key):
        if key in self.items:
             next = self.items[key].get_next
             prev = self.items[key].get_prev
             prev.put_next(next)
             del items[key]
        else:
            print("not key")


if __name__ == '__main__':
    cache = Cache(3)
    cache.put("key", "value")
    cache.put("key2", "value2")
    cache.put("key3", "value3")
    #cache.remove("key")
    cache.put("key", "new value")
    
    print(cache.get("key"))
    print(cache.get("key2"))
    print(cache.get("key3"))
    print(cache.get("hoge"))
