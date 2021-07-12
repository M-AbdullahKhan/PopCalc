import matplotlib.pyplot as plt


def population_in_year(first_year_pop, year_to_compute, annual_growth_rate, max_pop):
    """
    This function will calculate the population in a certain year. It does this by recursively calculating the
    population for each year and adding them together.

    :param first_year_pop: The initial population in year 1.
    :param year_to_compute: The year n for which the population will be calculated.
    :param annual_growth_rate: The annual growth rate as a floating point value between 0.0 and 1.0.
    :param max_pop: The maximum population that the environment can support.
    :return: The calculated population in the year n.
    """
    if year_to_compute == 1:
        return first_year_pop
    else:
        current_pop = population_in_year(first_year_pop, year_to_compute - 1, annual_growth_rate, max_pop)
        return current_pop + ((annual_growth_rate * (1 - current_pop/max_pop)) * current_pop)


# Creating data for population for years 1 - 100.
# Initial population = 900, Year (n) = 1 to 100, Annual growth rate (r) = 0.01, Maximum population (k) = 10000
years_to_calculate = range(1, 101)
pop_per_year = []

for i in years_to_calculate:
    pop_per_year.append(population_in_year(900, i, 0.01, 10000))

# Plotting and displaying a line plot using matplotlib for population for years 1 - 100.
plt.plot(years_to_calculate, pop_per_year)
plt.title("Population growth for years 1 to 100")
plt.ylabel("Population")
plt.xlabel("Year Number")
plt.show()

# Calculating and printing how many years (n) it takes for the population to reach 10 billion
# Initial population = 7 billion, Annual growth rate (r) = 0.011, Maximum population (K) = 10 billion.
total_years = 1
pop_in_last_year = 0

while pop_in_last_year < 9900000000:
    total_years += 1
    pop_in_last_year = population_in_year(7000000000, total_years, 0.011, 10000000000)

print("It will take " + str(total_years) + " years to exceed 9.9 billion population.")