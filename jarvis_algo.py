import matplotlib.pyplot as plt

def jarvis_convex_hull(points):
   #need of 3 points
    if len(points) < 3:
        raise ValueError("Convex hull computation requires at least 3 points.")

    # Find the leftmost point
    leftmost_point = min(points, key=lambda p: (p[0], p[1]))
    hull = []
    current_point = leftmost_point

    while True:
        hull.append(current_point)
        next_point = points[0]
        for candidate in points:
            if candidate == current_point:
                continue
            # Check orientation
            cross_product = (
                (next_point[0] - current_point[0]) * (candidate[1] - current_point[1]) -
                (candidate[0] - current_point[0]) * (next_point[1] - current_point[1])
            )
            if next_point == current_point or cross_product < 0:
                next_point = candidate

        current_point = next_point
        if current_point == leftmost_point:
            break

    return hull

# Visualization
def visualize_convex_hull(points, hull):
    # Extract x and y coordinates
    x, y = zip(*points)

    # Plot the points
    plt.scatter(x, y, color='blue', label='Points')

    # Plot the convex hull
    hull_x, hull_y = zip(*(hull + [hull[0]]))  # Close the hull by adding the first point at the end
    plt.plot(hull_x, hull_y, color='red', label='Convex Hull')

    # Add labels and legend
    plt.title('Convex Hull Visualization (Jarvis Algorithm)')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    # Example points
    points = [(0, 3), (2, 2), (1, 1), (2, 1), (3, 0), (0, 0), (3, 3)]

    # Compute convex hull
    hull = jarvis_convex_hull(points)

    # Visualize
    visualize_convex_hull(points, hull)
