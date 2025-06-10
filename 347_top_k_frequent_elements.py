from collections import Counter
from typing import List
import heapq
'''
For this approach, we create a hashmap with frequency as the values and key as the unique elements and get the top k elements
by running a for loop K times and appending it to the output

--> Time Complexity

Counter Creation: Building the hash map with Counter(nums) takes O(n), where n is the length of nums.

Max Search Loop: The loop runs k times. In each iteration:

Finding the max element in the hash map via max(count_dict, key=count_dict.get) scans all entries in count_dict. If there are m unique elements (where m <= n), this takes O(m) per iteration.

Total for the loop: O(k * m).

Total Time Complexity: O(n) + O(k * m) = O(n + k * m).

In the worst case, if m is close to n (many unique elements), and k is large, this can be slow, e.g., O(n^2) if k approaches n.

--> Space Complexity

Hash Map: count_dict stores frequency for each unique element, taking O(m) space, where m is the number of unique elements.

Output List: The output list stores k elements, taking O(k) space.

Total Space Complexity: O(m) + O(k) = O(m).
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

--> Time Complexity

Counter Creation: Building count_dict takes O(n), where n is the length of nums.

Heap Operations:

Iterate over count_dict with m unique elements.

Push each tuple (value, key) to the heap: O(log h), where h is the current heap size.

If heap size exceeds k, pop the smallest: O(log h).

At most, the heap size is k + 1, so each push/pop is O(log k).

Total for m elements: O(m * log k).

Result Extraction: The list comprehension [key for _, key in heap_] processes k elements, taking O(k).

Total Time Complexity: O(n) + O(m * log k) + O(k) = O(n + m * log k).

Since m <= n and k <= m, this is generally more efficient than Approach 1, especially for large n and small k.

--> Space Complexity

Hash Map: count_dict takes O(m) space for m unique elements.

Heap: The heap stores at most k elements (after popping), taking O(k) space.

Output: The result list takes O(k) space.

Total Space Complexity: O(m) + O(k) = O(m).

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
        
        