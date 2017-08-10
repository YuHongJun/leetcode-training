class Solution:
    # @param {int[]} A an integer array sorted in ascending order
    # @param {int} target an integer
    # @return {int} an integer
    def closestNumber(self, A, target):
        if not A:
            return -1
        start, end = 0, len(A) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            print(start,end,mid)
            if A[mid] == target:
                return mid
            elif A[mid] > target:
                end = mid
            else:
                start = mid
        if A[end] - target > target - A[start]:
            return start
        else:
            return end

if __name__ == '__main__':
    result = Solution().closestNumber([1, 4, 6], 5)
    print(result)