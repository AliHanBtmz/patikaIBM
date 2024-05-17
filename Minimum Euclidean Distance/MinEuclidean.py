points=[(4,5),(2,2),(8,5),(6,4),(3,8),(1,2),(8,6),(5,2)]
num=0
distance=[]

def euclideanDistance(point1,point2):
    temp=(point1[0]-point2[0])**2+(point1[1]-point2[1])**2
    return temp**0.5

for point1 in range (0,len(points)):

    num+=1
    for point2 in range (num,len(points)):
        distance.append(euclideanDistance(points[point1],points[point2]))

def minkowskiDistance(distance):
    min=10000000

    for i in range(len(distance)):
        if distance[i]<min:
            min=distance[i]
    return min

print(minkowskiDistance(distance))