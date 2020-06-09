mode 163,5
%SystemRoot%\System32\choice.exe /C YN /N /M "Have set the token on the main.py [Y/N]? "
if errorlevel 2 goto :EOF

endlocal
echo off
color f
set counter=0
set counterb=000
set core=
set "valuecore=                                                                                                                                                                "
setLocal EnableDelayedExpansion
:start
cls
echo.ÉÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄ»
echo.³%valuecore:~0,160%³
echo.ÈÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄ¼
if %counter% GEQ 160 set msg=complete& set counterb=10000& goto exit
echo. %counterb:~0,-2%%%
set /a counter=counter+1
set /a counterb=counterb+62
set "valuecore=!core:~0,%counter%!                                                                                                                                                                "
set delay=0
:delay
if %delay%==200 goto start
set /a delay=delay+1
goto delay
:exit
echo. %counterb:~0,-2%%% %msg%
cls
echo Thank you for launching the Radiant Bot
echo Credits to Adelenade and Heliferepo
pause
mode 100,50
python3 src\main.py
pause