#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from functools import reduce

__author__ = 'Demi Yu'


# Given a collection of integers that might contain duplicates, S, return all possible subsets.
# Note: Elements in a subset must be in non-descending order. The solution set must not contain duplicate subsets.
# For example, If S = [1,2,2], a solution is:
# [ [2], [1], [1,2,2], [2,2], [1,2], [] ]


class Solution:
    def subsetsWithDup(self, S):
        S.sort()
        p = [[S[x] for x in range(len(S)) if i >> x & 1] for i in range(2 ** len(S))]
        func = lambda x, y: x if y in x else x + [y]
        p = reduce(func, [[], ] + p)
        return list(reversed(p))


# result = Solution().subsetsWithDup([1,2,2])
# print(result)

if __name__ == '__main__':
    result = Solution().subsetsWithDup([1, 2, 2])
    print(result)
 