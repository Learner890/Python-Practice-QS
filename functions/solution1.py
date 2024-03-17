def calculate_area(base,height,shape='traingle'):
    if shape.lower()=='triangle':
        area=0.5*base*height
    else:
        area=base*height
    return area
    



def main():
    shape=input("Enter shape either traingle or rectangle : ")
    if shape.lower()=='traingle':
        base=float(input("Enter base of the traingle : "))
        height=float(input("Enter height of traingle : "))
        output=calculate_area(base,height,shape)
        print(f"Area of triangle with base {base} and height {height} is {output}")
    else:
        length=float(input("Enter length of rectangle : "))
        width=float(input("Enter width of rectangle"))
        output=calculate_area(length,width,shape)
        print(f"Area of triangle with base {length} and height {width} is {output}")


if __name__=="__main__":
    main()