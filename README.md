# FutureNetWorth Tracker

#### Video Demo: https://youtu.be/MRKs1Jh-idM

#### Description:
FutureNetWorth Tracker is a Python-based financial planning tool designed to project a user's future net wealth based on income, expenses, and investments.

The program allows users to input their monthly income, categorize and track multiple expenses, and add investments with expected returns over time. Using this information, it estimates how wealth evolves, helping users better understand their financial trajectory.

The project is structured with simple functions:
- `add_income()` records or updates total income.
- `add_expense()` stores categorized expenses in a dictionary.
- `add_investment()` tracks investments including amount, rate of return, and duration.

Testing is implemented using `pytest`, with test cases validating correct updates to income, expenses, and investments. Mock input (`monkeypatch`) is used to simulate user interaction.

This project emphasizes:
- Clean function-based design
- Basic financial modeling
- Test-driven development using pytest

Overall, it serves as a simple but practical tool for visualizing and projecting future net wealth.