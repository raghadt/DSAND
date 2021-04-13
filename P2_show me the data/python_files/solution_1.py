from collections import deque

class LRU_Cache(object):

    def __init__(self, capacity):
        # Initialize class variables
        self.capacity = capacity
        self.value = {}
        self.order_ = deque()

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent. 
        if not key:
            return - 1
        
        return self.value.get(key, -1)

    def set(self, key, value):

        if self.capacity <=0:
            print("sorry, can't complete operation because of 0 capacity")
            return
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item. 
        
        if len(self.order_) >= self.capacity:
            val = self.order_.popleft()
            del self.value[val]
            
        self.order_.append(key)
        self.value[key] = value
         
            
our_cache = LRU_Cache(5)

our_cache.set(1, 1);
our_cache.set(2, 2);
our_cache.set(3, 3);
our_cache.set(4, 4);


print(our_cache.get(1))       # returns 1
print(our_cache.get(2))      # returns 2
print(our_cache.get(9))      # returns -1 because 9 is not present in the cache

our_cache.set(5, 5) 
our_cache.set(6, 6)

our_cache.get(3)      # returns -1 because the cache reached it's capacity and 3 was the least recently used entry

# ---- test 2 ---------
our_cache = LRU_Cache(2)

our_cache.set(1, 1);
our_cache.set(2, 2);
our_cache.set(1, 3);

print(our_cache.get(1))       # returns 3
print(our_cache.get(2))      # returns 2
print(our_cache.get(9))      # returns -1 because 9 is not present in the cache



# ---- test 3 ---------
our_cache = LRU_Cache(0)

our_cache.set(1, 1);

print(our_cache.get(1))       # returns 3
print(our_cache.get(2))      # returns 2
print(our_cache.get(9))      # returns -1 because 9 is not present in the cache
