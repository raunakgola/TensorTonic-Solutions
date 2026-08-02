# 📐 Intersection over Union (IoU)
## 📌 1. Coordinate System Context

In computer vision, the coordinate system differs from standard Cartesian graphs:

- **(0,0) is at the TOP-LEFT corner**
- Increasing X moves **RIGHT**
- Increasing Y moves **DOWN**

```
(0,0) ──────────────────────────► +X
  │
  │   (x1, y1) ┌──────────────┐
  │             │  Bounding    │
  │             │     Box      │
  │             └──────────────┘ (x2, y2)
  ▼
 +Y

```

- **Top-Left Corner:** `(x1, y1)` = min X, min Y
- **Bottom-Right Corner:** `(x2, y2)` = max X, max Y

---
## 🎨 2. Visualizing Box Overlap

Given two bounding boxes:

```python
box_a = [0, 0, 4, 4]
box_b = [2, 2, 6, 6]

```

```
(0,0)────────────┐
  │              │
  │   box_a  (2,2)────────┐
  │      │▓▓▓▓▓▓│         │
  └──────│▓▓▓▓▓▓│  box_b  │
       (4,4)────────────(6,6)

▓▓ = Intersection Region

```

[▶ Interactive IoU Visualizer](https://codepen.io/editor/Raunakgola/pen/019fc24b-0497-7564-99d0-0433507dc276)

---
## 🧠 3. How to Find the Intersection Rectangle

The intersection forms a new rectangle. Find its 4 boundary edges:

```
inter_x1 = max(box_a[x1], box_b[x1])   ← Rightmost Left Edge   (overlap starts where BOTH boxes started)
inter_y1 = max(box_a[y1], box_b[y1])   ← Bottommost Top Edge   (overlap starts where BOTH boxes started)
inter_x2 = min(box_a[x2], box_b[x2])   ← Leftmost Right Edge   (overlap ends where EITHER box ends)
inter_y2 = min(box_a[y2], box_b[y2])   ← Topmost Bottom Edge   (overlap ends where EITHER box ends)

```

> **Intuition:** Overlap starts at the **latest** starting point (`max`) and ends at the **earliest** ending point (`min`).

---
## 📐 4. Calculating Dimensions &amp; Handling Disjoint Boxes

```
width  = inter_x2 - inter_x1
height = inter_y2 - inter_y1

```

> ⚠️ **What if boxes do NOT overlap?** If boxes are completely separate, width or height will be **negative**. Clamp to 0:

```
valid_width  = max(0, width)
valid_height = max(0, height)

area_intersection = valid_width * valid_height

```

---
## 🧮 5. Computing Union and Final IoU

Using the **Inclusion-Exclusion Principle:**

```
Area(Union) = Area(A) + Area(B) - Area(Intersection)

IoU = Area(Intersection) / Area(Union)

```
### Numerical Example

```
box_a = [0, 0, 4, 4]    box_b = [2, 2, 6, 6]

Area(A)            = (4 - 0) × (4 - 0) = 16
Area(B)            = (6 - 2) × (6 - 2) = 16
Intersection Area  = (4 - 2) × (4 - 2) = 4
Union Area         = 16 + 16 - 4        = 28

IoU = 4 / 28 ≈ 0.142857...

```

---
## 💻 6. Code

```python
def iou(box_a, box_b):
    """
    Compute Intersection over Union of two bounding boxes.
    Each box: [x1, y1, x2, y2]
    """
    # Intersection rectangle
    inter_x1 = max(box_a[0], box_b[0])
    inter_y1 = max(box_a[1], box_b[1])
    inter_x2 = min(box_a[2], box_b[2])
    inter_y2 = min(box_a[3], box_b[3])

    # Clamp to 0 if no overlap
    inter_area = max(0, inter_x2 - inter_x1) * max(0, inter_y2 - inter_y1)

    # Individual areas
    area_a = (box_a[2] - box_a[0]) * (box_a[3] - box_a[1])
    area_b = (box_b[2] - box_b[0]) * (box_b[3] - box_b[1])

    # Union
    union_area = area_a + area_b - inter_area

    return inter_area / union_area if union_area &gt; 0 else 0.0

```

---
## ✅ 7. Test Cases

box_a box_b IoU `[0, 0, 4, 4]` `[2, 2, 6, 6]` `0.142857` `[0, 0, 2, 2]` `[3, 3, 5, 5]` `0.0` `[0, 0, 4, 4]` `[0, 0, 4, 4]` `1.0`

---
## 🧠 8. Key Takeaways

```
IoU = 1.0   → perfect overlap (identical boxes)
IoU = 0.0   → no overlap at all
IoU &gt; 0.5   → generally considered a good detection in object detection

```