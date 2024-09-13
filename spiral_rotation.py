import matplotlib.pyplot as plt
fig,ax=plt.subplots(4,4)
def display(i, j, t,c):
    ax[i, j].bar(1,1)  # Use a simple plot with x and y values
    ax[i, j].set_title(f"Plot {i},{j}")
    fig.savefig(f"{c}.png")

arr=[[1,2,3,4],[12,13,14,5],[11,16,15,6],[10,9,8,7]]
l=len(arr)
x=[0,3]
y=[0,3]
end_points=[[ x[0],y[1] ] ,
            [ x[1],y[1] ] ,
            [x[1],y[0]],
            [x[0],y[0]]
           ]

x_path=[0,1,0,-1]
y_path=[1,0,-1,0]
count=0
path=0
i=j=0
x_inc=x_path[0]
y_inc=y_path[0]
while count<l**2:

    display(i,j,arr[i][j],count)
    if [i,j]==end_points[0] and path==0:
        path=(path+1)%l
        end_points[0][0]+=1
        end_points[-1][0]+=1
        
    elif [i,j]==end_points[1] and path==1:
        path=(path+1)%l
        end_points[1][1]-=1
        end_points[0][1]-=1
    elif [i,j]==end_points[2] and path==2:
        path=(path+1)%l
        end_points[2][0]-=1
        end_points[2-1][0]-=1
    elif [i,j]==end_points[3] and path==3:
        path=(path+1)%l
        end_points[3][1]+=1
        end_points[2][1]+=1
    x_inc=x_path[path]
    y_inc=y_path[path]
    i+=x_inc
    j+=y_inc
    count+=1
