# Elan Shetreat-Klein, 5/25/21

import math
import matplotlib.pyplot as plt

# Calculates angle between segments 12 and 23, P2 is the vertex
def calc_angle(p1, p2, p3, degrees=True):
    
    # calculate lengths
    d12 = math.dist(p1, p2)
    d23 = math.dist(p2, p3)
    d13 = math.dist(p1, p3)

    result = math.acos((d12**2 + d23**2 - d13**2) / (2 * d12 * d23))

    if not degrees:
        return result

    return math.degrees(result)

# Plots a line segment between two points
def plot_line(p1, p2):
    plt.plot([p1[0], p2[0]], [p1[1], p2[1]], 'ro-')

# Plots a body_25 given an array of points
def plot_body(data):
    connections = [(8,9,11), (11,22,23), (11,24,24), (8,12,14), (14,19,20), (14,21,21), (0,1,4), (1,5,7), (1,8,8), (0,15,15), (15,17,17), (0,16,16), (16,18,18)]
    for i in range(len(connections)):
        subline = connections[i]
        plot_line((data[subline[0]][0], data[subline[0]][1]), (data[subline[1]][0], data[subline[1]][1]))
        for j in range(subline[1], subline[2]):
            plot_line((data[j][0], data[j][1]), (data[j+1][0], data[j+1][1]))
    plt.gca().invert_yaxis()

# Plots a hand given an array of points
def plot_hand(data):
    connections = [(0,17,20), (0,13,16), (0,9,12), (0,5,8), (0,1,4)]
    for i in range(len(connections)):
        subline = connections[i]
        plot_line((data[subline[0]][0], data[subline[0]][1]), (data[subline[1]][0], data[subline[1]][1]))
        for j in range(subline[1], subline[2]):
            plot_line((data[j][0], data[j][1]), (data[j+1][0], data[j+1][1]))
    plt.gca().invert_yaxis()


