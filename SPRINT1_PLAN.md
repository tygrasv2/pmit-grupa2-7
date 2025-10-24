# Sprint 1 — Plan (2 tygodnie)

## Cel sprintu
Dostarczyć MVP: dodawanie planów treningowych, dodawanie ćwiczeń, lista planów, wykresy postępów, zielone CI.

## Zakres (wybrane z BACKLOG.csv)
- US1, US2, US3, US4, TECH1

## Zadania techniczne
- Inicjalizacja repo i struktury projektu
- Implementacja modelu i prostego storage (in-memory + zapis JSON/CSV)
- Funkcjonalności:
  - Dodawanie planu treningowego
  - Dodawanie ćwiczenia do planu
  - Lista planów treningowych
  - Generowanie wykresu postępów (prosta wizualizacja)
- Testy jednostkowe dla kluczowych funkcji
- Konfiguracja CI/CD (pytest, flake8, black)

## Definition of Done
- Testy jednostkowe zielone (>= 80% coverage mile widziane)
- Lint bez błędów
- PR z code review (>= 1 approval)
- Uaktualnione README i changelog sprintu

## Ryzyka sprintu
- Zbyt ambitny zakres – jeśli nie zdążymy z US4 (wykresy), ograniczyć do prostej wizualizacji danych w tabeli
