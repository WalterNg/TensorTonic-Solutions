import math
def generate_anchors(feature_size, image_size, scales, aspect_ratios):
    """
    Generate anchor boxes for object detection.
    """
    boxes = []
    stride = image_size / feature_size
    for i in range(feature_size):
        for j in range(feature_size):
            cx = (j + 0.5) * stride
            cy = (i + 0.5) * stride

            for s in scales:
                for r in aspect_ratios:
                    w = s * math.sqrt(r)
                    h = s / math.sqrt(r)
                    box = [cx - w/2, cy - h/2, cx + w/2, cy + h/2]
                    boxes.append(box)

    return boxes
                    