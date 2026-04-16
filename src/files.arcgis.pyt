from zipfile import ZipFile
import os

base = "/mnt/data/multi_layer_neural_system_v7"
os.makedirs(base, exist_ok=True)

def write(path, content):
    full = os.path.join(base, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w") as f:
        f.write(content)

# README
write("README.md", """
Multi Layer Neural System v7 (ROS2 + Nav2 + SLAM Architecture Stub)

This is a robotics cognition stack:
- Perception (YOLO)
- Cognition (DQN + GPT fallback)
- SLAM (RTAB-Map stub)
- Navigation (Nav2 bridge concept)
- ROS2 node architecture (conceptual)

Run as a reference architecture for robotics expansion.
""")

# requirements
write("requirements.txt", """
torch
numpy
opencv-python
ultralytics
""")

# tf tree
write("ros2_ws/src/tf_tree/tf_tree.py", """
class TFTree:
    def __init__(self):
        self.frames = {}

    def set_transform(self, parent, child, transform):
        self.frames[(parent, child)] = transform

    def get_transform(self, parent, child):
        return self.frames.get((parent, child), None)
""")

# nav2 bridge stub
write("ros2_ws/src/nav2_bridge/nav2_bridge.py", """
class Nav2Bridge:
    def __init__(self):
        self.goal = (0,0)

    def set_goal(self, x, y):
        self.goal = (x,y)

    def compute_next_action(self, pose):
        px, py = pose
        gx, gy = self.goal

        if px > gx:
            return "forward"
        if py > gy:
            return "left"
        return "forward"
""")

# rtabmap stub
write("slam/rtabmap_stub.py", """
class RTABMap:
    def __init__(self):
        self.map = []

    def update(self, pose, observations):
        self.map.append((pose, observations))

    def get_map(self):
        return self.map
""")

# main system
write("main.py", """
print('Multi Layer Neural System v7 starting...')

from ros2_ws.src.nav2_bridge.nav2_bridge import Nav2Bridge
from slam.rtabmap_stub import RTABMap

nav = Nav2Bridge()
slam = RTABMap()

pose = (0,0)

nav.set_goal(10,10)

for i in range(10):
    action = nav.compute_next_action(pose)
    pose = (pose[0]+1, pose[1]+1)
    slam.update(pose, ["obj"])
    print(pose, action)
""")

zip_path = "/mnt/data/multi_layer_neural_system_v7.zip"
with ZipFile(zip_path, "w") as z:
    for root, _, files in os.walk(base):
        for file in files:
            full = os.path.join(root, file)
            arc = os.path.relpath(full, base)
            z.write(full, arc)

zip_path
