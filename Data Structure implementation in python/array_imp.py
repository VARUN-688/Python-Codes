import numpy as np
class Array:
    def __init__(self,size=1,arr=[]):
        if len(arr)!=0:
            self.array=np.array(arr)
        else:
            self.array=np.zeros(size)
        print(f'Your array is ={self.array}')
    def sort(self,ascending=True):
        if ascending:
         self.array=self.array.sort()
        else:
            self.array=self.array.sort()
            self.array=self.array[-1::-1]

    def display(self):
        print(f'Your array is ={self.array}')
    def sum(self):
        print(self.array.sum())
    def mean(self):
        print(self.array.mean())
    def product(self):
        print(self.array.prod())
    def search(self):
        print(np.array==int(input('enter the element to search')))
    def __str__(self):
        return "'You can use the following functions:-" \
               "1.Search" \
               "2.Sum" \
               "3.Product" \
               "4.Display" \
               "5.Sort(give ascending=False if you want it descending order)'"

if __name__=='__main__':
    n=0
    if (input('enter a random number if you want to give size of array')).isdigit():
        n=int(input('enter the size'))

    l=np.zeros(n)
    if input("enter 'yes' if you want to give to initialize an array").upper()=='YES':
        for i in range(n):
            l[i]=int(input('enter the array element'))
        if n:
            arr=Array(n,l)
        else:
            arr=Array(l)
    else:
        if n:
            arr=Array(n)
        else:
            arr=Array(n)
