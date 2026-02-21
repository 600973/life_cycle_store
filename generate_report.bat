@echo off
chcp 65001 >nul

:: Генерация отчётов

cd /d "%~dp0"
call venv\Scripts\activate.bat

echo === Генерация отчётов ===

echo.
echo --- Untitled.ipynb ---
jupyter nbconvert --to notebook --execute Untitled.ipynb --output Untitled.ipynb --no-input
if %errorlevel% neq 0 (
    echo [Ошибка] Не удалось сгенерировать отчёт
)

echo.
echo === Готово! ===
pause
