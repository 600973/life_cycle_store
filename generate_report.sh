#!/bin/bash

# Генерация отчётов

cd "$(dirname "$0")"
source venv/bin/activate

echo "=== Генерация отчётов ==="

echo ""
echo "--- Untitled.ipynb ---"
jupyter nbconvert --to notebook --execute Untitled.ipynb --output Untitled.ipynb --no-input
if [ $? -ne 0 ]; then
    echo "[Ошибка] Не удалось сгенерировать отчёт"
fi

echo ""
echo "=== Готово! ==="
