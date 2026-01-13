class Solution:
    def palindrome_checker(self, s: str) -> bool:
        if not s:
            return True

        list_s = []
        for i in s:
            if i.isalnum():
                list_s.append(i.lower())

        original_s_list = list_s[:]

        left, right = 0, len(list_s) - 1
        print(f"list_s is {list_s}")

        while left < right:
            list_s[left], list_s[right] = list_s[right], list_s[left]
            left += 1
            right -= 1

        return list_s == original_s_list
