import pandas as pd
import matplotlib.pyplot as plt

# 1. Load iris.data as a DataFrame
df = pd.read_csv(r"C:\Users\heyit\Downloads\iris\iris.data", header=None)

# 2. Update column names from iris.names
df.columns = ['sepal length', 'sepal width', 'petal length', 'petal width', 'class']
print("=== DataFrame Head ===")
print(df.head())
print()

# 3. Calculate mean, min, max, and std for each column
print("=== Overall Statistics (mean, min, max, std) ===")
print("Mean:\n", df.mean(numeric_only=True))
print("\nMin:\n", df.min(numeric_only=True))
print("\nMax:\n", df.max(numeric_only=True))
print("\nStd:\n", df.std(numeric_only=True))
print()

# 4. Create class value column using pd.factorize
df['class value'] = pd.factorize(df['class'])[0]
print("=== DataFrame with 'class value' ===")
print(df.head())
print()

# 5. Group by class using .groupby()
grouped = df.groupby('class')
print("=== Grouped Object ===")
print(grouped)
print()

# 6. Extract each group by name using .get_group()
print("=== Extract Group by Name using .get_group() ===")
setosa = grouped.get_group('Iris-setosa')
print("Iris-setosa group:")
print(setosa.head())
print()

# 7. Calculate per-class statistics
print("=== Per-Class Statistics ===")
print("Per-class Mean:\n", grouped.mean(numeric_only=True))
print("\nPer-class Min:\n", grouped.min(numeric_only=True))
print("\nPer-class Max:\n", grouped.max(numeric_only=True))
print("\nPer-class Std:\n", grouped.std(numeric_only=True))
print()

# 8. Scatter plot of sepal length vs petal length
plt.figure(figsize=(8, 6))
colors = {'Iris-setosa': 'red', 'Iris-versicolor': 'blue', 'Iris-virginica': 'green'}
for name, group in grouped:
    plt.scatter(group['sepal length'], group['petal length'],
                label=name, color=colors[name], alpha=0.7)
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Petal Length (cm)')
plt.title('Iris Dataset: Sepal Length vs Petal Length')
plt.legend()
plt.tight_layout()
plt.show()

# 9. Two methods to iterate through a DataFrame row by row
print("=== Method 1: iterrows() ===")
for index, row in df.head(3).iterrows():
    print(f"Index: {index}, Sepal Length: {row['sepal length']}, Class: {row['class']}")

print("\n=== Method 2: itertuples() ===")
for row in df.head(3).itertuples():
    print(f"Index: {row.Index}, Sepal Length: {row[1]}, Class: {row[5]}")

# 10. Summary of what the statistics reveal
print("\n=== Summary of Statistical Findings ===")
summary = """
1. SETOSA IS CLEARLY SEPARABLE
   - Iris-setosa has the smallest petals (mean length 1.46 cm, width 0.25 cm),
     far below versicolor (4.26 cm, 1.33 cm) and virginica (5.55 cm, 2.03 cm).
   - Its petal measurements do not overlap with the other two classes,
     making it linearly separable on petal features alone.

2. VERSICOLOR AND VIRGINICA OVERLAP
   - These two classes share similar sepal length ranges (versicolor 4.9-7.0,
     virginica 4.9-7.9), making sepal length alone insufficient to distinguish them.
   - Petal length and petal width provide better separation, though some overlap
     remains (versicolor petal length 3.0-5.1 vs virginica 4.5-6.9).

3. FEATURE DISCRIMINATING POWER
   - Petal length has the highest overall std (1.76), indicating it varies the
     most across classes and is the strongest discriminator.
   - Sepal width has the lowest std (0.43) and is the least useful for
     distinguishing between classes.

4. VIRGINICA IS THE LARGEST OVERALL
   - Virginica has the highest mean values for sepal length (6.59 cm),
     petal length (5.55 cm), and petal width (2.03 cm).
   - It also shows the most within-class variability (highest std in most features),
     suggesting greater morphological diversity.

5. SCATTER PLOT INSIGHT
   - The sepal length vs petal length scatter plot shows three distinct clusters.
   - Setosa forms a tight, isolated cluster in the bottom-left.
   - Versicolor and virginica form partially overlapping clusters toward
     the top-right, with virginica generally having longer petals for a
     given sepal length.
"""
print(summary)
