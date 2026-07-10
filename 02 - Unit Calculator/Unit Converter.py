def length_converter(value, from_unit, to_unit):
    units={
        "mm":0.001,
        "cm":0.01,
        "m":1,
        "km":1000,
    }

    return (value*units[from_unit]/units[to_unit])
    
def weight_converter(value, from_unit, to_unit):
    units={
        "mg":0.001,
        "g":1,
        "kg":1000,
    }

    return (value*units[from_unit]/units[to_unit])

def temperature_converter(value, from_unit, to_unit):
        
    if from_unit == to_unit:
        return value

    #celcius
    if from_unit== "C":
        if to_unit=="F":
            return (value*9/5)+32
        elif to_unit=="K":
            return value+273.15

    #fahrenheit
    elif from_unit == "F":
        if to_unit == "C":
            return (value-32)*5/9
        elif to_unit == "K":
            return value-32*5/9+273.15

    #kelvin
    elif from_unit == "K":
        if to_unit == "C":
            return value-273.15
        elif to_unit == "F":
            return value-273.15*9/5+32

            
while True:

    print("\nUnit Converter\n")
    print("1. Length")
    print("2. Weight")
    print("3. Temperature")
    print("4. Exit")

    try:
        choice = int(input("Enter your choice: "))

        if choice == 4:
            print ("Goodbye !")
            break

        value=float(input("Enter value to convert:"))
        from_unit=input("Enter the unit you are converting from:").strip()
        to_unit=input("Enter the unit you are converting to:").strip()

        if choice == 1:
            answer=length_converter(value,from_unit,to_unit)
        
        elif choice == 2:
            answer=weight_converter(value,from_unit,to_unit)

        elif choice == 3:
            answer=temperature_converter(value,from_unit,to_unit)    

        else:
            print("Invalid choice")

        print(f"\n Result: {answer: .4f} {to_unit}" )


    except KeyError:
        print("Invalid Unit. Please try again!")

    except ValueError:
        print("Invalid value. Please enter a valid number!")

    except Exception as error:
        print(f"An error occurred: {error}")