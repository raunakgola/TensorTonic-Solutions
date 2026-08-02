def iou(box_a, box_b):
    """
    Compute Intersection over Union of two bounding boxes.
    """
    # top left x1 for intersection
    inter_x1 = max(box_a[0], box_b[0]) 
    # top left y1 for intersection  
    inter_y1 = max(box_a[1], box_b[1])
    # bottom right x2 for intersection
    inter_x2 = min(box_a[2], box_b[2])
    # bottom right y2 for intersection
    inter_y2 = min(box_a[3], box_b[3])

    # intersection area
    width  = inter_x2 - inter_x1
    height = inter_y2 - inter_y1
    # but what if boxes don't overlap at all?
    # width or height could be NEGATIVE! so clamp to 0
    intersection = max(0, width) * max(0, height)
    area_a = (box_a[0]-box_a[2]) * (box_a[1]-box_a[3])
    area_b = (box_b[0]-box_b[2]) * (box_b[1]-box_b[3])
    union = area_a + area_b - intersection
    IoU = intersection / union
    return IoU