import pandas as pd
import numpy as np

np.random.seed(42)

stores = [f'Магазин {i}' for i in range(1, 6)]

# Все магазины начинаются с 1-й недели, но заканчиваются в разные
end_weeks = {
    'Магазин 1': 15,  # все 15 недель
    'Магазин 2': 15,  # все 15 недель
    'Магазин 3': 12,  # до 12-й недели
    'Магазин 4': 10,  # до 10-й недели
    'Магазин 5': 7,   # до 7-й недели
}

week_cols = [f'Неделя {i}' for i in range(1, 16)]

data = []
for store in stores:
    end = end_weeks[store]
    base = np.random.randint(50000, 150000)
    row = []
    for w in range(15):
        if w >= end:
            row.append(np.nan)
        else:
            trend = base + w * np.random.randint(500, 3000)
            noise = np.random.randint(-10000, 10000)
            row.append(max(0, trend + noise))
    data.append(row)

df = pd.DataFrame(data, columns=week_cols)
df.insert(0, 'Магазин', stores)

df.to_excel('weekly_sales.xlsx', index=False)
print(df.to_string(index=False))
print(f'\nФайл weekly_sales.xlsx создан: {len(stores)} магазинов, {len(week_cols)} недель')
