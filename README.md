# Automatyzacja przypadku testowego dla aplikacji mobilnej Android przy pomocy Appium #

Celem projektu jest zautomatyzowanie wybranych przypadkow testowych dla aplikacji mobilnej **Fitatu** za pomoca emulatora urządzenia Samsung Galaxy S8 z Android 8.0. 

W aplikacji Fitatu znajdziemy miedzy innymi licznik kalorii, kalkulator wartości odżywczych, dziennik odżywiania, monitor utraty wagi, przypomnienia o piciu wody, proste zdrowe przepisy, wymienniki węglowodanowe.


**Środowisko testowe, dane konfiguracyjne (hardware/software):**
System operacyjny komputera: Windows 10, 64-bitowy, 
Dane o komputerze: Procesor Intel(R) Core(TM) i5-1035G1 CPU @ 1.00GHz   1.19 GHz, 16 GB RAM.
Chrome wersja 89.0.4389.90,
Ubuntu 20.04 LTS,
java  1.8.0_292,
Android Studio 4.2.1,
node.js 14.16.1,
npm 6.14.12,
appium 1.20.2,
appium-doctor 1.16.0,
Pycharm 2021.1.2,
python 3.8.5,
pip 20.2.3,
Appium Python Client 1.1.0,
selenium 3.141.0.

Testy z wykorzystaniem Genymotion Cloud – SaaS, emulator urządzenia Samsung Galaxy S8 z Android 8.0

## **I Przypadek testowy:** ##

**ID:** 001

**Tytuł:**  Logowanie się użytkownika używając nieprawidłowego adresu e-mail

Plik: 01test_fitatu.py Klasa: Test1Appium Metoda: testIncorrectEmail

**Kroki:**
1. Otwórz aplikację Fitatu.apk
2. Zamknij komunikat „Intent Filter Verification Service has stopped”
3. Wybierz z menu głównego przycisk logowania „Log in”
4. Kliknij ponownie przycisk „Log in”
5. Wpisz nieprawidłowy adres e-mail: „tester.135@wp.pl”
6. Wpisz hasło: „Testy123”
7. Kliknij przycisk „Log in”

## **I Oczekiwane rezultaty:** ##  
Logowanie użytkownika nie powiodło się. Użytkownik otrzymał komunikat:” Login error” „Incorrect email address or/and password.”

<p align="center">
    <img src="https://github.com/Jula90210/Automatyzacja-Appium/blob/master/01fitatu.png" width="900" />

## **II Przypadek testowy:** ##

**ID:** 002

**Tytuł:**  Poprawne zalogowanie się do aplikacji i sprawdzenie czy w zakładce „More” pod przyciskiem „Log out” znajduje się login użytkownika.
Plik: 02test_fitatu.py Klasa: Test2Appium Metoda: testCorrectEmail

**Kroki:**
1. Otwórz aplikację Fitatu.apk
2. Zamknij komunikat „Intent Filter Verification Service has stopped”
3. Wybierz z menu głównego przycisk logowania „Log in”
4. Kliknij ponownie przycisk „Log in”
5. Wpisz poprawny adres mailowy: „tester.123@wp.pl”
6. Wpisz hasło: „Testy123”
7. Kliknij przycisk „Log in”
8. Kliknij wstecz androidowe i przejdź do strony dodawania posiłków
9. Wybierz przycisk „More”
10. Sprawdź czy pod przyciskiem „Log out” znajduje się login: „tester.123@wp.pl”

## **II Oczekiwane rezultaty:** ##  
Logowanie przebiega pomyślnie. Użytkownik loguje się do aplikacji. Pod przyciskiem „Log out” znajduje się login użytkownika:”tester.123@wp.pl”.

<p align="center">
    <img src="https://github.com/Jula90210/Automatyzacja-Appium/blob/master/02fitatu.png" width="900" />

## **III Przypadek testowy:** ##

**ID:** 003

**Tytuł:**  Uzupełnienie danych w zakładce „Weight loss”  podając niepoprawną datę urodzenia(31.02.1997)

Plik: 03test_fitatu.py Klasa: Test3Appium Metoda: testInCorrectDateOfBirth

**Kroki:**
1. Otwórz aplikację Fitatu.apk
2. Zamknij komunikat „Intent Filter Verification Service has stopped”
3. Wybierz z menu głównego „Weight loss”
4. Wpisz następujące dane:
Gender:”Female”
Date of birth: „31.02.1997”
Height: „172”
Current Body Weight: „76”
Goal Weight: „66
5. Kliknij w opcje zaawansowane (Advanced settings (optional))
6. Wybierz poziom aktywności w ciągu dnia (level of activity during the day): „Very low”
7. Kliknij przycisk dalej „Next”
       

## **III Oczekiwane rezultaty:** ##  
Pod polem z datą urodzenia pojawia się czerwony komunikat: „Date of birth is incorrect”. Użytkownik nie może przejść dalej.

<p align="center">
    <img src="https://github.com/Jula90210/Automatyzacja-Appium/blob/master/03fitatu.png" width="900" />

## **IV Przypadek testowy:** ##

**ID:** 004

**Tytuł:**  Sprawdzenie czy użytkownik poniżej 16 roku życia może wypełnić dane w zakładce „Weight loss”

Plik: 04test_fitatu.py Klasa:Test4Appium Metoda: testDateOfBirthBelow16yo

**Kroki:**
1. Otwórz aplikację Fitatu.apk
2. Zamknij komunikat „Intent Filter Verification Service has stopped”
3. Wybierz z menu głównego „Utrata masy ciała”
4. Uzupełnij dane:
Gender:”Female”
Date of birth: „31.01.2010”
Height: „172”
Current Body Weight: „76”
Goal Weight: „66”
5. Kliknij w opcje zaawansowane (Advanced settings (optional))
6. Wybierz poziom aktywności w ciągu dnia (level of activity during the day): „Very low”
7. Kliknij przycisk dalej „Next”
       

## **IV Oczekiwane rezultaty:** ##  
Pod polem do wprowadzania daty urodzenia pojawia się czerwony komunikat: „You must be at least 16 years old.” Użytkownik nie przechodzi dalej. 

<p align="center">
    <img src="https://github.com/Jula90210/Automatyzacja-Appium/blob/master/04fitatu.png" width="900" />

## **V Przypadek testowy:** ##

**ID:** 005

**Tytuł:**  Sprawdzenie zakresu wzrostu użytkownika (niższego niż 120 cm)

Plik: 05test_fitatu.py Klasa:Test5Appium Metoda: testHeightLowerThan120cm

**Kroki:**
1. Otwórz aplikację Fitatu.apk
2. Zamknij komunikat „Intent Filter Verification Service has stopped”
3. Wybierz z menu głównego „Weight loss”
4. Uzupełnij dane:
Gender:”Female”
Date of birth: „31.01.2005”
Height: „119”
Current Body Weight: „76”
Goal Weight: „66”
5. Kliknij w opcje zaawansowane (Advanced settings (optional))
6. Wybierz poziom aktywności w ciągu dnia (level of activity during the day): „Very low”
7. Kliknij przycisk dalej: „Next”
       

## **V Oczekiwane rezultaty:** ##  
Poniżej pola edycji wzrostu użytkownika pojawia się czerwony komunikat: „120-219 cm”. Użytkownik nie przechodzi dalej.

<p align="center">
    <img src="https://github.com/Jula90210/Automatyzacja-Appium/blob/master/05fitatu.png" width="900" />
    
## **VI Przypadek testowy:** ##

**ID:** 006

**Tytuł:**  Sprawdzenie zakresów wzrostu użytkownika (wyższego niż 219 cm)

Plik: 06test_fitatu.py Klasa:Test6Appium Metoda: testHeightHigherThan219cm

**Kroki:**
1. Otwórz aplikację Fitatu.apk
2. Zamknij komunikat „Intent Filter Verification Service has stopped”
3. Wybierz z menu głównego „Weight loss”
4. Uzupełnij dane:
Gender:”Female”
Date of birth: „31.01.2005”
Height: „220”
Current Body Weight: „76”
Goal Weight: „66”
5. Kliknij w opcje zaawansowane (Advanced settings (optional))
6. Wybierz poziom aktywności w ciągu dnia (level of activity during the day): „Very low”
7. Kliknij przycisk dalej: „Next”
       

## **VI Oczekiwane rezultaty:** ##  
Poniżej pola edycji wzrostu użytkownika pojawia się czerwony komunikat: „120-219 cm”. Użytkownik nie przechodzi dalej.

<p align="center">
    <img src="https://github.com/Jula90210/Automatyzacja-Appium/blob/master/06fitatu.png" width="900" />

## **VII Przypadek testowy:** ##

**ID:** 007

**Tytuł:**  Sprawdzenie czy po wprowadzeniu poprawnych danych w zakładce „Weight loss” zostanie dodany posiłek do śniadania „# płatki owsiane górskie z biedronki (Plony Natury”)

Plik: 07test_fitatu.py Klasa:Test7Appium Metoda:testAddMealToBreakfast

**Kroki:**
       
1. Otwórz aplikację Fitatu.apk
2. Zamknij komunikat „Intent Filter Verification Service has stopped”
3. Wybierz z menu głównego „Utrata masy ciała”
4. Wpisz poprawne dane:
Gender:”Female”
Date of birth: „04.07.1997”
Height: „172”
Current Body Weight: „76”
Goal Weight: „66”
5. Kliknij w opcje zaawansowane (Advanced settings (optional))
6. Wybierz poziom aktywności w ciągu dnia (level of activity during the day) „Very low”
7. Kliknij przycisk dalej: „Next” i przejdź do dodawania posiłków
8. Przejdź do pola wyszukiwania posiłków: „Search for your meal”  wybierając przycisk dalej „Next”
9. Dodaj pierwszy posiłek i wpisz w opcji wyszukiwania: „platki owsiane”
10. Wybierz z listy : „# płatki owsiane górskie z biedronki (Plony Natury”)
11. Przejdź do wyboru właściwej miary „Choose the right measure” klikając przycisk zrobione „Done”
12. Wybierz miarę posiłku: „4xtablespoon”
       

## **VII Oczekiwane rezultaty:** ##  
W profilu użytkownika w zakładce „Breakfast” został dodany posiłek: „# płatki owsiane górskie z biedronki (Plony Natury)”.

<p align="center">
    <img src="https://github.com/Jula90210/Automatyzacja-Appium/blob/master/07fitatu.png" width="900" />

## **VIII Przypadek testowy:** ##

**ID:** 008

**Tytuł:**  Sprawdzenie czy w zakladce „Utrata masy ciała” przycisk przejścia do następnego ekranu jest w języku polskim („Dalej”)

Plik: 08test_fitatu.py Klasa: Test8Appium metoda: testChooseLanguage


**Kroki:**
       
Kroki:
1. Otwórz aplikację Fitatu.apk
2. Zamknij komunikat „Intent Filter Verification Service has stopped”
3. Kliknij na ikonkę flagi w prawym górnym rogu
4. Wybierz „Język polski”
5. Kliknij wstecz androidowe i powróć do menu głównego
6. Wejdź w zakładkę „Utrata masy ciała” i sprawdź czy przycisk przejścia do następnego ekranu jest w języku polskim („Dalej”)
       

## **VIII Oczekiwane rezultaty:** ##  
Aplikacja działa w języku polskim i w zakladce „Utrata masy ciała” przycisk przejścia do następnego ekranu jest w języku polskim („Dalej”).

<p align="center">
    <img src="https://github.com/Jula90210/Automatyzacja-Appium/blob/master/08fitatu.png" width="900" />












