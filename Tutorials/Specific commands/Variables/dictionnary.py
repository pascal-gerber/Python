#dictionary

#d = {"test":"non", "value":"no"}
d = {8:4, "value":"no"}


print(d[8])

#add new value to dictionnary
d["noway"] = "newvalue"


#same thing
#will create error if empty
print(d["noway"])
#will return None if empry
print(d.get("noway"))
