
# Project Charter — Expense Tracker Dashboard (ETD)

## Cel (SMART)
Do **15 grudnia 2025** dostarczyć wersję MVP aplikacji webowej ETD umożliwiającej:
- dodawanie wydatków,
- podgląd sumy i liczby wydatków z ostatnich 30 dni,
- eksport CSV.
Czas rejestracji pojedynczego wydatku ≤ 10 s; błędy krytyczne ≤ 1/100 uruchomień.

## Zakres (in/out)
**IN:** prosty backend (Python), pamięć in‑memory/plik, UI minimalny, testy jednostkowe, CI.
**OUT:** rejestracja przychodów, integracje bankowe, logowanie użytkowników.

## Interesariusze
- Klient (prowadzący) – priorytety i akceptacja.
- PM zespołu studenckiego – prowadzenie backlogu.
- Zespół dev/test/DevOps – implementacja i jakość.

## Kryteria sukcesu
- Przejście demo i akceptacja kryteriów z `docs/ACCEPTANCE_CRITERIA.md`.
- Zielone pipeline’y w CI.
- Dokumentacja ukończona.

## Założenia
- Zespół 4 osoby, 1 sprint (2 tyg.).

## Ograniczenia
- Brak prawdziwej bazy danych i logowania.

