class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st=[]
        for i in tokens:
            if i in ("+","-","*","/"):
                r=st.pop()
                l=st.pop()

                if i == "+":
                    st.append(l + r)
                elif i == "-":
                    st.append(l - r)
                elif i == "*":
                    st.append(l * r)
                else:  # "/"
                    st.append(int(l / r))  # Truncate toward zero
            else:
                st.append(int(i))
        return st.pop() 
        