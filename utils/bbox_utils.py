
def get_center_of_box(bbox):
    y2 = bbox[3]
    x2 = bbox[2]
    x1 = bbox[0]
    y1 = bbox[1]
    return int((x1 + x2)/2),int((y2+y1)/2)

def get_bbox_width(bbox):
    x2 = bbox[2]
    x1 = bbox[0]
    return x2-x1


def measure_distance(p1,p2):
    return ((p1[0]-p2[0])**2 +(p1[1]-p2[1])**2)**0.5


def measure_xy_distance(p1,p2):
    return p1[0]-p2[0],p1[1]-p2[1]

def get_foot_position(bbox):
    x1,y1,x2,y2 = bbox
    return int((x1+x2)/2),int((y2))
