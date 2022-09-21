from pickle import FALSE
import networkx as nx
import numpy as np
import math

class Obstacle:
  #def __init__(self,orig_node_id,dest_node_id,current_lane_id,obstacle_node_id):
    #self.orig_node_id = orig_node_id
    #self.current_lane_id = current_lane_id
    #self.current_position = []
    #self.obstacle_node_id = obstacle_node_id

  def __init__(self,obstacle_node_id, obstacle_lane_id, fake_flag):
    self.fake_flag = fake_flag
    self.current_position  = []
    if fake_flag == False:
      self.obstacle_node_id = obstacle_node_id
      self.obstacle_lane_id = obstacle_lane_id
    else:
      self.fakeobs_node_id = obstacle_node_id
      self.fakeobs_lane_id = obstacle_lane_id


  def init(self, DG):
    if self.fake_flag == False:
      current_node_id = self.obstacle_node_id
    else:
      current_node_id = self.fakeobs_node_id
    self.current_position = DG.nodes[ current_node_id ]["pos"]

  def move(self):
    x_new = self.current_position[0]
    y_new = self.current_position[1]
    return x_new, y_new
