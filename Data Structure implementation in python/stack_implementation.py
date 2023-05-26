class Stack:
    def __init__(self):
        self.stk=[]
        self.top = 0
    def push(self,elm:int):
        if self.top<5:
            self.top += 1
            print(self.top)
            self.stk.insert(0,elm)

        else:
            print('stack is full')
    def pop(self):
        if self.top==0:
            return 'stack is empty'
        else:
            self.top-=1
            return self.stk.pop(0)
    def display(self):
        if self.top==0:
            print('Stack is empty')
        print(self.stk)

if __name__=='__main__':
    objects=[]
    ch=0
    while ch!=5:
        print('1.CREATE\n2.PUSH\n3.POP\n4.DISPLAY\n5.EXIT')
        ch=int(input('enter your choice'))
        if ch==1:
            a=Stack()
            objects.append(a)
            print('Stack created successfully')
        elif ch==2:
            a=objects[-1]
            a.push(int(input('enter element to push')))
        elif ch==3:
            a=objects[-1]
            print(a.pop())
        elif ch==4:
            a=objects[-1]
            a.display()
        else:
            exit(0)
