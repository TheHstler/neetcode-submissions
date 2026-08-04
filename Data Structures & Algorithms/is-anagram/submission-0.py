class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)

        return Counter(s) == Counter(t)


        if len(s) != len(t):
            return False  # check that they are same length


        countS, countT = {},{}

        for i in range(len(s)):
            countS[s[i]] =  1 + countS.get(s[i], 0 ) #counting the occurences of each character in string S
            countT[t[i]] =  1 + countT.get(t[i], 0 )
        for c in countS:
            if countS[c] != countT.get(c, 0): #count= like the length but if the key doesnt exist in T then we use the get method
                return False

        return True