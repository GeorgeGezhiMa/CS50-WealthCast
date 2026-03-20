# this is a program which helps users track their budget
from matplotlib import pyplot
import random
import numpy as np

# the main function asks the user about their fundamental incomes and expenses
income = 0
expenses = {}
investments = []
def main():
    print("Welcome to the Budget Tracker!")
    while True:
        action = input("Would you like to add an your income, add an expense, add an investment, or view your budget? (Type 'income', 'expense', 'investment', 'view', or 'projection') ")
        if action == "income":
            add_income()
            continue
        elif action == "expense":
            add_expense()
            continue
        elif action == "investment":
            add_investment()
            continue
        elif action == "view":
            show_budget()
            view_budget()
            continue
        elif action == "projection":
            net_worths = projection()
            plot_projection(net_worths)
            continue
        else:
            print("Invalid input. Please try again.")
            continue
    
# update the income
def add_income():
    global income
    while True:
        try:
            income = int(input("What is your total monthly income including both your full-time and part-time jobs? "))
            break
        except ValueError:
            print("Please enter a valid number.")

# the add_expense function allows the user to add different spend categories to their budget
def add_expense():
    global expenses
    while True:
        category = input("What category of expense (excluding investments) would you like to add? (e.g., rent, groceries, transportation) ")
        try:
            amount = int(input(f"How much do you spend on {category} each month? "))
            expenses[category] = amount
        except ValueError:
            print("Please enter a valid number.")
        _continue =  input("Would you like to add another expense? (yes/no) ")
        if _continue != "yes":
            break
        elif _continue == "yes":
            continue
        else:
            print("Invalid input. Please try again.")

# the add_investment function allows the user to add different investment categories to their budget
def add_investment():
    global investments
    while True:
        category = input("What category of investment would you like to add? (e.g., stocks, bonds, real estate) ")
        try:
            amount = int(input(f"How much do you invest in {category} each month? "))
        except ValueError:
            print("Please enter a valid number.")
        try:
            mu = float(input(f"What is the expected monthly return rate (in percentage) for {category}? "))
        except ValueError:
            print("Please enter a valid number.")
        try:
            sigma = float(input(f"What is the expected monthly volatility (in percentage) for {category}? "))
            investments.append((category, amount, mu, sigma))
        except ValueError:
            print("Please enter a valid number.")
        _continue =  input("Would you like to add another investment? (yes/no) ")
        if _continue != "yes":
            break
        elif _continue == "yes":
            continue
        else:
            print("Invalid input. Please try again.")

# the show_budget function allows the user to see their current budget status
def show_budget():
    expenses["investments"] = sum([inv[1] for inv in investments])
    expenses["savings"] = income - sum(expenses.values())
    print(f"Total Monthly Income: ${income}")
    print("Monthly Expenses:")
    for category, amount in expenses.items():
        print(f"  {category}: ${amount}")

# the view_budget function allows the user to see a pie chart of their spending breakdown
def view_budget():
    labels = list(expenses.keys())
    values = list(expenses.values())

    def show_value(pct):
        total = sum(values)
        value = pct * total / 100
        return f"${value:.0f}"
    try:
        pyplot.pie(values, autopct=show_value)
    except ValueError:
        print("Total expenses must not exceed total income to display pie chart.")

    legend_labels = [f"{item}: ${expense}" for item, expense in expenses.items()]

    pyplot.legend(
        legend_labels,
        loc="center left",
        bbox_to_anchor=(1, 0.5)
    )

    pyplot.title("Spending Breakdown")
    pyplot.tight_layout()
    pyplot.show()

# the projection function allows the user to see how their investments will grow over time
def projection():
    while True:
        try:
            time = int(input("How many months would you like to project your investments for? "))
        except ValueError:
            print("Please enter a valid number.")
        if time <= 0:
            print("Please enter a positive number.")
        else:
            break
    projections = []
    for i in range(len(investments)):
        category, amount, mu, sigma = investments[i]
        mean = [amount]
        lower = [amount]
        upper = [amount]
        sigma = sigma / 100
        mu = mu / 100
        for month in range(1, time + 1):
            mean.append(amount * np.exp(mu * month))
            lower.append(amount * np.exp(((mu - 0.5 * sigma**2)) * month - 1.96 * sigma * np.sqrt(month)))
            upper.append(amount * np.exp(((mu + 0.5 * sigma**2)) * month + 1.96 * sigma * np.sqrt(month)))
        projections.append((category, mean, lower, upper))

    net_worths = []
    for month in range(time + 1):
        savings = expenses["savings"] * month
        mean_net_worth = savings + sum([projection[1][month] for projection in projections])
        lower_net_worth = savings + sum([projection[2][month] for projection in projections])
        upper_net_worth = savings + sum([projection[3][month] for projection in projections])
        net_worths.append((mean_net_worth, lower_net_worth, upper_net_worth))
    
    return net_worths

def plot_projection(net_worths):
    mean_net_worths = [net_worth[0] for net_worth in net_worths]
    lower_net_worths = [net_worth[1] for net_worth in net_worths]
    upper_net_worths = [net_worth[2] for net_worth in net_worths]
    months = list(range(len(net_worths)))

    pyplot.plot(months, mean_net_worths, label="Mean Net Worth")
    pyplot.fill_between(months, lower_net_worths, upper_net_worths, color='b', alpha=0.2, label="95% Confidence Interval")
    pyplot.xlabel("Months")
    pyplot.ylabel("Net Worth ($)")
    pyplot.title("Projected Net Worth Over Time")
    pyplot.legend()
    pyplot.grid()
    pyplot.show()
    
if __name__ == "__main__":
    main()