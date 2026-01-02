import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st  

# Ex 3.1: Load the dataset from the defined data_path and display the first 5 rows.

data_path = "../data/cities_temperatures.csv"

temps_df = pd.read_csv(data_path)  # TODO
temps_df.index=range (1, len(temps_df)+1)  # TODO
temps_df

 #Converting the date column to datetime date format in order to be able to analyze better the time series and plot it
temps_df["Date"] = pd.to_datetime(temps_df["Date"]).dt.date

# Ex 3.2: Create a new column called `AvgTemperatureCelsius` that contains the temperature in Celsius degrees.

# temps_df["AvgTemperatureCelsius"] = ...  # TODO: uncomment this line to complete it

temps_df["AvgTemperatureCelsius"] = (temps_df["AvgTemperatureFahrenheit"] - 32) * 5.0/9.0  # TODO: uncomment this line to complete it
temps_df

# Ex 3.3: How many different cities are there? Provide a list of them.

unique_countries_list = temps_df["City"].unique().tolist()  # TODO
num_cities= len(unique_countries_list)
print(f"There are {num_cities} different cities.")
print("List of cities:")
print(unique_countries_list)

# TODO: print a message with the number of unique countries and the list of them

# Ex 3.4: What are the minimum and maximum dates?

min_date = temps_df["Date"].min()  # TODO
max_date = temps_df["Date"].max()  # TODO

# TODO: print a message with the min and max dates
print(f"The minimum date is {min_date} and the maximum date is {max_date}.")


# Ex 3.5: What are the global minimum and maximum temperatures? Find the city and the date of each of them.

min_temp = temps_df["AvgTemperatureCelsius"].min()  # TODO
max_temp = temps_df["AvgTemperatureCelsius"].max()  # TODO

min_temp_city = temps_df.loc[temps_df["AvgTemperatureCelsius"] == min_temp, "City"].iloc[0]  # TODO
min_temp_date = temps_df.loc[temps_df["AvgTemperatureCelsius"] == min_temp, "Date"].iloc[0]  # TODO
max_temp_city = temps_df.loc[temps_df["AvgTemperatureCelsius"] == max_temp, "City"].iloc[0]  # TODO
max_temp_date = temps_df.loc[temps_df["AvgTemperatureCelsius"] == max_temp, "Date"].iloc[0]  # TODO

# TODO: print a message with the min temperature, its city and date, and then another message with the max temperature, its city and date
print(f"The minimum temperature is {min_temp:.2f}°C, recorded in {min_temp_city} on {min_temp_date}.")
print(f"The maximum temperature is {max_temp:.2f}°C, recorded in {max_temp_city} on {max_temp_date}.")

# Ex 3.6: For a given city and a range of dates (start and end):
#   - Make a line plot with the temperature reads of that city during the selected time period, the x axis has to be the timestamp column.
#   - Make a histogram of the temperature reads of that city during the selected time period.
#   - Make sure that all plots include a title, axis labels and a legend.

city = "Munich"
start_date = pd.to_datetime("2008-01-01").date()
end_date = pd.to_datetime("2010-12-31").date()

city_df = temps_df[temps_df["City"] == city]        # TODO: get a dataframe with the rows of the selected city

city_df_period = city_df[(city_df["Date"] >= start_date) & (city_df["Date"] <= end_date)]   # TODO: get a dataframe with the rows of the selected city and the selected period of time using the Date column and any of the <, >, <=, >= operators to compare with start_date and end_date

plt.figure(figsize=(10, 5))

# TODO: Uncomment and complete the following lines to plot the line plot using the city_df_period AvgTemperatureCelsius column as the y axis and the Date column as the x axis

plt.plot(city_df_period["Date"], city_df_period["AvgTemperatureCelsius"])    # TODO
plt.title(f"Temperature in {city} from {start_date} to {end_date}")   # TODO
plt.xlabel("Date")  # TODO
plt.ylabel("Temperature (°C)")  # TODO
plt.legend()

plt.show()

# TODO: Build the histogram plot using the city_df_period AvgTemperatureCelsius column as the data to plot

plt.figure(figsize=(10, 5))

plt.hist(city_df_period["AvgTemperatureCelsius"], bins=20)    # TODO: use the city_df_period AvgTemperatureCelsius column as the data to plot, you can use the parameter bins=20
plt.title(f"Temperature in {city} from {start_date} to {end_date}")   # TODO
plt.xlabel("Temperature (°C)")  # TODO
plt.ylabel("Frequency")  # TODO

plt.show()

# Ex 3.7: Now repeat the previous question but for a list of cities:
#   - Make a line plot with the temperature reads of the cities in the list, for the selected time period, every city has to be a different line with a different color, the x axis has to be the timestamp column.
#   - Make a histogram of the temperature reads of a list of selected cities, for the selected time period, every city has to be its own distribution with a different color.
#   - Make sure that all plots include a title, axis labels and a legend.

selected_cities = ["Munich", "Buenos Aires", "Tokyo"]
start_date = pd.to_datetime("2008-01-01").date()
end_date = pd.to_datetime("2010-12-31").date()


plt.figure(figsize=(15, 5))

# TODO: Uncomment and complete the following lines to plot the line plot using the city_df_period AvgTemperatureCelsius column as the y axis and the Date column as the x axis

for city in selected_cities:
    city_df = temps_df[temps_df["City"] == city]        # TODO: get a dataframe with the rows of the selected city
    city_df_period = city_df[(city_df["Date"] >= start_date) & (city_df["Date"] <= end_date)]   # TODO: get a dataframe with the rows of the selected city and the selected period of time using the Date column and any of the <, >, <=, >= operators to compare with start_date and end_date
    plt.plot(city_df_period["Date"], city_df_period["AvgTemperatureCelsius"], label=city)                # TODO plot each city line and use the label parameter to set the legend name for each city

plt.title("Temperature in Selected Cities")   # TODO
plt.xlabel("Date")  # TODO
plt.ylabel("Temperature (°C)")  # TODO

plt.legend()

# TODO: Build the histogram plot for the selected cities using the city_df_period AvgTemperatureCelsius column as the data to plot for each one

plt.figure(figsize=(15, 5))

for city in selected_cities:
    city_df = temps_df[temps_df["City"] == city]        # TODO: get a dataframe with the rows of the selected city
    city_df_period = city_df[(city_df["Date"] >= start_date) & (city_df["Date"] <= end_date)]   # TODO: get a dataframe with the rows of the selected city and the selected period of time using the Date column and any of the <, >, <=, >= operators to compare with start_date and end_date
    plt.hist(city_df_period["AvgTemperatureCelsius"], bins=20, label=city)                    # TODO: plot each city histogram in the same plot and use the label parameter to set the legend name for each city 

plt.title("Temperature in Selected Cities")   # TODO
plt.xlabel("Temperature (°C)")  # TODO
plt.ylabel("Frequency")  # TODO

plt.legend()

plt.show()




