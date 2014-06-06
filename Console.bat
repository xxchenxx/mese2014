@echo off

:menu
cls
set ch=""
echo **************************************
echo *   1: Pip tool                      *
echo *   2: Open IDEs                     *
echo *   3: Open browser and test         *
echo *   4: Startup manage.py             *
echo *   5: CMD                           *
echo *   6: Mysql                         *
echo *   q: Exit                          *
echo **************************************
set /p ch="Please input a choice:"
cls
if /i "%ch%"=="1" goto 1
if /i "%ch%"=="2" goto 2
if /i "%ch%"=="3" goto 3
if /i "%ch%"=="4" goto 4
if /i "%ch%"=="5" goto 5
if /i "%ch%"=="6" goto 6
if /i "%ch%"=="q" goto end
goto menu

:6
mysql -uroot -p
goto menu

:5
cmd
goto menu

:1
echo Input the package name:
set /p Name=
echo You are going to install %Name%
E:\Program" "Files\Python\Scripts\pip install %Name%
pause
goto menu

:2
cls
set select=""
echo Select the IDE you need:
echo *************************************
echo *   1: Python Wing IDE              *
echo *   2: Dreamweaver                  *
echo *   3: PhotoShop                    *
echo *   4: Notepad++                    *
echo *   q: exit                         *
echo *************************************
set /p select=
if /i "%select%"=="1" goto 21
if /i "%select%"=="2" goto 22
if /i "%select%"=="3" goto 23
if /i "%select%"=="4" goto 24
if /i "%select%"=="q" goto menu
goto 2

:21
start "" "E:\Program Files\Wing IDE 101 4.1\bin\wing-101.exe"
goto 2

:22
start "" "E:\Program Files\AdobeDreamweaver_cn\Dreamweaver.exe"
goto 2

:23
start "" "E:\Program Files\Photoshop7.0\photoshop.exe"
goto 2

:24
start "" "E:\Program Files\Notepad++\notepad++.exe"
goto 2

:3
explorer.exe "http://localhost:8080"
goto menu

:4
set /p choice="manage> "
if /i "%choice%"=="exit" goto menu
if /i "%choice%"=="cls" goto cls
if /i "%choice%"=="cleardb" goto cleardb
python manage.py %choice% --traceback
echo.
goto 4
:cleardb
set /p name="Enter app name: "
mysql -uroot -p --execute="drop database app_%name%;create database app_%name%;"
goto 4
:cls
cls
goto 4

:end
@echo on