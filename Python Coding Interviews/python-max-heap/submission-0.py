import heapq
from typing import List


from typing import List
import heapq

def get_reverse_sorted(nums: List[int]) -> List[int]:
    """
    Returns the list of integers in reverse sorted (descending) order
    using a max-heap (built on top of Python's min-heap via negation).
    """
    if not nums:
        return []
    
    # Build max-heap by pushing negated values (heapq is min-heap)
    heap = []
    for num in nums:
        heapq.heappush(heap, -num)
    
    # Extract elements in descending order
    result = []
    while heap:
        result.append(-heapq.heappop(heap))
    
    return result





# do not modify below this line
print(get_reverse_sorted([1, 2, 3]))
print(get_reverse_sorted([5, 6, 4, 2, 7, 3, 1]))
print(get_reverse_sorted([5, 6, -4, 2, 4, 7, -3, -1]))
