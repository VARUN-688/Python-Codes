a=input("enter the infix expression->")
op={'(':0,'+':1,'-':1,'*':2,'/':2,'^':3}
class stack:
    def __init__(self):
        self.top=-1
        self.st=[]
    def push(self,x):
        self.top+=1
        self.st.append(x)
    def pop(self):
        self.top-=1
        return self.st.pop()
    def get(self):
        return self.st[self.top]
stk=stack()
result=[]
stk=stack()
for i in a:
    if i.isalpha():
        result.append(i)
    else:
        if stk.top==-1 or i=='(':
            stk.push(i)
        elif i==')':
            while stk.get()!='(':
                result.append(stk.pop())
            if stk.get()=='(':
                stk.pop()
        else:
            p1=op.get(i)
            p2=op.get(stk.get())
            if p1>p2:
                stk.push(i)
            elif p2>p1:
                while p1<=p2 and stk.top!=0:
                    result.append(stk.pop())
                    p2=op.get(stk.get())
                    result.append(stk.pop())
                    stk.push(i)
            elif p1==p2 and i!='^':
                result.append(stk.pop())
                stk.push(i)
            elif p1==p2 and i=='^':
                stk.push(i)
while stk.top!=-1:
    result.append(stk.pop())
print("the postfix expression is->","".join(result))
#k+l-m*n+(o^p)*w/u/v*t+q
