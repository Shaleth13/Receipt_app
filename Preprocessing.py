# Remove ₹ or commas, convert to float
def preprocess_dataframe(df):
  df['amount_clean'] = df['amount'].str.replace('₹', '').str.replace(',', '').astype(float)
  df["amount_Clean"] = pd.to_numeric(df["amount_Clean"], errors="coerce")

# Parse date from dd/mm/yyyy to datetime
  df["parsed_Date"] = pd.to_datetime(df["date"], format="%d/%m/%Y", errors="coerce")

  return df

# Get top N vendors by frequency
def get_top_vendors_by_frequency(df, n=5):
    return df["vendor"].value_counts().head(n)

# Get top N vendors by spend
def get_top_vendors_by_spend(df, n=5):
    return df.groupby("vendor")["amount_clean"].sum().sort_values(ascending=False).head(n)

# Get monthly spend trend
def get_monthly_spend_trend(df):
    if "parsed_Date" not in df.columns:
        df = preprocess_dataframe(df)
    monthly = df.groupby(df["parsed_Date"].dt.to_period("M"))["amount_Clean"].sum()
    return monthly
