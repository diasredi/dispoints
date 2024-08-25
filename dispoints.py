
#function that chooses a number of dispersed points
def choose_dispersed_points(points, amount, distance_function):
    #if the number of points is equal to the amount required, return all points
    if len(points)<=amount:
        return points


    #greedy algorithm to select dispersed points :
    # 1) select n points    
    # 2) for each p in points replace it with the nearest selected point
    # 3) if the sum of the distances is greater replace for the selected
    selected = points[:amount]


    for p in points[amount:]:
        
        #distances beetween p and selected
        distances = [distance_function(p,ps) for ps in selected]
        #nearest point from p
        nearest_point = selected[ distances.index(min(distances)) ]

        #remove nearest point from selected to calculate the distances correctly
        selected.remove(nearest_point)


        #add to selected the landmark that maximises the distances with other selected points
        if sum([distance_function(p,ps) for ps in selected]) > sum([distance_function(nearest_point,ps) for ps in selected]):
            selected.append(p)
        else :
            selected.append(nearest_point)

    return selected
