import csv

import click
import matplotlib.pyplot as plt
import pandas as pd

from pythondaq.DiodeExperiment import DiodeExperiment, list_devices


@click.group()
def cmd_group():
    pass

@cmd_group.command()
@click.option(
    "-p",
    "--port",
    default = None,
    show_default=True,  # show default in help
    help=  "the port to which the arduino is connected"
)
@click.option(
    "-s",
    "--start",
    default= 0.0,
    show_default=True,  # show default in help
    help = 'the volt value from which to start the experiment (value between 0-3.3)'
)
@click.option(
    "-e",
    "--end",
    default= 3.3,
    show_default=True,  # show default in help
    help = 'the volt value at which to end the experiment (value between 0-3.3)'
)
@click.option(
    "-r",
    "--rep",
    default= 3,
    show_default=True,  # show default in help
    help = 'the amount of times each volt value should be tested to calc std and mean (int)'
)
@click.option(
    "-o",
    "--output",
    default= None,
    show_default=True,  # show default in help
    help = "-o FILENAME (without extention) to save the raw data in a csv file."
)
@click.option('--graph/--no-graph', help = 'type --graph to show a errorbar graph of the results', default=False)


def scan(port, start, end, rep, graph, output):
    """
    Start a loop that tests from a start and stop value between volt values 0-3.3. This will be repeated rep times and is the amount of data used to caluclate the mean and standart deviation of each point. It is also possible to graph the function and to save it as a csv file.
    """

    if port is None or not int:
        return print("Give a value for the port with 'diode scan -p [value]'")

    else:
        Begin = DiodeExperiment(port)
        test1 = Begin.scan(int(start * (1023/3.3)), int(end * (1023/3.3)), rep)

        df = pd.DataFrame({"U in [V]": test1[0], "I in [A]": test1[1]})
        print(df)

        if output is not None:
            zipped_data = zip(test1[0],test1[1], test1[2], test1[3])
            with open(f'{output}.csv', 'w', newline='') as csvfile:
                writer = csv.writer(csvfile, lineterminator= '\n')
                writer.writerow([
                    'Voltage in [V]',
                    'Amperage in [A]',
                    'Error on the voltage',
                    'Error on the Amperage'
                ])
                writer.writerows(zipped_data)


        if graph:
            plt.xlabel("Voltage in [V]")
            plt.ylim
            plt.ylabel("Amperage in [A]")
            plt.errorbar(x = test1[0] ,y = test1[1] ,xerr = test1[2], yerr= test1[3], linestyle='')
            plt.show()
        return



@cmd_group.command()
def list():
    """
    Lists the devices currently connected.
    """
    return list_devices()


@cmd_group.command()
@click.option(
    "-n",
    "--port",
    default= None,
    show_default=True,  # show default in help
    help = "the port to which the device is connected (int)"
)

def info(port):
    
    """
    Prints the identification string of the device connected

    arg = the port you want info on (int)
    """

    if port is None or not int:
        return print("Give a value for the port with 'diode scan -p [value]'")

    else:
        Begin = DiodeExperiment(port)
        return print(Begin.iden())

if __name__ == "__main__":
    cmd_group()
