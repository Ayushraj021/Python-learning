def can_form_triangle(a, b, c):
    # Check the triangle inequality theorem
    if a + b > c and a + c > b and b + c > a:
        return True
    else:
        return False

# Example usage
side1 = 3
side2 = 4
side3 = 5

if can_form_triangle(side1, side2, side3):
    print("The given numbers can form a triangle.")
else:
    print("The given numbers cannot form a triangle.")