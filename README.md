# Automatyzacja przypadku testowego dla aplikacji mobilnej Android przy pomocy Appium

Celem projektu jest zautomatyzowanie wybranych przypadkow testowych dla aplikacji mobilnej Fitatu za pomoca emulatora urządzenia Samsung Galaxy S8 z Android 8.0. 

W aplikacji Fitatu znajdziemy miedzy innymi licznik kalorii, kalkulator wartości odżywczych, dziennik odżywiania, monitor utraty wagi, przypomnienia o piciu wody, proste zdrowe przepisy, wymienniki węglowodanowe.


**Środowisko testowe, dane konfiguracyjne (hardware/software):**
System operacyjny komputera: Windows 10, 64-bitowy, 
Dane o komputerze: Procesor Intel(R) Core(TM) i5-1035G1 CPU @ 1.00GHz   1.19 GHz, 16 GB RAM.
Chrome wersja 89.0.4389.90 
Ubuntu 20.04 LTS
java  1.8.0_292
Android Studio 4.2.1
node.js 14.16.1
npm 6.14.12
appium 1.20.2
appium-doctor 1.16.0.
Pycharm 2021.1.2
python 3.8.5
pip 20.2.3
Appium Python Client 1.1.0
selenium 3.141.0

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

## **II Oczekiwane rezultaty:** ##  Logowanie użytkownika nie powiodło się. Użytkownik otrzymał komunikat:” Login error” „Incorrect email address or/and password.”



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

## **II Oczekiwane rezultaty:** ##  Logowanie przebiega pomyślnie. Użytkownik loguje się do aplikacji. Pod przyciskiem „Log out” znajduje się login użytkownika:”tester.123@wp.pl”



## **III Przypadek testowy:** ##

**ID:** 003

**Tytuł:**  PUzupełnienie danych w zakładce „Weight loss”  podając niepoprawną datę urodzenia(31.02.1997)
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
       Goal Weight: „66”
	5. Kliknij w opcje zaawansowane (Advanced settings (optional))
	6. Wybierz poziom aktywności w ciągu dnia (level of activity during the day): „Very low”
       7. Kliknij przycisk dalej „Next”
       

## **II Oczekiwane rezultaty:** ##  Pod polem z datą urodzenia pojawia się czerwony komunikat: „Date of birth is incorrect”. Użytkownik nie może przejść dalej
 



