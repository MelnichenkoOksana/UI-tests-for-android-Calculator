@echo off

REM Запуск Appium Server
echo Запуск Appium Server...
start "Appium Server" cmd /k appium

REM Задержка, чтобы Appium Server запустился
timeout /t 10

REM Запуск Android Emulator
echo Запуск Android Emulator...
start "Android Emulator" cmd /k emulator -avd Medium_Phone_API_33

REM Задержка, чтобы эмулятор полностью загрузился
timeout /t 20

REM Запуск тестов
echo Запуск тестов...
pytest calculator_tests2.py

timeout /t 20

REM Остановка Appium Server
REM Завершение процессов node.exe
taskkill /F /IM node.exe
