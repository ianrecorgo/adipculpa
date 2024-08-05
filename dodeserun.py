import numpy as np

# Define a function to apply a transformation matrix to a set of points
def apply_transformation(points, transformation_matrix):
    transformed_points = []
    for point in points:
        transformed_point = np.dot(transformation_matrix, np.append(point, 1))
        transformed_points.append(transformed_point[:2])  # Ignore the homogeneous coordinate
    return np.array(transformed_points)

# Define a function to calculate the bounding box of a set of points
def calculate_bounding_box(points):
    min_x = np.min(points[:, 0])
    min_y = np.min(points[:, 1])
    max_x = np.max(points[:, 0])
    max_y = np.max(points[:, 1])
    return (min_x, min_y), (max_x, max_y)

# Example items with vertices and transformation matrices
items = [
    {
        'vertices': np.array([[0, 0], [1, 0], [1, 1], [0, 1]]),
        'transformation': np.identity(3)  # No transformation
    },
    {
        'vertices': np.array([[0, 0], [2, 0], [2, 2], [0, 2]]),
        'transformation': np.array([
            [1, 0, 1],  # Translation by (1, 1)
            [0, 1, 1],
            [0, 0, 1]
        ])
    }
]

# Calculate bounding boxes for each item
for item in items:
    transformed_vertices = apply_transformation(item['vertices'], item['transformation'])
    bounding_box = calculate_bounding_box(transformed_vertices)
    print(f"Bounding box: {bounding_box}")
