import matplotlib.pyplot as plt
import psutil
import subprocess
import sys
import tabulate

def create_table(data):
    table = []
    for i in range(len(data)):
        table.append([0.1 * i] + data[i])
    headers = ["Time"]
    for i in range(psutil.cpu_count()):
        headers.append("CPU" + str(i))
    print("\n" + tabulate.tabulate(table, headers, floatfmt=".2f") + "\n")

def create_plot(data):
    fig, ax = plt.subplots(psutil.cpu_count(), sharex=True, sharey=True)
    for c in range(psutil.cpu_count()):
        x = []
        y = []
        for i in range(len(data)):
            x.append(0.1 * i)
            y.append(data[i][c])
        ax[c].fill_between(x, y, label="CPU"+str(c))
        ax[c].legend(loc="center left", bbox_to_anchor=(1, 0.5))
    fig.text(0.5, 0.07, "Time (seconds)", ha="center")
    fig.text(0.06, 0.5, "Usage (percent)", va="center", rotation="vertical")
    plt.xlim([0.0, 0.1 * (len(data) - 1)])
    plt.ylim([0, 100])
    plt.yticks([0, 50, 100], ["", "50%", ""])
    plt.show()

if __name__ == "__main__":
    data = [psutil.cpu_percent(interval=0.1, percpu=True)]
    proc = subprocess.Popen([sys.executable, sys.argv[1]])
    while proc.poll() is None:
        data.append(psutil.cpu_percent(interval=0.1, percpu=True))
    create_table(data)
    create_plot(data)
