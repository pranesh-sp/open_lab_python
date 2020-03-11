N = int(input())
while(N>0):
    string = list(input())
    size = len(string)
    string.reverse()
    stack = []
    while string:
        ch = string.pop()
        if ch == '{' or ch == '[' or ch == '(':
            stack.append(ch)
        elif ch == '}':
            if stack.pop() != '{':
                print("NO")
                break
        elif ch == ']':
            if stack.pop() != '[':
                print("NO")
                break
        elif ch == ')':
            if stack.pop() != '(':
                print("NO")
                break
        else:
            print("NO")
            break
        if not string:
            if(len(stack)==0):
             print("YES")
            else:print("NO")
    N-=1