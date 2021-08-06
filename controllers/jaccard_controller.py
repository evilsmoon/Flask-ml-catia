def jaccard(v1,v2):
    matrizjacc = []
    for valor in v2:
        a=set(v1)
        b=set(valor)
        union=a.union(b)
        inter=a.intersection(b)
            
        if len(union)==0:
            if len(inter)==0:
                return -1

        similitud=len(inter)/len(union)
        matrizjacc.append(similitud)
    print("jaccard:")
    return matrizjacc