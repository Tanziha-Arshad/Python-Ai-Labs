from queue import Queue
adj_list={
"A":["B","D"],
"B":["A","C"],
"C":["B"],
"D":["A","E","F"],
"E":["D","F","G"],
"F":["D","E","H"],
"G":["E","H"],
"H":["G","F"]
}


#bfs code
visited={}
level={}               #distance dictionary
parent={}
bfs_traversal_output=[]
queue=Queue()



for node in adj_list.keys():
    visited[node]=False
    parent[node]=None
    level[node]=-1      #inf


print(visited)
print(level)  
print(parent) 
 














