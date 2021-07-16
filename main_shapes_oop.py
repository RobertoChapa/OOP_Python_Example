import shape_areas_oop as sao

def main():
    # circle---
    circle = sao.Shape()
    circle.set_radius(2)
    print("Area of a circle: ", f"{circle.get_circle_area():.2f}")

    # square---
    square = sao.Shape()
    square.set_side(3)
    print("Area of a square: ", f"{square.get_square_area():.2f}")

    # rectangle---
    rectangle = sao.Shape()
    rectangle.set_width_length(2,4)
    print("Area of a rectangle: ", f"{rectangle.get_rectangle_area():.2f}")

    # triangle---
    triangle = sao.Shape()
    triangle.set_height_base(4,8)
    print("Area of a triangle: ", f"{triangle.get_triangle_area():.2f}")

if __name__ == '__main__':
    main()