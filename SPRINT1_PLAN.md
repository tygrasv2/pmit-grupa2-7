# Sprint 1 - Plan (2 tygodnie)

## Cel sprintu
Dostarczyć MVP: dodawanie planów treningowych i wykresy postępów, działający pipeline CI.

## Zakres (wybrane z BACKLOG.csv)
- US1 - Dodanie planu treningowego  
- US4 - Wykres postępów  
- TECH1 - Pipeline CI  
- TECH3 - Testy jednostkowe  

## Zadania techniczne
- Funkcjonalności:
  - Dodawanie planu treningowego (US1)
    - Stworzenie tabeli do planów w bazie danych  
    - Backend: endpoint do dodawania i pobierania planów  
    - Frontend: formularz dodawania planu z walidacją oraz lista utworzonych planów
  - Generowanie wykresu postępów (US4) 
    - Stworzenie tabeli do treningów w bazie danych  
    - Backend: endpoint zwracający dane treningów do wykresu  
    - Frontend: widok wykresu postępów z obsługą braku danych
- Testy jednostkowe (TECH3)
- Konfiguracja CI/CD (TECH1)

## Definition of Done
- User stories (US1 oraz US4) spełniają kryteria akceptacji.
- Testy jednostkowe zielone (>= 80% coverage mile widziane).
- Lint bez błędów.
- PR z code review (≥ 1 approval).
- Uaktualnione README i changelog sprintu.

## Ryzyka sprintu
| ID | Ryzyko | Reakcja | Plan awaryjny |
|----|---------|----------|----------------|
| R1 | Zbyt duży zakres funkcjonalności | Timeboxing | Ograniczyć zakres do US1 |
| R4 | Brak pokrycia testami | Testy jednostkowe | Zwiększyć priorytet TECH3 |
