from collections import defaultdict
'''
This solution implements a **Time-Based Key-Value Store**.

For each key, we store a list of (value, timestamp) pairs sorted by timestamp.
- `set()` stores the value with its timestamp.
- `get()` retrieves the value with the **largest timestamp ≤ the given timestamp**.

Since timestamps are strictly increasing for each key, binary search can be used efficiently to perform the get operation.

--> Time Complexity

1. set(key, value, timestamp)
- Appending to the list takes O(1) time since we maintain values in order.
- Total Time Complexity: **O(1)**

2. get(key, timestamp)
- Performs binary search over the list of (value, timestamp) pairs.
- Let n = number of values stored for `key`.
- Binary Search: O(log n)
- Total Time Complexity: **O(log n)**

--> Space Complexity

- A dictionary where each key maps to a list of (value, timestamp) pairs.
- Let m = number of unique keys, and total number of set calls be N.
- Space used: O(N), where N is the total number of key-value pairs stored.

This implementation ensures fast retrieval and is optimal for time-based queries.
'''
class TimeMap:

    def __init__(self):
        self.store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = [(value, timestamp)]
        else:
            self.store[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        values = self.store.get(key, [])

        if not values:
            return ''
        
        lp = 0
        rp = len(values) - 1
        res = ''
        while lp <= rp:
            mid = (lp + rp) // 2
            if values[mid][1] > timestamp:
                rp = mid - 1
            else:
                res = values[mid][0]
                lp = mid + 1
        return res
        
        




# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)