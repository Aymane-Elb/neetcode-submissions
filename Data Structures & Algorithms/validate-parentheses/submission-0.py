class Solution:
    def isValid(self, s: str) -> bool:
        st= deque()
        for i in s:
            if i=='('or i=='[' or i=='{':
                st.append(i)
            else:
                if len(st)==0:
                    return False
                top = st.pop()
                if  (i ==')' and top =='(') or (i ==']' and top =='[') or (i =='}' and top =='{'):
                     continue
                else:
                     return False
        return len(st)==0
    