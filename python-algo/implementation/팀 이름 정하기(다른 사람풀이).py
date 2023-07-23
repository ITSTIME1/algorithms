def get_best_try(minsik_name, girl_names):
    scores = []
    for girl_name in girl_names:
        L = girl_name.count("L") + minsik_name.count("L")
        O = girl_name.count("O") + minsik_name.count("O")
        V = girl_name.count("V") + minsik_name.count("V")
        E = girl_name.count("E") + minsik_name.count("E")
        
        score = ((L+O)*(L+V)*(L+E)*(O+V)*(O+E)*(V+E)) % 100
        
        scores.append((score, girl_name))
       	print(scores)
        
    scores.sort(key=lambda x: (-x[0]))
    print(scores)
    return scores[0][1]

if __name__ == "__main__":
    girl_names = []
    minsik_name = input()
    for _ in range(int(input())):
        girl_name = input()
        girl_names.append(girl_name)
        
    print(get_best_try(minsik_name, girl_names))
