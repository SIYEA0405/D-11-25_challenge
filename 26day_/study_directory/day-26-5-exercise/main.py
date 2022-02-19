weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}
# 🚨 Don't change code above 👆

#(temp_c * 9/5) + 32 = temp_f

# Write your code 👇 below:
weather_f = {day: (value * 9/5) + 32 for (day, value) in weather_c.items()}

print(weather_f)


