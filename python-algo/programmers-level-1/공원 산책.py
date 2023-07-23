def solution(park, routes):
    answer = []
    w, h = len(park[0]), len(park)
    x, y = 0, 0
#     ["SOO",
#      "OOO",
#      "OOO"]
    
#     ["OSO",
#      "OOO",
#      "OXO",
#      "OOO"]

    for i in range(h):
        for j in range(w):
            if park[i][j] == "S":
                x, y = i, j
    

    # 0, 1
    for i in routes:
        di = i.split(" ")[0]
        num = i.split(" ")[1]        
        nx, ny = x, y
        
        if di == "E":
            for i in range(1, int(num)+1):
                if ny + i >= w or park[nx][ny + i] == "X":
                    break
                else:
                    y = ny + i
        elif di == "W":
            for i in range(1, int(num)+1):
                if ny - i < 0 or park[nx][ny-i] == "X":
                    break
                else:
                    y = ny - i
        
        elif di == "S":
            for i in range(1, int(num)+1):
                if nx + i >= h or park[nx+i][ny] == "X":
                    break
                else:
                    x = nx+i 
                    
        elif di == "N":
            for i in range(1, int(num)+1):
                if nx - i < 0 or park[nx-i][ny] == "X":
                    break
                else:
                    x = nx+i 
                    
        
        
            
    print(x, y)
    
solution(["OSO","OOO","OXO","OOO"], ["E 2","S 3","W 1"])