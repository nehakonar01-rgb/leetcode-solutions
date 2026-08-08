class Solution:
    def findSubstring(self, s, words):

        if not s or not words:
            return []

        wordLen = len(words[0])
        wordCount = len(words)
        totalLen = wordLen * wordCount

        # Frequency of words we need
        wordMap = {}

        for word in words:
            if word in wordMap:
                wordMap[word] += 1
            else:
                wordMap[word] = 1

        result = []

        # We need to try wordLen different starting positions
        for offset in range(wordLen):

            left = offset
            right = offset

            seen = {}
            count = 0

            while right + wordLen <= len(s):

                word = s[right:right + wordLen]
                right += wordLen

                # Word is not present in words
                if word not in wordMap:

                    seen = {}
                    count = 0
                    left = right
                    continue

                # Add word to current window
                if word in seen:
                    seen[word] += 1
                else:
                    seen[word] = 1

                count += 1

                # Too many occurrences of this word
                while seen[word] > wordMap[word]:

                    leftWord = s[left:left + wordLen]

                    seen[leftWord] -= 1
                    left += wordLen
                    count -= 1

                # We have exactly all words
                if count == wordCount:
                    result.append(left)

                    # Move window forward
                    leftWord = s[left:left + wordLen]

                    seen[leftWord] -= 1
                    left += wordLen
                    count -= 1

        return result