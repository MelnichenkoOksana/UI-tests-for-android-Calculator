@echo off

REM Запуск Appium Server
echo Starting the Appium Server...
start "Appium Server" cmd /k appium

REM Задержка, чтобы Appium Server запустился
timeout /t 10

REM Запуск Android Emulator
echo Starting the Android Emulator...
start "Android Emulator" cmd /k emulator -avd Medium_Phone_API_33

REM Задержка, чтобы эмулятор полностью загрузился
timeout /t 40

REM Запуск тестов
echo Starting tests...
pytest calculator_tests.py

timeout /t 20

REM Остановка Appium Server
REM Завершение процессов node.exe
taskkill /F /IM node.exe
