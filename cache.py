class Item(object):
    def __init__(self, key, value, prev=None, next=None):
        self.key = key
        self.value = value
        self.next = next
        self.prev = prev


class Cache(object):
    def __init__(self, capacity):
        self.capacity = capacity
        self.first = None
        self.last = None
        self.items = {}

    def get(self, key):
        if key not in self.items: return "not value"
        return self.items[key].value

    def put(self, key, value):
        if len(self.items) == 0:
            new = Item(key, value)
            self.items[key] = new
            self.first = new
            self.last = new
            return

        if key in self.items:
            if self.first.key == key: return

            new = Item(key, value)
            prev = self.items[key].prev
            next = self.items[key].next
            prev.next = next
        elif len(self.items) >= self.capacity:
            del self.items[self.last.key]
            self.last = self.last.prev

        new = Item(key, value, None, self.first)
        self.first.prev = new
        self.first = new
        self.items[key] = new

    def remove(self, key):
        if key in self.items:
             next = self.items[key].next
             prev = self.items[key].prev
             prev.next = next
             del self.items[key]
        else:
            print("not key")


if __name__ == '__main__':
    cache = Cache(3)
    cache.put("URL1", "content1")
    cache.put("URL2", "content2")
    cache.put("URL3", "content3")
    cache.put("URL4", "content4")
    cache.remove("URL2")
    cache.put("URL3", "new content")
    
    print(cache.get("URL1"))
    print(cache.get("URL2"))
    print(cache.get("URL3"))
    print(cache.get("URL4"))
    print(cache.get("hoge"))
