import time
import hashlib


class Block:
    def __init__(self, timestamp, data, previous_hash):
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash()

    def calc_hash(self):
        sha = hashlib.sha256()
        hash_str = "We are going to encode this string of data!".encode('utf-8')
        sha.update(hash_str)

        return sha.hexdigest()
    
class LL:
    
    def __init__(self):
        self.head = None
        self.last = None
        
    def append(self, timestamp, data):
        if self.head is None:
            self.head = Block(timestamp, data, 0)
            self.last = self.head
            
        else:
            last_temp = self.last
            self.last = Block(timestamp, data, 0)
            self.last.previous_hash = last_temp
    
    def get_block(self, data):
        if self.head == None:
            return False

        block = self.head

        while block:
            if block.data == data:
                return (block.data, block.timestamp, block.hash)
            else:
                return False

            


def generacte_info(count):
    return 'generated information number #:'+str(count)


print('=====================================================================')

LL_block = LL()

for count in range(3):
    block = Block(time.time(), generacte_info(count) , count)
    LL_block.append(block.timestamp, block.data)
    
    print(block.data)
    print(block.hash)
    print('Timestamp: ' + str(block.timestamp))
    print('Previous hash number: '+str(block.previous_hash))

    

try:
    print(LL_block.head.data)
    print(LL_block.head.timestamp)
    print(LL_block.last.data)
    print(LL_block.last.previous_hash.data)
except:
    print('Erorr, check your data')

print('=====================================================================')

LL_block = LL()


for count in range(0):
    block = Block(time.time(), generacte_info(count) , count)
    LL_block.append(block.timestamp, block.data)
    
    print(block.data)
    print(block.hash)
    print('Timestamp: ' + str(block.timestamp))
    print('Previous hash number: '+str(block.previous_hash))

    

try:
    print(LL_block.head.data)
    print(LL_block.head.timestamp)
    print(LL_block.last.data)
    print(LL_block.last.previous_hash.data)
except:
    print('Erorr, check your data')


print('=====================================================================')

LL_block = LL()


for count in range(1):
    block = Block(time.time(), generacte_info(count) , count)
    LL_block.append(block.timestamp, block.data)
    
    print(block.data)
    print(block.hash)
    print('Timestamp: ' + str(block.timestamp))
    print('Previous hash number: '+str(block.previous_hash))
    

try:
    print(LL_block.head.data)
    print(LL_block.head.timestamp)
    print(LL_block.last.data)
    print(LL_block.previous_hash.data)
except:
    print('Erorr, check your data')

