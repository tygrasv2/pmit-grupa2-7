
from datetime import datetime, timedelta
from typing import List, Dict

_EXPENSES: List[Dict] = []

def add_expense(amount: float, category: str, date: datetime, note: str = "") -> Dict:
    if amount <= 0:
        raise ValueError("amount must be > 0")
    item = {
        "id": len(_EXPENSES) + 1,
        "amount": float(amount),
        "category": category or "general",
        "date": date,
        "note": note,
    }
    _EXPENSES.append(item)
    return item

def list_expenses() -> List[Dict]:
    return list(_EXPENSES)

def summary_last_30_days() -> Dict[str, float]:
    now = datetime.utcnow()
    cutoff = now - timedelta(days=30)
    filtered = [e for e in _EXPENSES if e["date"] >= cutoff]
    total = sum(e["amount"] for e in filtered)
    return {"count": len(filtered), "total": round(total, 2)}
