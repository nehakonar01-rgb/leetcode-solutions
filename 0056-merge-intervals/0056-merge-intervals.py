class Solution:
    def merge(self, intervals):

        # Sort intervals based on starting value
        intervals.sort(key=lambda x: x[0])

        result = []

        for interval in intervals:

            start = interval[0]
            end = interval[1]

            # If result is empty OR no overlap
            if not result or start > result[-1][1]:
                result.append([start, end])

            else:
                # Merge overlapping intervals
                result[-1][1] = max(result[-1][1], end)

        return result