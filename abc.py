import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("city.csv")
print(df)

plt.figure(figsize=(10, 6))
plt.bar(df['city'], df['population'])
plt.xlabel('city')
plt.ylabel('population')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

