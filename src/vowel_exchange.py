class Solution:
    def vowel_exchange(self, s: str) -> str:
        vowels = set(["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"])

        if not s:
            return ""

        list_s = list(s)
        left, right = 0, len(s) - 1

        while left < right:
            if list_s[left] not in vowels:
                left += 1
            elif list_s[right] not in vowels:
                right -= 1
            else:
                list_s[right], list_s[left] = list_s[left], list_s[right]
                left += 1
                right -= 1

        return "".join(list_s)
