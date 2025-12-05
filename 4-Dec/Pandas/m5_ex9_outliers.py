
import pandas as pd

df = pd.DataFrame({
    'customer_id': [1, 2, 3, 4, 5, 6, 7],
    'Amount': [3000, 3500, 4000, 4500, 5000, 85000, 120],   # 85000 is an outlier
    'Items': [3, 4, 5, 6, 7, 50, 1]                        # 50 is an outlier
})

def remove_outliers_iqr(dataframe, cols):
    cleaned = dataframe.copy()
    mask = pd.Series([True] * len(cleaned), index=cleaned.index)
    bounds = {}

    for col in cols:
        q1 = cleaned[col].quantile(0.25)
        q3 = cleaned[col].quantile(0.75)
        iqr = q3 - q1
        lower = q1 - 1.5 * iqr
        upper = q3 + 1.5 * iqr
        bounds[col] = (lower, upper)
        mask &= cleaned[col].between(lower, upper, inclusive='both')

    return cleaned[mask], bounds

cleaned_df, iqr_bounds = remove_outliers_iqr(df, cols=['Amount', 'Items'])

print("IQR bounds per column:")
print(iqr_bounds)
print("\nCleaned dataset (outliers removed):")
print(cleaned_df)
