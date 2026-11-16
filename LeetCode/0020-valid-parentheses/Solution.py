class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        st = []
        for i in range(len(s)):
            if s[i] == "(" or s[i] == "[" or s[i] == "{" :
                st.append(s[i])
            elif s[i] == ")": 
                if st and st[-1] == "(":
                    st.pop()
                else:
                    return False
            elif s[i] == "]":
                if st and st[-1] == '[':
                    st.pop()
                else:
                    return False
            elif  s[i] == "}":
                if st and st[-1] == '{':
                    st.pop()
                else:
                    return False
        if not st:
            return True
        else:
            return False