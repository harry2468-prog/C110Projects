Circle_diameter = float(input('Enter the circle diameter in cm: '))
Area = 3.142*0.25*Circle_diameter*Circle_diameter
print(f'Area of circle is ,{Area:.2f},cm^2')
Cylinder_Diameter = float(input('Enter the cylinder diameter in cm:  '))
Cylinder_Height = float(input('Enter the cylinder height in cm:  '))
Cross_sectional_Area_of_Cylinder = 0.25*3.142*Cylinder_Diameter*Cylinder_Diameter
Volume_of_cylinder=Cylinder_Height*Cross_sectional_Area_of_Cylinder
print(f'Cross-sectional area of cylinder is,{Cross_sectional_Area_of_Cylinder:.2f} cm^2')
print(f'Volume of cylinder is,{Volume_of_cylinder:.2f} cm^3')
# The code calculates the area of a circle and the volume of a cylinder based on user input for diameter and height.
# It uses the formula for the area of a circle (A = πr²) and the formula for the volume of a cylinder (V = πr²h).
# The results are printed with two decimal places for clarity.  

