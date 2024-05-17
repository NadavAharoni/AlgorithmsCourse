def main():
    names = ["shir", "shani","shir","roy","efraim","moshe","baruch","bracha"]

    size = 31
    hash_table : list[tuple[str,int]] = [("",0)] * size;
    for name in names:
        h = hash(name) % size
        t = hash_table[h]
        if t[0] == "":
            t : tuple[str,int] = (name, 0)
        if name != t[0]:
            print(F"colission! between {name} and {t[0]}")
            
        t=(name,t[1]+1)
        hash_table[h]=t
        print(h,name,t)