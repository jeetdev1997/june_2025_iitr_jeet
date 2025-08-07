def calculate_interest(principle, rate, time):
    intrest = (principle * rate * time) / 100
    return intrest

intrest = calculate_interest(100.05, 4.5, 5)
print(intrest)

