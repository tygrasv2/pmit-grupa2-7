
# Expense Tracker Dashboard (Model Project)

This is a **model project** for the course *Zarządzanie projektami IT*. 
It demonstrates a lightweight agile workflow, CI/CD, quality checks, and documentation structure.

## Quickstart
1. Create a new repository and copy these files.
2. (Optional) Set `SONAR_TOKEN` and `SONAR_HOST_URL` as repository secrets if you use SonarQube/SonarCloud.
3. Run locally:
   ```bash
   python -m venv .venv && source .venv/bin/activate
   pip install -r requirements.txt
   pytest -q
   ```
4. Push to main — CI will run tests and linters.

## Vision
Deliver a minimal **Expense Tracker Dashboard** (ETD) that lets a user:
- record expenses (category, amount, date, note),
- view a simple summary for the last 30 days,
- export data as CSV.
