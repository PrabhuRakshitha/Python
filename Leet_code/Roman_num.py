class Solution(object):
    def romanToInt(self, s):
        rom_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        num = 0
        for i in range(len(s)-1):
            if rom_dict[s[i]] >= rom_dict[s[i+1]]:
                num = num + rom_dict[s[i]]
            else:
                num = num - rom_dict[s[i]]

        num = num+rom_dict[s[-1]]
        return num


def main():
    a = Solution()
    print(a.romanToInt(input("enter Roman number :")))


main()