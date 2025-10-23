
# Acceptance Criteria — MVP

- **Dodanie wydatku**: wysłanie poprawnego JSON do POST /expenses zwraca 201 i id rekordu.
- **Lista**: GET /expenses zwraca listę z co najmniej 1 rekordem po dodaniu.
- **Podsumowanie**: GET /summary zwraca `{"count": N, "total": S}` dla ostatnich 30 dni.
- **Jakość**: CI zielone (pytest, flake8, black --check, bandit).
