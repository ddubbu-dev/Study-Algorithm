def solution(sentence):
    st = []
    
    for s in sentence:
        if s == "(":
            st.append(s)
        else:
            if not st:
                return False
            st.pop()
            
    if st:
        return False
    return True