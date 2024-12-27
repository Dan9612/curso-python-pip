import matplotlib.pyplot as plt

def generate_bar_charts(labels, values):
    fig, ax = plt.subplots()
    ax.bar(labels, values)
    plt.savefig('bar.png')
    plt.close()


def generate_pie_charts(labels, values):
    fig, ax = plt.subplots()
    ax.pie(values, labels=labels)
    ax.axis('equal')
    plt.savefig('pie2.png')
    plt.close()


if __name__ == '__main__':
    labels = [ 'a', 'b', 'c']
    values = [ 40, 500, 150]
    # generate_bar_charts(labels, values)
    generate_pie_charts(labels, values)
