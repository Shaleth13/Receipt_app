def get_summary_stats(df):
    return {
        "Total Spend": df["amount_clean"].sum(),
        "Average Spend": df["amount_clean"].mean(),
        "Median Spend": df["amount_clean"].median()
    }
get_summary_stats(df)

top_vendors = df['vendor'].value_counts().head(5)
top_vendors.plot(kind='bar', title="Top Vendors by Frequency")

vendor_spend = df.groupby('vendor')['amount_clean'].sum().sort_values(ascending=False).head(5)
vendor_spend.plot(kind='bar', title="Top Vendors by Spend", color='orange')

df['date_parsed'] = pd.to_datetime(df['date'], format='%d/%m/%Y', errors='coerce')
monthly = df.groupby(df['date_parsed'].dt.to_period("M"))['amount_clean'].sum()

monthly.plot(kind='line', title="Monthly Spend Trend", marker='o')
