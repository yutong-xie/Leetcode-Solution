#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
    Copyright 2020, Yutong Xie, UIUC.
    Using bfs to solve word ladder problem. 
 '''

class Solution(object):
    import collections
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        if endWord not in wordList:
            return 0

        L = len(beginWord)

        comb_word = collections.defaultdict(list)

        for w in wordList:
            for i in range(L):
                key = w[:i]+ "*" + w[i+1:]
                comb_word[key].append(w)

        q = collections.deque()

        q.append((beginWord, 1))

        visited = set()

        while q:
            word, level = q.popleft()
            for i in range(L):
                mid_word = word[:i]+ "*" + word[i+1:]

                for w in comb_word[mid_word]:
                    if w == endWord:
                        return level + 1
                    if w not in visited:
                        q.append((w, level+1))
                        visited.add(w)

        return 0
