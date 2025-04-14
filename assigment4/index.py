def main():
    print("Temprature Converter Faranheit! :)")
    faranheit = float(input("Enter the temprature in Faranheit: "))
    celcius = (faranheit - 32) * 5.0/9.0
    print(f"Temperature in Faranheit is {faranheit}F and in Celcius is {celcius}C.")


# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()