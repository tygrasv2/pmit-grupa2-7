# Project Charter — Fitness Tracker

## Cel (SMART)
Do **15 grudnia 2025** dostarczyć wersję MVP aplikacji webowej Fitness Tracker umożliwiającej:
- dodawanie planów treningowych (US1),
- dodawanie ćwiczeń (US2),
- przeglądanie listy planów (US3),
- wizualizację postępów (US4),
- konfigurację CI (TECH1).

Czas dodania nowego planu ≤ 10 s; błędy krytyczne ≤ 1/100 uruchomień.

## Zakres (in/out)
**IN:** backend PHP z pamięcią in-memory/plikową, UI, testy jednostkowe (TECH3), pipeline CI (TECH1).  
**OUT:** rejestracja treningów, integracja użytkowników, logowanie użytkowników, analiza jakości (TECH2), edycja/usuń plan (US6).

## Interesariusze
- Product Manager (PM)
- Developerzy (Backend, Frontend)
- DevOps
- Moderatorzy (testy i feedback)

## Kryteria sukcesu
- Wszystkie kryteria akceptacji z `backlog.csv` spełnione dla US1–US4 i TECH1.
- Pipeline CI zielony.
- Dokumentacja i testy jednostkowe zakończone (TECH3).

## Założenia
- Zespół 4 osoby, sprint 2-tygodniowy.
- Częściowy dostęp do hostingu.

## Ograniczenia
- Tylko wersja webowa.
- Brak integracji z zewnętrznym API fitness.
