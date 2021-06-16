# Automatyzacja przypadku testowego dla aplikacji mobilnej Android(Fitatu) przy pomocy Appium


## **I Przypadek testowy:** ##

**ID:** 001

**Tytuł:**  Logowanie się użytkownika używając nieprawidłowego adresu e-mail
Plik: 01test_fitatu.py Klasa: Test1Appium Metoda: testIncorrectEmail

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


**Kroki:**
       1. Otwórz aplikację Fitatu.apk
       2. Zamknij komunikat „Intent Filter Verification Service has stopped”
       3. Wybierz z menu głównego przycisk logowania „Log in”
       4. Kliknij ponownie przycisk „Log in”
       5. Wpisz nieprawidłowy adres e-mail: „tester.135@wp.pl”
       6. Wpisz hasło: „Testy123”
       7. Kliknij przycisk „Log in”

## **II Oczekiwane rezultaty:** ##  Logowanie użytkownika nie powiodło się. Użytkownik otrzymał komunikat:” Login error” „Incorrect email address or/and password.”
 



