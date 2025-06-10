from collections import Counter
from typing import List
import heapq
'''
For this approach, we create a hashmap with frequency as the values and key as the unique elements and get the top k elements
by running a for loop K times and appending it to the output

'''
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_dict = Counter(nums)
        output = []
        
        for _ in range(k):
            index = max(count_dict, key=count_dict.get)
            count_dict[index] = 0
            output.append(index)
        return output

'''
In the second solution, which is the optimal one, we can use min-heap or max-heap. 
If we use min-heap, we have a pop after the heap has k elements and only keep the last k biggest elements. 
If we use max-heap, we return the top k elements.
'''

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_dict = Counter(nums)
        #output = []

        heap_ = []

        for key, value in count_dict.items():
            heapq.heappush(heap_, (value, key))

            if len(heap_) > k:
                heapq.heappop(heap_)

        #At the end we will have something like:
        #heap = [(3, 1), (2, 4)]
        return [key for _, key in heap_]
    
###We can also use nlargest function that heap supports.
        
        