# Initial treasures on each island
golden_island = {"gold coins", "ruby", "emerald", "map"}
silver_island = {"silver coins", "emerald", "pearl", "map"}


print("golden_island_treasures:",golden_island)
print("silver_island_treasure:",silver_island)

# Union
combine=golden_island.union(silver_island)
print(combine)

# Intersection
common=golden_island.intersection(silver_island)
print(common)

# Difference
# unique=golden_island.difference(silver_island)
# print(unique)

unique1=silver_island.difference(golden_island)
print(unique1)

# Symmetric_difference
unique2=golden_island.symmetric_difference(silver_island)
print(unique2)