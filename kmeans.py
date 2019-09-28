import math
import numpy as np

class KMeans:

     def __init__(self, k=3, tol=0.0001, max_iter=500, ssid_list=None):
          self.k = k
          self.tol = tol
          self.max_iter = max_iter
          self.ssid_list = ssid_list

          if ssid_list:
               self.ssid_list = ssid_list

     def euclid_distance(self, ap_one, ap_two):
          sq_dist = 0

          for i in range (len(self.ssid_list)):
               if self.ssid_list[i] in ap_one.keys() and \
                  self.ssid_list[i] in ap_two.keys():

                    sq_dist += (ap_one[self.ssid_list[i]] - ap_two[self.ssid_list[i]])**2

               elif self.ssid_list[i] in ap_one.keys() and \
                    self.ssid_list[i] not in ap_two.keys():

                    sq_dist += (ap_one[self.ssid_list[i]])**2

               elif self.ssid_list[i] not in ap_one.keys() and \
                    self.ssid_list[i] in ap_two.keys():

                    sq_dist += (ap_two[self.ssid_list[i]])**2

          euclid_dist = math.sqrt(sq_dist)

          return euclid_dist

     def fit(self, data):

          self.centroids = {}

          for i in range(self.k):
               self.centroids[i] = data[i]

          for i in range(self.max_iter):
               self.classes = {}
               for i in range(self.k):
                    self.classes[i] = []

               for loc in data:
                    distances = [self.euclid_distance(loc, self.centroids[centroid]) for centroid in self.centroids]
                    classification = distances.index(min(distances))
                    self.classes[classification].append(loc)

               previous = dict(self.centroids)

               new_classes = self.classes
               for classification in self.classes:

                    print()
                    print("******************* self.classes **************************")
                    print(self.classes[classification])
                    print()
                    print("******************* self.classes.values **************************")
                    for val in self.classes[classification]:
                         print(val)

                    for val in self.classes[classification]:
                         new_classes[classification] += np.average([v for v in val.values()], axis=0) ############## fix this!!!!!!!!!!!!!!!
                    print (new_classes)
               
               isOptimal = True

               for centroid in self.centroids:

                    original_centroid = previous[centroid]
                    curr = self.centroids[centroid]

                    if np.sum((curr - original_centroid)/original_centroid * 100.0) > self.tol:
                         isOptimal = False

               if isOptimal:
                    break

     def pred(self, loc):
          distances = [self.euclid_distance(loc, self.centroids[centroid]) for centroid in self.centroids]
          classification = distances.index(min(distances))

          return classification


# X = np.array([[50, 50], [50, 62], [50, 75], [62, 50], [62, 62], [62, 75], [75, 50], [75, 62], [75, 75],
#      [50, 150], [50, 162], [50, 175], [62, 150], [62, 162], [62, 175], [75, 150], [75, 162], [75, 175],
#      [50, 250], [50, 262], [50, 275], [62, 250], [62, 262], [62, 275], [75, 250], [75, 262], [75, 275],
#      [150, 50], [150, 62], [150, 75], [162, 50], [162, 62], [162, 75], [175, 50], [175, 62], [175, 75],
#      [150, 150], [150, 162], [150, 175], [162, 150], [162, 162], [162, 175], [175, 150], [175, 162], [175, 175],
#      [150, 250], [150, 262], [150, 275], [162, 250], [162, 262], [162, 275], [175, 250], [175, 262], [175, 275],
#      [200, 250], [200, 262], [200, 275], [212, 250], [212, 262], [212, 275], [225, 250], [225, 262], [225, 275],
#      [250, 50], [250, 62], [250, 75], [262, 50], [262, 62], [262, 75], [275, 50], [275, 62], [275, 75],
#      [250, 150], [250, 162], [250, 175], [262, 150], [262, 162], [262, 175], [275, 150], [275, 162], [275, 175],
#      [250, 250], [250, 262], [250, 275], [262, 250], [262, 262], [262, 275], [275, 250], [275, 262], [275, 275]])