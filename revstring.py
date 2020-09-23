from stack import Stack

def reverseString(st, input_str):

    for i in range(len(input_str)):
        st.push(input_str[i])
    
    rev = ''
    while not st.isEmpty():
        rev += st.remove()

    return rev



st = Stack()
input_str = 'Hello'
print(reverseString(st, input_str))
