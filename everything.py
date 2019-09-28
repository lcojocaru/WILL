import xml.etree.ElementTree as ET
import numpy as np
import matplotlib.pyplot as plt
from kmeans import KMeans

def do_rss_stack_diff(ssid_dict):
    ssid_dict_diff = {}
    for ssid in ssid_dict:
        diff = 0
        for ssid_iter in ssid_dict:
            diff += abs(ssid_dict[ssid] - ssid_dict[ssid_iter])
        ssid_dict_diff[ssid] = diff
    return ssid_dict_diff

tree = ET.parse('foreground_vlad.xml')
root = tree.getroot()
loc_list = []

for loc in root.iter('loc'):
    r_dict = {}

    for r in loc.iter('r'):
        r_dict[r.get('b')] = int(r.get('s'))

    loc_list.append(r_dict)

ssid_list = []
loc_diff_list = []
for loc in loc_list:
    loc_diff_list.append(do_rss_stack_diff(loc))
    print(loc)
    for ssid in loc:
        if ssid not in ssid_list:
            ssid_list.append(ssid)

print(ssid_list)
print()
print(loc_diff_list)

kmeans = KMeans(k=10, ssid_list=ssid_list)
kmeans.fit(loc_diff_list)







y_kmeans = kmeans.predict(X)
centers = kmeans.cluster_centers_
print(centers)

plt.scatter(X[:, 0], X[:, 1], c=y_kmeans, s=50, cmap='viridis')
plt.scatter(centers[:, 0], centers[:, 1], c='black', s=200, alpha=0.5)
plt.show()