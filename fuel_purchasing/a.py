s='BJAQFDTIDGHATMRBJA'
print "->".join([s[k-3:k] for k in range(1,len(s)) if k%3==0 ])