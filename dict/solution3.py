def circle_calc(radius):
    area=3.14*radius*radius
    cirum_ference=2*3.14*radius
    diameter=2*radius
    return f"area = {area} circumference = {cirum_ference} diameter={diameter}"

def main():
    output=circle_calc(int(input('Enter the radius : ')))
    print(output)

if __name__=='__main__':
    main()