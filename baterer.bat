@echo off
setlocal
setlocal EnableDelayedExpansion
set extension = !RANDOM!!RANDOM!!RANDOM!!RANDOM!
type %1 > temp%extension%.bat
call temp%extension%.bat
del /q /f temp%extension%.bat
endlocal
