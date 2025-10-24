
from datetime import datetime, timedelta
from app import add_expense, list_expenses, summary_last_30_days

def test_add_and_list():
    before = len(list_expenses())
    add_expense(10.5, "food", datetime.utcnow(), "lunch")
    after = len(list_expenses())
    assert after == before + 1

def test_summary_last_30_days_counts_recent_only():
    add_expense(5, "misc", datetime.utcnow() - timedelta(days=1))
    add_expense(100, "old", datetime.utcnow() - timedelta(days=40))
    s = summary_last_30_days()
    assert s["count"] >= 1 and s["total"] >= 5
