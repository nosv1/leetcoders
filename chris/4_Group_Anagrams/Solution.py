class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        # use two dictionaries to store the count of each character in s and t
        # loop through s and t and populate the dictionaries
        # loop through the dictionaries and compare the counts
        # if the counts are not equal, return False
        # if the loop completes, return True

        
        s_chars: dict[str, int] = {}
        t_chars: dict[str, int] = {}
        for i in range(len(s)):
            s_char = s[i]
            t_char = t[i]

            if s_char not in s_chars:
                s_chars[s_char] = 1
            else:
                s_chars[s_char] += 1

            if t_char not in t_chars:
                t_chars[t_char] = 1
            else:
                t_chars[t_char] += 1

        for char, count in s_chars.items():
            if char not in t_chars:
                return False

            if t_chars[char] != count:
                return False

        return True
    
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams: list[list[str]] = []

        if not strs:
            return anagrams
        
        anagrams.append([strs[0]])
        del strs[0]
        
        i = len(strs) - 1
        while strs:
            _str = strs[-1]
            group_found = False
            for j in range(len(anagrams)):
                if self.isAnagram(_str, anagrams[j][0]):
                    anagrams[j].append(_str)
                    group_found = True
                    break
            if not group_found:
                anagrams.append([_str])
            del strs[-1]
            i -= 1

        return anagrams