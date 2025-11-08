# Sprint 1 - Plan (2 tygodnie)

## Cel sprintu
Dostarczyć MVP: dodawanie planów treningowych, dodawanie ćwiczeń, lista planów, wykresy postępów, działający pipeline CI.

## Zakres (wybrane z BACKLOG.csv)
- US1 - Dodanie planu treningowego  
- US2 - Dodanie ćwiczenia do planu  
- US3 - Lista planów treningowych  
- US4 - Wykres postępów  
- TECH1 - Pipeline CI  
- TECH3 - Testy jednostkowe  

## Zadania techniczne
- Inicjalizacja repo i struktury projektu.
- Implementacja modelu i prostego storage (in-memory + zapis JSON/CSV).
- Funkcjonalności:
  - Dodawanie planu treningowego (US1)
  - Dodawanie ćwiczenia do planu (US2)
  - Lista planów treningowych (US3)
  - Generowanie wykresu postępów (US4)
- Testy jednostkowe (TECH3)
- Konfiguracja CI/CD (TECH1)

## Definition of Done
- Wszystkie user stories (US1-US4) spełniają kryteria akceptacji.
- Testy jednostkowe zielone (>= 80% coverage mile widziane).
- Lint bez błędów.
- PR z code review (≥ 1 approval).
- Uaktualnione README i changelog sprintu.

## Ryzyka sprintu
| ID | Ryzyko | Reakcja | Plan awaryjny |
|----|---------|----------|----------------|
| R1 | Zbyt duży zakres funkcjonalności | Timeboxing | Ograniczyć zakres do US1-US3 |
| R4 | Brak pokrycia testami | Testy jednostkowe | Zwiększyć priorytet TECH3 |
