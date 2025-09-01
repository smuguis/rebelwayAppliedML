import pickle
import hou
import os
import time
node = hou.pwd()
geo = node.geometry()


file_path = r"D:\ML\rebelway\houdini\A_star\pickle\paths.pkl"

with open(file_path, 'rb') as f:
    data = pickle.load(f)

frame = int(hou.frame()) - 1
npc_count = len(data)

for i in range(1, npc_count+1):
    npc_name = f"npc_{i}"
    box_name = f"box{i}"
    path = data.get(npc_name, [])   
    if not path:
        continue
        
    id = min(frame, len(path)-1)
    row, col = path[id]
    
    node_path = f"/obj/geo1/{box_name}"
    box_node = hou.node(node_path)
    

    if box_node:
        box_node.parmTuple("t").set((col, 0, row))
