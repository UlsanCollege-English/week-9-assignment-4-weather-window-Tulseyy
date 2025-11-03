"""
HW04 — Weather Window: Sliding Maximum

Implement sliding_window_max(nums, k) -> list
"""

def sliding_window_max(nums, k):
    # Handle edge cases
    if not nums or k <= 0:
        return []
    if k > len(nums):
        return [max(nums)]
    
    from heapq import heappush, heappop
    
    result = []
    heap = []  # Will store tuples of (-value, index)
    
    # Process first k elements
    for i in range(k):
        heappush(heap, (-nums[i], i))
    
    # Add first window's maximum
    result.append(-heap[0][0])
    
    # Process rest of the elements
    for i in range(k, len(nums)):
        # Remove elements outside current window
        while heap and heap[0][1] <= i - k:
            heappop(heap)
        
        # Add current element
        heappush(heap, (-nums[i], i))
        
        # Add current window's maximum
        result.append(-heap[0][0])
    
    return result
