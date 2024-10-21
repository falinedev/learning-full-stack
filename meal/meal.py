def main():
# Ask user what time it is
    time = input ("What time is it? ")

    time_converted = (convert(time))

    if time_converted == 7 <= 8.0:
        print ("breakfast time")
    if time_converted == 12.0 <= 13.0:
        print ("lunch time")
    elif time_converted == 18.0 <= 20.0:
        print ("dinner time")

def convert(time):

    hours, minutes = time.split(":")

    hours = float (hours)
    minutes = float (minutes) / 100

    if minutes > 0.25:
        minutes = 0.5

    time = (hours + minutes)
    return (time)

if __name__ == "__main__":
    main()
