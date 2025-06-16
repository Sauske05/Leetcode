'''
In this design, we use a stack that stores a tuple of (value, current_minimum) at each push. 
This way, we can retrieve the minimum element in O(1) time at any point without needing to iterate over the stack.

Key Idea:
- Track the current minimum value along with each element in the stack.
- On each push, we compare the new value with the current minimum and push a tuple (val, min(val, current_min)).
- This ensures we can access both the top value and the current minimum in constant time.

--> Time Complexity

push(val): O(1) — appending a tuple to the list and computing min(val, current_min) is constant time.
pop(): O(1) — popping the last element is constant time.
top(): O(1) — accessing the top element is constant time.
getMin(): O(1) — accessing the stored minimum in the top element is constant time.

Total Time Complexity: O(1) per operation.

--> Space Complexity

Each element in the stack stores an extra integer (the min at that point), so space usage is doubled.

Let n be the number of elements pushed into the stack.

Total Space Complexity: O(n)
'''
class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        #self.stack.append(val) Not optimal as we have to use min function which is O(n) time but we can do it in O(1).
        if not self.stack:
            self.stack.append((val, val))
        else:
            min_val = self.stack[-1][-1]
            self.stack.append((val, min(min_val, val)))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]
        
    def getMin(self) -> int:
        return self.stack[-1][1]


        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()