# Example 1:

# Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
# Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].
# Example 2:

# Input: intervals = [[1,4],[4,5]]
# Output: [[1,5]]
# Explanation: Intervals [1,4] and [4,5] are considered overlapping.

from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """sort by the start of intervals, then traverse to check overlap"""
        if intervals == None:
            return None
        if len(intervals) < 2:
            return intervals[0]
        # sort the intervals by the start of intervals
        sortedintervals = self.sort(intervals)
        # initialize the result
        mergedintervals = [sortedintervals[0]]
        # traverse 
        for itv in sortedintervals[1:]:
            # end of the merged interval is smaller than the start of next interval
            if mergedintervals[-1][1] < itv[0]:
                mergedintervals.append(itv)
            # else check the overlap
            else:
                # if extended
                if mergedintervals[-1][1] < itv[1]:
                    mergedintervals[-1][1] = itv[1]

        return mergedintervals

    
    def sort(self, intervals: List[List[int]]) -> List[List[int]]:
        """merge sort"""
        if intervals == None:
            return intervals
        # looking for the middle point
        mid = len(intervals)//2
        # sort by recursion
        left_sorted = self.sort(intervals[:mid])
        right_sorted = self.sort(intervals[mid+1:])
        # merge sorted list
        sortedlist = self. mergeSorted(left_sorted, right_sorted)

        return sortedlist

    def mergeSorted(self, left, right):
        
        result = []
        if left == None:
            return right
        if right == None:
            return left
        if left[0][0] <= right[0][0]:
            result.append([left, self.mergeSorted(left[1:], right)])
        else:
            result.append([right, self.mergeSorted(left, right[1:])])
        
        return result
