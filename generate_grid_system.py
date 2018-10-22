# -*- coding: utf-8 -*-
"""
Created on Mon Oct 22 15:00:08 2018

@author: LN043-HB
"""

from geopy.distance import VincentyDistance
from shapely.geometry import Polygon

def grid_system_generator(current_zones):
    # center_save_list saves all the points as long as they are used as "center"
    real_center=(14.5546,121.0451)
    north_dist=55
    east_dist=20
    south_dist=70
    west_dist=30
    
    south_north_dist=north_dist+south_dist
    west_east_dist=west_dist+east_dist
    # Calculate the border points and draw a red rectangle based on the points
    north = VincentyDistance(kilometers=north_dist).destination(real_center, 0)
    east = VincentyDistance(kilometers=east_dist).destination(real_center, 90)
    south = VincentyDistance(kilometers=south_dist).destination(real_center, 180)
    west = VincentyDistance(kilometers=west_dist).destination(real_center, 270)
    new_range_list=[(north[0],east[1]),(south[0],east[1]),(south[0],west[1]),(north[0],west[1]),(north[0],east[1])]
    node_list={}
    zone_polygon_list={}
    # Calculate the side long of each square
    south_north=(new_range_list[0][0]-new_range_list[1][0])/(south_north_dist)
    west_east=(new_range_list[1][1]-new_range_list[2][1])/(west_east_dist)
    
    # Store the coordinates for each square
    for m in range(south_north_dist+1): 
        for n in range(west_east_dist+1):
            node_list[(m,n)]=(south[0]+south_north*m,west[1]+west_east*n)
    for i in range(south_north_dist): #110
        for j in range(west_east_dist):
            draw_node_list=Polygon([node_list[(i,j)],node_list[(i+1,j)],node_list[(i+1,j+1)],node_list[(i,j+1)],
                       node_list[(i,j)]])
            if current_zones.intersects(draw_node_list):
                zone_polygon_list[(i,j)]=draw_node_list
    return zone_polygon_list
            
    
