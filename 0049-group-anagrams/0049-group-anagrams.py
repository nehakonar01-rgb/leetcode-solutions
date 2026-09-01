class Solution:
    def groupAnagrams(self, strs):

        groups = {}

        for s in strs:

            # Sort the characters
            key = ''.join(sorted(s))

            # If key doesn't exist, create a list
            if key not in groups:
                groups[key] = []

            # Add the string to its group
            groups[key].append(s)

        return list(groups.values())