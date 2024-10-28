def solution(arr):
    st = []
    
    for n in arr:
        if st and st[-1] != n:
            st.append(n)
        elif not st:
            st.append(n)
            
    return st