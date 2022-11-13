def estimate_home_value(size_in_sqft, number_of_bedrooms):

    # Assumed all homes are worth at least $50,000
    value =50000

    # Adjusting the value estimated based on the size of the house
    value = value + (size_in_sqft*92)

    # Adjusting the value estimated based on the number of bedrooms
    value = value + (number_of_bedrooms * 10000)

    return value

# Estimated value of 4000ft house with 5 bedrooms

value = estimate_home_value(4000, 5)

print("Estimated valued: " + str(value))