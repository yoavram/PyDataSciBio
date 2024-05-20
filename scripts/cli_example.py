import argparse
import math

def calculate_circle_area(radius):
    return math.pi * radius**2

def main():
    parser = argparse.ArgumentParser(description='Calculate the area of a circle.')
    parser.add_argument('-r', '--radius', type=float, help='Radius of the circle', required=True)
    args = parser.parse_args()

    area = calculate_circle_area(args.radius)
    print(f"The area of the circle with radius {args.radius} is: {area:.2f}") # change to normal print

if __name__ == "__main__":
    main()