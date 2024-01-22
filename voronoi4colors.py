import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import Voronoi
# ボロノイ図の点の数
n = 40

def get_effective_polygons(polygons):
    return [polygon for polygon in polygons if -1 not in polygon and len(polygon) > 2]

def get_touching_polygons(polygons):
    touching_polygons = []
    for index0, vertices0 in enumerate(polygons):
        touching_polygon = []
        for index1, vertices1 in enumerate(polygons):
            if index0 != index1 and set(vertices0) & set(vertices1):
                touching_polygon.append(index1)
        touching_polygons.append(touching_polygon)
    return touching_polygons

def set_colors(polygons, touching_polygons):
    colors = [-1] * len(polygons)
    choices = [[0, 0, 0, 0] for _ in range(len(colors))]
    i = 0
    while True:
        if not 0 in choices[i][colors[i]+1:] or colors[i] == 3 or not all([[0 in choice] for choice in choices[i:]]):
            if colors[i] > -1:
                for touching_polygon in touching_polygons[i]:
                    choices[touching_polygon][colors[i]] -= 1
                colors[i] = -1
            i -= 1
            continue
        pre = colors[i]
        colors[i] = choices[i].index(0, colors[i]+1)
        for touching_polygon in touching_polygons[i]:
            choices[touching_polygon][colors[i]] += 1
            if pre > -1:
                choices[touching_polygon][pre] -= 1
        i += 1
        if i == len(colors):
            break
    return colors

def paint_colors(polygons, colors):
    color_choices = ["red", "yellow", "green", "blue"]
    for vertices_index, color_index in zip(polygons, colors):
        polygon = [vor.vertices[i] for i in vertices_index]
        plt.fill(*zip(*polygon), alpha=0.5, color=color_choices[color_index])

plt.clf()
start_points = np.random.rand(n, 2)
vor = Voronoi(start_points)
ax = plt.subplot()
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_box_aspect(1)

polygons = get_effective_polygons(vor.regions)
touching_polygons = get_touching_polygons(polygons)
colors = set_colors(polygons, touching_polygons)
paint_colors(polygons, colors)
plt.show()