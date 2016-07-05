from atlas import airportatlas
def main():
	source=raw_input("Enter source airport name:  ")
	four_airports=raw_input("Enter four airports names(separated by coma): ")
	four_airports_lists=four_airports.split(',')
	airport=airportatlas('airport.csv')
	economic_pat,rate_eur=airport.greatcirledist(source=source,airports_4=four_airports_lists)
	print "Value in EUR: ",rate_eur
	print "->".join([economic_pat[k-3:k] for k in range(1,len(economic_pat)) if k%3==0 ])+"->"+economic_pat[-3:]

main()