import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("ipl_2008_to_2025.csv")
df["Match_Winner"] = df["Match_Winner"].replace({
    "Delhi Daredevils": "Delhi Capitals",
    "Rising Pune Supergiant": "Rising Pune Supergiants"
})

print(df["Match_Winner"].value_counts())
df["Match_Winner"].value_counts().plot(kind="bar", figsize=(10,5))
plt.title("Most Winning Teams in IPL (2008–2025)")
plt.xlabel("Team")
plt.ylabel("Number of Wins")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
toss_match_win = (df["Toss_Winner"] == df["Match_Winner"]).mean() * 100
print("Percentage of matches where toss winner also won the match:")
print(round(toss_match_win, 2), "%")


