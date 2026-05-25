"""
Sports Statistics Analysis & Visualization
==========================================
A beginner-friendly Python project to analyze and visualize sports data.
Uses pandas for data analysis and matplotlib/seaborn for visualizations.

Topics covered:
- Data loading and exploration
- Data cleaning and filtering
- Statistical analysis
- Data visualization
- Working with CSVs
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from io import StringIO

# Set style for better-looking plots
sns.set_style("darkgrid")
plt.rcParams['figure.figsize'] = (12, 6)

# ============================================================================
# PART 1: CREATE SAMPLE DATA
# ============================================================================

# Sample basketball player statistics data
basketball_data = """
Player,Team,Games,Points,Rebounds,Assists,FieldGoalPercent,Height_cm
LeBron James,Lakers,56,27.2,7.9,7.2,52.3,203
Stephen Curry,Warriors,56,29.4,5.2,6.5,47.8,190
Kevin Durant,Suns,55,29.1,6.5,5.0,58.5,206
Giannis Antetokounmpo,Bucks,55,31.1,11.8,5.7,58.8,211
Luka Doncic,Mavericks,55,28.4,9.6,8.0,49.7,201
Joel Embiid,76ers,51,33.1,10.2,3.5,54.8,213
Jayson Tatum,Celtics,56,30.1,8.8,3.6,47.4,203
Damian Lillard,Trail Blazers,55,32.2,4.8,7.3,43.2,188
Devin Booker,Suns,56,28.3,4.5,6.9,49.1,198
Kawhi Leonard,Clippers,52,23.8,3.5,3.2,49.4,201
"""

# Create DataFrame from CSV string
df = pd.read_csv(StringIO(basketball_data))

print("=" * 70)
print("SPORTS STATISTICS ANALYSIS & VISUALIZATION")
print("=" * 70)
print()

# ============================================================================
# PART 2: DATA EXPLORATION
# ============================================================================

print("📊 PART 1: DATA EXPLORATION")
print("-" * 70)

print("\n1. First few rows of data:")
print(df.head())

print("\n2. Data Info:")
print(df.info())

print("\n3. Basic Statistics:")
print(df.describe())

print("\n4. Data Shape:")
print(f"Total players: {df.shape[0]}, Total columns: {df.shape[1]}")

# ============================================================================
# PART 3: DATA ANALYSIS
# ============================================================================

print("\n\n📈 PART 2: DATA ANALYSIS")
print("-" * 70)

# Find top scorers
print("\n5. Top 5 Scorers:")
top_scorers = df.nlargest(5, 'Points')[['Player', 'Points', 'Team']]
print(top_scorers.to_string(index=False))

# Find best rebounders
print("\n6. Top 5 Rebounders:")
top_rebounders = df.nlargest(5, 'Rebounds')[['Player', 'Rebounds', 'Team']]
print(top_rebounders.to_string(index=False))

# Find best shooters
print("\n7. Top 5 Best Field Goal Percentage:")
top_shooters = df.nlargest(5, 'FieldGoalPercent')[['Player', 'FieldGoalPercent', 'Team']]
print(top_shooters.to_string(index=False))

# Team performance summary
print("\n8. Average Points by Team:")
team_avg = df.groupby('Team')['Points'].mean().sort_values(ascending=False)
print(team_avg)

# Calculate correlation between height and points
correlation = df['Height_cm'].corr(df['Points'])
print(f"\n9. Correlation between Height and Points: {correlation:.3f}")
print(f"   (Ranges from -1 to 1. 0.3+ suggests a relationship)")

# ============================================================================
# PART 4: VISUALIZATIONS
# ============================================================================

print("\n\n🎨 PART 3: CREATING VISUALIZATIONS...")
print("-" * 70)

# Create a figure with multiple subplots
fig, axes = plt.subplots(2, 2, figsize=(15, 12))
fig.suptitle('Basketball Players Statistical Analysis', fontsize=16, fontweight='bold', y=1.00)

# Plot 1: Top 10 Scorers
ax1 = axes[0, 0]
top_10 = df.nlargest(10, 'Points')
ax1.barh(top_10['Player'], top_10['Points'], color='steelblue')
ax1.set_xlabel('Points Per Game', fontweight='bold')
ax1.set_title('Top 10 Scorers', fontweight='bold', pad=10)
ax1.invert_yaxis()
for i, v in enumerate(top_10['Points']):
    ax1.text(v + 0.5, i, f'{v:.1f}', va='center', fontsize=9)

# Plot 2: Points vs Rebounds
ax2 = axes[0, 1]
scatter = ax2.scatter(df['Points'], df['Rebounds'], s=200, alpha=0.6, c=df['Assists'], cmap='viridis')
for idx, row in df.iterrows():
    ax2.annotate(row['Player'].split()[0], 
                (row['Points'], row['Rebounds']),
                fontsize=8, alpha=0.7)
ax2.set_xlabel('Points Per Game', fontweight='bold')
ax2.set_ylabel('Rebounds Per Game', fontweight='bold')
ax2.set_title('Points vs Rebounds (colored by Assists)', fontweight='bold', pad=10)
cbar = plt.colorbar(scatter, ax=ax2)
cbar.set_label('Assists', fontweight='bold')

# Plot 3: Field Goal Percentage Distribution
ax3 = axes[1, 0]
ax3.hist(df['FieldGoalPercent'], bins=8, color='coral', edgecolor='black', alpha=0.7)
ax3.axvline(df['FieldGoalPercent'].mean(), color='red', linestyle='--', linewidth=2, label=f'Mean: {df["FieldGoalPercent"].mean():.1f}%')
ax3.set_xlabel('Field Goal Percentage (%)', fontweight='bold')
ax3.set_ylabel('Number of Players', fontweight='bold')
ax3.set_title('Distribution of Field Goal Percentage', fontweight='bold', pad=10)
ax3.legend()

# Plot 4: Height vs Points (Scatter with trend line)
ax4 = axes[1, 1]
ax4.scatter(df['Height_cm'], df['Points'], s=150, alpha=0.6, color='green')
# Add trend line
z = np.polyfit(df['Height_cm'], df['Points'], 1)
p = np.poly1d(z)
ax4.plot(df['Height_cm'], p(df['Height_cm']), "r--", linewidth=2, label='Trend Line')
ax4.set_xlabel('Height (cm)', fontweight='bold')
ax4.set_ylabel('Points Per Game', fontweight='bold')
ax4.set_title(f'Height vs Points (Correlation: {correlation:.3f})', fontweight='bold', pad=10)
ax4.legend()

plt.tight_layout()
plt.savefig('/mnt/user-data/outputs/sports_analysis_visualizations.png', dpi=300, bbox_inches='tight')
print("✅ Saved: sports_analysis_visualizations.png")

# Create additional visualization: Team comparison
fig2, ax = plt.subplots(figsize=(12, 6))
team_data = df.groupby('Team')[['Points', 'Rebounds', 'Assists']].mean().sort_values('Points', ascending=False)
team_data.plot(kind='bar', ax=ax, color=['#FF6B6B', '#4ECDC4', '#45B7D1'])
ax.set_title('Average Statistics by Team', fontweight='bold', fontsize=14, pad=15)
ax.set_xlabel('Team', fontweight='bold')
ax.set_ylabel('Average per Game', fontweight='bold')
legend = ax.legend(title='Statistics')
legend.get_title().set_fontweight('bold')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig('/mnt/user-data/outputs/team_comparison.png', dpi=300, bbox_inches='tight')
print("✅ Saved: team_comparison.png")

plt.show()

# ============================================================================
# PART 5: SUMMARY STATISTICS
# ============================================================================

print("\n\n📋 PART 4: SUMMARY STATISTICS")
print("-" * 70)

print("\nTop Player by Different Metrics:")
print(f"Highest Scorer: {df.loc[df['Points'].idxmax(), 'Player']} ({df['Points'].max():.1f} PPG)")
print(f"Best Rebounder: {df.loc[df['Rebounds'].idxmax(), 'Player']} ({df['Rebounds'].max():.1f} RPG)")
print(f"Best Passer: {df.loc[df['Assists'].idxmax(), 'Player']} ({df['Assists'].max():.1f} APG)")
print(f"Best Shooter: {df.loc[df['FieldGoalPercent'].idxmax(), 'Player']} ({df['FieldGoalPercent'].max():.1f}% FG%)")

print("\n" + "=" * 70)
print("Analysis Complete! Check the saved PNG files for visualizations.")
print("=" * 70)
