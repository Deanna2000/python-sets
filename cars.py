# Python exercise to learn about sets
showroom = set()
showroom = {"1992 Volvo 240", "2011 Nissan xTerra", "1970 International Scout", "1975 Nissan 280"}
print("This is what's in the showroom now ", showroom)
showroom.update({"1962 MG MGA", "1989 Toyota MR2"})
print("We just added 2 more vehicles to the showroom ", showroom)
showroom.discard("2011 Nissan xTerra")
print("We just sold the xTerra ", showroom)
junkyard = set()
junkyard.update({"1955 Clunker", "1961 Rustbucket", "1982 Gas-Guzzler"})
print("Our junkyard has the following vehicles: ", junkyard)
junkyard.update({"1968 POS"})
print("We just added another item to the junkyard ", junkyard)
showroom.union(junkyard)
print("We just bought out the local junkyard so now we have some 'economy' vehicles ", showroom)
