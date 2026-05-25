#  Data Analysis Cheat Sheet
## Quick Reference for Pandas, Matplotlib & Seaborn

---

## PANDAS BASICS

### Loading Data
```python
import pandas as pd

df = pd.read_csv('file.csv')           # From CSV file
df = pd.read_excel('file.xlsx')        # From Excel
df = pd.read_json('file.json')         # From JSON
df = pd.read_sql(query, connection)    # From database
```

### Viewing Data
```python
df.head()          # First 5 rows
df.head(10)        # First 10 rows
df.tail()          # Last 5 rows
df.sample(5)       # Random 5 rows
df.info()          # Column types & null values
df.describe()      # Summary statistics
df.shape           # (rows, columns)
df.columns         # Column names
df.dtypes          # Data types
```

### Selecting Data
```python
df['column_name']              # Single column (Series)
df[['col1', 'col2']]          # Multiple columns (DataFrame)
df.loc[0]                      # Row by label
df.iloc[0]                     # Row by position
df.loc[0, 'column']           # Specific cell
df[0:5]                        # First 5 rows
```

### Filtering
```python
df[df['Points'] > 25]                    # Greater than
df[df['Team'] == 'Lakers']              # Equals
df[(df['Points'] > 25) & (df['Games'] > 50)]  # AND
df[(df['Points'] > 25) | (df['Team'] == 'Lakers')]  # OR
df[df['Player'].str.contains('James')]   # String contains
df[~df['Team'].isin(['Lakers', 'Celtics'])]  # NOT in list
```

### Sorting & Ranking
```python
df.sort_values('Points')                 # Ascending
df.sort_values('Points', ascending=False)  # Descending
df.sort_values(['Points', 'Rebounds'])   # Multiple columns
df.nlargest(5, 'Points')                # Top 5 by Points
df.nsmallest(5, 'Points')               # Bottom 5 by Points
df['Points'].rank()                      # Rank (1 = highest)
```

### Grouping & Aggregation
```python
df.groupby('Team')['Points'].mean()
df.groupby('Team')['Points'].sum()
df.groupby('Team')['Points'].count()
df.groupby('Team')['Points'].max()

# Multiple aggregations
df.groupby('Team').agg({
    'Points': 'mean',
    'Rebounds': 'sum',
    'Assists': 'count'
})

# Custom names
df.groupby('Team').agg(
    avg_points=('Points', 'mean'),
    total_rebounds=('Rebounds', 'sum')
)
```

### Statistics
```python
df['Points'].mean()      # Average
df['Points'].median()    # Middle value
df['Points'].std()       # Standard deviation
df['Points'].var()       # Variance
df['Points'].min()       # Minimum
df['Points'].max()       # Maximum
df['Points'].sum()       # Total
df['Points'].count()     # Non-null count

# Correlation
df['Points'].corr(df['Rebounds'])     # Between 2 columns
df.corr()                             # All columns
```

### Creating & Modifying
```python
df['NewCol'] = df['Points'] * 2       # Create column
df['Ratio'] = df['Points'] / df['Games']  # Calculate
df.drop('column_name', axis=1)        # Remove column
df.rename(columns={'Old': 'New'})     # Rename column
df['Points'].fillna(0)                # Replace NaN with 0
df.dropna()                           # Remove rows with NaN
df.drop_duplicates()                  # Remove duplicates
```

---

##  MATPLOTLIB BASICS

### Setup
```python
import matplotlib.pyplot as plt

plt.figure(figsize=(10, 6))  # Set size (width, height)
plt.title('Title')
plt.xlabel('X Axis Label')
plt.ylabel('Y Axis Label')
plt.legend()
plt.grid(True)
plt.tight_layout()           # Auto-adjust spacing
plt.savefig('chart.png', dpi=300)  # Save
plt.show()                   # Display
```

### Simple Plots
```python
# Line chart
plt.plot(x, y)
plt.plot(x, y, marker='o', linestyle='--', linewidth=2)

# Bar chart
plt.bar(x, y)
plt.barh(x, y)  # Horizontal

# Scatter plot
plt.scatter(x, y, s=100, alpha=0.5, c='red')

# Histogram
plt.hist(data, bins=20)

# Pie chart
plt.pie(sizes, labels=labels)

# Box plot
plt.boxplot(data)
```

### Customization
```python
plt.color = 'red'           # Colors: 'r', 'b', 'g', 'yellow', '#FF5733'
plt.marker = 'o'            # 'o', 's', '^', 'x', '*'
plt.linestyle = '--'        # '-', '--', '-.', ':'
plt.alpha = 0.5             # Transparency (0-1)
plt.linewidth = 2           # Line thickness

plt.xlim(0, 100)           # Set x-axis limits
plt.ylim(0, 50)            # Set y-axis limits
plt.xticks(rotation=45)    # Rotate x labels
```

### Multiple Subplots
```python
fig, axes = plt.subplots(2, 2)  # 2 rows, 2 columns
fig, axes = plt.subplots(2, 2, figsize=(12, 10))

axes[0, 0].plot(x, y)      # Top-left
axes[0, 1].bar(x, y)       # Top-right
axes[1, 0].scatter(x, y)   # Bottom-left
axes[1, 1].hist(data)      # Bottom-right

fig.suptitle('Overall Title')
plt.tight_layout()
```

---

##  SEABORN BASICS

### Setup
```python
import seaborn as sns

sns.set_style("whitegrid")  # darkgrid, white, dark, ticks
sns.set_palette("husl")     # Color palette
```

### Common Plots
```python
# Bar plot
sns.barplot(data=df, x='Team', y='Points')
sns.barplot(data=df, x='Team', y='Points', hue='Season')

# Scatter plot
sns.scatterplot(data=df, x='Points', y='Rebounds', hue='Team')

# Line plot
sns.lineplot(data=df, x='Date', y='Points', hue='Team')

# Histogram/KDE
sns.histplot(data=df, x='Points', kde=True)

# Box plot
sns.boxplot(data=df, x='Team', y='Points')

# Violin plot
sns.violinplot(data=df, x='Team', y='Points')

# Heatmap (correlation)
sns.heatmap(df.corr(), annot=True)

# Pair plot
sns.pairplot(df)
```

---

##  COMMON PATTERNS

### Top/Bottom N
```python
top_5_points = df.nlargest(5, 'Points')
bottom_5_points = df.nsmallest(5, 'Points')
```

### Find a Record
```python
best_player = df.loc[df['Points'].idxmax()]
worst_player = df.loc[df['Points'].idxmin()]
```

### Create Categories
```python
df['Category'] = pd.cut(df['Points'], bins=[0, 20, 30, 40], labels=['Low', 'Mid', 'High'])
```

### Pivot Table
```python
pivot = df.pivot_table(
    values='Points',
    index='Team',
    columns='Season',
    aggfunc='mean'
)
```

### Merge DataFrames
```python
merged = pd.merge(df1, df2, on='Player')
merged = pd.concat([df1, df2], axis=0)  # Stack rows
```

### Apply Function
```python
df['NewCol'] = df['Points'].apply(lambda x: x * 2)
df['Category'] = df['Points'].apply(
    lambda x: 'Star' if x > 30 else 'Regular'
)
```

---

## HELPFUL TRICKS

### Check for Missing Data
```python
df.isnull().sum()                  # Count nulls per column
df.isnull().sum().sum()            # Total nulls
df[df.isnull().any(axis=1)]       # Rows with any null
```

### Unique Values
```python
df['Team'].unique()                # List of unique values
df['Team'].nunique()               # Count of unique values
df['Team'].value_counts()          # Frequency of each
```

### String Operations
```python
df['Player'].str.upper()           # Uppercase
df['Player'].str.lower()           # Lowercase
df['Player'].str.len()             # Length
df['Player'].str.contains('James') # Contains
df['Player'].str.split(' ')        # Split
```

### Type Conversion
```python
df['Points'] = df['Points'].astype(int)      # To integer
df['Date'] = pd.to_datetime(df['Date'])      # To datetime
df['Team'] = df['Team'].astype('category')   # To category
```

### Export Data
```python
df.to_csv('file.csv', index=False)
df.to_excel('file.xlsx', index=False)
df.to_json('file.json')
df.to_html('file.html')
```

---

## ANALYSIS WORKFLOW

```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. LOAD
df = pd.read_csv('data.csv')

# 2. EXPLORE
print(df.head())
print(df.info())
print(df.describe())

# 3. CLEAN
df = df.dropna()
df['Date'] = pd.to_datetime(df['Date'])

# 4. ANALYZE
top_performers = df.nlargest(10, 'Score')
avg_by_team = df.groupby('Team')['Score'].mean()
correlation = df['X'].corr(df['Y'])

# 5. VISUALIZE
plt.figure(figsize=(12, 6))
sns.barplot(data=df, x='Team', y='Score')
plt.title('Average Score by Team')
plt.savefig('result.png')
plt.show()

# 6. INTERPRET
print(f"Best team: {avg_by_team.idxmax()}")
print(f"Correlation: {correlation:.3f}")
```

---

## RESOURCES

- Pandas Documentation: https://pandas.pydata.org/docs/
- Matplotlib Documentation: https://matplotlib.org/
- Seaborn Documentation: https://seaborn.pydata.org/
- Stack Overflow: For specific errors/problems

---

##  COMMON ERRORS

| Error | Solution |
|-------|----------|
| `KeyError: 'column'` | Column name typo - check `df.columns` |
| `TypeError: unsupported operand type(s)` | Wrong data type - check `df.dtypes` |
| `ValueError: No objects to concatenate` | Check if lists/arrays are empty |
| `FileNotFoundError` | Wrong file path - use absolute path |
| `NaN` values everywhere | Check encoding: `pd.read_csv('file.csv', encoding='utf-8')` |

---

Happy analyzing! 🚀
