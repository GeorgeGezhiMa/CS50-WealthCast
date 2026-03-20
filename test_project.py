import pytest
from project import add_income
from project import add_expense
from project import add_investment
from project import show_budget

def test_add_income(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "5000")
    add_income()
    import project
    assert project.income == 5000

def test_add_income_overwrite(monkeypatch):
    import project
    project.income = 5000
    monkeypatch.setattr("builtins.input", lambda _: "8000")
    project.add_income()
    assert project.income == 8000

def test_add_expense(monkeypatch):
    inputs = iter(["rent", "1500", "yes", "groceries", "500", "no"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    add_expense()
    import project
    assert project.expenses["rent"] == 1500
    assert project.expenses["groceries"] == 500

def test_add_investment(monkeypatch):
    
    inputs = iter(["stocks", "1000", "5", "10", "yes", "bonds", "500", "3", "5", "no"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    add_investment()
    import project
    assert project.investments[0] == ("stocks", 1000, 5.0, 10.0)
    assert project.investments[1] == ("bonds", 500, 3.0, 5.0)

