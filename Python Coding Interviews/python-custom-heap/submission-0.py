import heapq
from typing import List


from typing import List
import heapq

def get_reverse_sorted(nums: List[int]) -> List[int]:
    """
    Returns the list of integers in reverse sorted (descending) order
    using a max-heap simulated with tuples.
    """
    if not nums:
        return []
    
    # Build max-heap using tuples: (-value, value)
    # The negative value is used for priority ordering
    heap = []
    for num in nums:
        heapq.heappush(heap, (-num, num))
    
    # Extract elements in descending order
    result = []
    while heap:
        _, original_value = heapq.heappop(heap)  # ignore the negated value
        result.append(original_value)
    
    return result



# do not modify below this line
print(get_reverse_sorted([1, 2, 3]))
print(get_reverse_sorted([5, 6, 4, 2, 7, 3, 1]))
print(get_reverse_sorted([5, 6, -4, 2, 4, 7, -3, -1]))
