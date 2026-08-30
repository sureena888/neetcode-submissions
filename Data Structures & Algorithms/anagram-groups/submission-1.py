class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = {}

        for word in strs:
            count = [0]*26
            for letter in word:
                count[ord(letter)-ord("a")] += 1
            if tuple(count) in anagram_map:
                anagram_map[tuple(count)].append(word)
            else:
                anagram_map[tuple(count)] = [word]
        return list(anagram_map.values())