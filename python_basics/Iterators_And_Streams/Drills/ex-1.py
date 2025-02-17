class SimpleIterator:
    def __init__(self):
        self.current = 1
        self.end = 10

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= self.end:
            num = self.current
            self.current += 1
            return num
        else:
            raise StopIteration  
        

iterator = SimpleIterator()
for number in iterator:
    print(number)
    
    
    
# Explanation:

# __iter__() returns the iterator object itself.

# __next__() returns the next value in the sequence. When there are no more items, it raises StopIteration.