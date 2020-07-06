import altair as alt
from vega_datasets import data
alt.renderers.enable('altair_viewer')
import matplotlib.pyplot as plt
import matplotlib.patches
import pandas as pd
import numpy as np


# demo chart
def demo_donut_chart():
    # Make data: I have 3 groups and 7 subgroups
    group_names = ['groupA', 'groupB', 'groupC']
    group_size = [12, 11, 30]
    subgroup_names = ['A.1', 'A.2', 'A.3', 'B.1', 'B.2', 'C.1', 'C.2', 'C.3', 'C.4', 'C.5']
    subgroup_size = [4, 3, 5, 6, 5, 10, 5, 5, 4, 6]
    subgroup_names_legs=['A.1:a1desc', 'A.2:a2desc', 'A.3:a3desc',
    'B.1:b1desc', 'B.2:b2desc', 'C.1:c1desc', 'C.2:c2desc', 'C.3:c3desc',
    'C.4:c4desc', 'C.5:c5desc']

    # Create colors
    a, b, c = [plt.cm.Blues, plt.cm.Reds, plt.cm.Greens]

    # First Ring (outside)
    fig, ax = plt.subplots()
    ax.axis('equal')
    mypie, _ = ax.pie(group_size, radius=1.3, labels=group_names, colors=[a(0.6), b(0.6), c(0.6)])
    plt.setp(mypie, width=0.3, edgecolor='white')

    # Second Ring (Inside)
    mypie2, _ = ax.pie(subgroup_size, radius=1.3 - 0.3, labels=subgroup_names, labeldistance=0.7,
                       colors=[a(0.5), a(0.4), a(0.3), b(0.5), b(0.4), c(0.6), c(0.5), c(0.4), c(0.3), c(0.2)])
    plt.setp(mypie2, width=0.4, edgecolor='white')
    plt.margins(0, 0)

    plt.legend(loc=(0.9, 0.1))
    handles, labels = ax.get_legend_handles_labels()

    ax.legend(handles[3:], subgroup_names_legs, loc=(0.9, 0.1))
    # show it
    plt.show()


def draw_simple_bar():
    x = ['Nuclear', 'Hydro', 'Gas', 'Oil', 'Coal', 'Biofuel']
    energy = [5, 6, 15, 22, 24, 8]

    x_pos = [i for i, _ in enumerate(x)]

    plt.bar(x_pos, energy, color='green')
    plt.xlabel("Energy Source")
    plt.ylabel("Energy Output (GJ)")
    plt.title("Energy output from various fuel sources")

    plt.xticks(x_pos, x)

    plt.show()


def draw_hbar():
    df = pd.DataFrame({'Name': np.random.choice(list('AABBBBBCCCCCDEEF'), 20000)})
    y = df['Name'].value_counts(ascending=False)
    print(y)
    fig, ax = plt.subplots(figsize=(12, 5))
    ax.barh(y.index, y, height=0.75, color="slateblue")
    plt.title('Count of supplies')
    plt.xlabel('Count')
    plt.ylabel('ylabel')
    _, xmax = plt.xlim()
    plt.xlim(0, xmax + 300)
    for i, v in enumerate(y):
        ax.text(v + 100, i, str(v), color='black', fontweight='bold', fontsize=14, ha='left', va='center')
    plt.show()


def draw_stack_bar():
    source = data.barley()[:20]
    print(source)

    chart = alt.Chart(source).mark_bar().encode(
        x='sum(yield)',
        y='variety',
        color='site'
    ).properties(
        width=600,
        height=450
    )
    chart.show()


def draw_simple_pie():
    # Pie chart, where the slices will be ordered and plotted counter-clockwise:
    labels = 'Frogs', 'Hogs', 'Dogs', 'Logs'
    sizes = [15, 30, 45, 10]
    explode = (0, 0.1, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')

    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
            shadow=True, startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    plt.show()


def draw_multiple_pies():
    df = pd.DataFrame(dict(
        Business='Beauty & Spas;Burgers-Restaurants;Pizza;Mexican Restaurants;Modern European-Restaurants;Chineese'.split(
            ';'),
        aniticipation=[0] * 6,
        enjoyment=[6., 1., 6., 33., 150., 19.5],
        sad=[1., 2., 1., 3., 13.5, 0.],
        disgust=[1, 1, 0, 3, 37, 3],
        anger=[1.5, 2., 4., 9., 19., 3.],
        surprise=[3, 0, 0, 2, 12, 1],
        fear=[0, 1, 1, 9, 22, 1],
        trust=[0] * 6
    ))
    fig, axes = plt.subplots(2, 3, figsize=(10, 6))

    for i, (idx, row) in enumerate(df.set_index(keys='Business').iterrows()):
        ax = axes[i // 3, i % 3]
        row = row[row.gt(row.sum() * .01)]
        ax.pie(row, labels=row.index, startangle=30)
        ax.set_title(idx)

    fig.subplots_adjust(wspace=.2)
    plt.show()


if __name__ == '__main__':
    draw_stack_bar()
    # draw_simple_pie()
    # draw_multiple_pies()
    # draw_hbar()