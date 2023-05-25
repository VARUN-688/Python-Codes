#include<stdio.h>
#include<stdlib.h>
int a[100],i,n;
void creation();
void display();
int insertion(int ELEM,int POS);
int deletion(int POS);
int main()
{
    int ELEM,POS,valid,m;
    while(1)
    {
        printf("\n1.CREATE AN ARRAY\n");
        printf("2.DISPLAY AN ARRAY\n");
        printf("3.INSERT AN ELEMENT\n");
        printf("4.DELETE AN ELEMENT\n");
        printf("5.EXIT\n");
        printf("ENTER YOUR CHOICE\n");
        scanf("%d",&m);
    switch(m)
        {
         case 1:
            creation();
             break;
        case 2:
            printf("\nTHE ARRAY IS:\n");
            display();
            break;
        case 3:
            printf("\nENTER THE ELEMENT ");
            scanf("%d",&ELEM);
            printf("ENTER THE POSITION");
            scanf("%d",&POS);
            valid=insertion(ELEM,POS);
            if(valid)
            printf("SUCCESSFUL INSERTION");
            else
            printf("UNSUCCESSFUL INSERTION");
            break;
        case 4:
            printf("ENTER THE POSITION");
            scanf("%d",&POS);
            valid=deletion(POS);
            if(valid)
            printf("SUCCESSFUL DELETION");
            else
            printf("UNSUCCESSFUL DELETION");
            break;
        case 5:
            exit(0);
        
        }
    }
    return 0;
}

void creation()
{
    printf("ENTER THE NUMBER OF ELEMENTS\n");
    scanf("%d",&n);
    printf("ENTER THE ELEMENTS\n");
    for(i=0;i<n;++i)
    {
        printf("ENTER %dTH ELEMENT",i);
        scanf("%d",&a[i]);
    }
}
void display()
{
    for(i=0;i<n;++i)
    {
        printf("%d \n",a[i]);
    }
}
int insertion(int ELEM,int POS)
{
    if(POS>0&&POS<n+1)
    {
        n=n+1;
        for(i=n-1;i>POS-1;i--)
        {
            a[i]=a[i-1];
        }
        a[POS-1]=ELEM;
        return 1;
    }
    else return 0;
}
int deletion(int POS)
{
    if(POS>0&&POS<n)
    {
        for(i=POS;i<n;i++)
            a[i]=a[i+1];
            n=n-1;
        
        return 1;
    }
    else return 0;
}
