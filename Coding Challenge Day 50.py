#Create a program that finds the intersection and union of two sets

def like_sets():
    set1 = ({"pineapple", "Yes", 10, 23, "23"})
    set2 = ({23, "10", 10, "seven", 40, 24})

    set_intersection = set1.intersection(set2)
    set_union = set1.union(set2)

    print(f" The intersection of the sets is: {set_intersection}\n The \
union of the sets is: \n{set_union}")

like_sets()
