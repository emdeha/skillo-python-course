import seaborn as sns
import matplotlib.pyplot as plt

sns.set_theme()

ls_one = [1, 2, 3, 4]
ls_two = [100, 200, 300, 400]

sns.relplot(
    data=[ls_one, ls_two]
)

plt.savefig("seaborn_plot.png")


