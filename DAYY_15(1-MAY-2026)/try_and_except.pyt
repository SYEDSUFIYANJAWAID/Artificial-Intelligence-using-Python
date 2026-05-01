try:
    a=int(input("enter number for divison by 100:"))
    if a <= 0:
        print("Please enter number greater than 0")
    else:
        print("the division of", a, "by 100 is:", 100 / a)

except ValueError:
    print("plz put number only",ValueError)

finally:
    print("program closed")


