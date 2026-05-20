# Playwright Automation Framework

## Overview
End-to-end test automation framework built with Playwright and Python
targeting the Saucedemo e-commerce application.

## Tech Stack
- Language: Python
- Automation Tool: Playwright
- Test Framework: pytest
- Design Pattern: Page Object Model
- CI/CD: GitHub Actions
- Reporting: pytest-html

## Framework Structure
playwright-framework/
├── pages/          → Page Object classes
├── tests/          → Test cases
├── utilities/      → Base class and helper functions
├── testdata/       → JSON test data
├── reports/        → Generated test reports
├── conftest.py     → Browser setup and fixtures
└── pytest.ini      → pytest configuration

## Test Coverage
- Login tests (valid, invalid, locked user)
- Product sorting tests
- Cart tests (add, remove)
- Checkout flow tests

## How to Run
pip install playwright pytest pytest-playwright pytest-html
playwright install
pytest --headed --html=reports/report.html