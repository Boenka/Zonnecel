import click
import matplotlib.pyplot as plt
import numpy as np
from numpy import pi
import csv
import pyvisa 
from pythondaq.DiodeExperiment import DiodeExperiment

@click.group()
def cmd_group():
    pass

@cmd_group.command()
@click.option(
    "-p",
    "--port",
    default = None,
    show_default=True,  # show default in help
)
@click.option(
    "-s",
    "--start",
    default= 0,
    show_default=True,  # show default in help
)
@click.option(
    "-e",
    "--end",
    default= 3.3,
    show_default=True,  # show default in help
)
@click.option(
    "-r",
    "--rep",
    default= 3,
    show_default=True,  # show default in help
)
@click.option(
    "-y",
    "--hold",
    default= None,
    show_default=True,  # show default in help
)
@click.option('--graph/--no-graph', default=False)


def scan(port, start, end, rep, graph, hold):
    """Calculate sin up until input.

    Args:
        number (int): 0 - 2*pi
    """

    if port is None:
        return print("Give a value for the port with 'diode scan -p [value]'")

    else:
        Begin = DiodeExperiment(port)
        test1 = Begin.scan(int(start * (1023/3.3)), int(end * (1023/3.3)), rep)

        print(test1[0])
        print(test1[1])


        if hold is not None:
            zipped_data = zip(test1[0],test1[1])
            with open(f'{hold}.csv', 'w', newline='') as csvfile:
                writer = csv.writer(csvfile, lineterminator= '\n')
                writer.writerow([
                    'Voltage in [V]',
                    'Amperage in [A]',
                    'Error on the voltage',
                    'Error on the Amperage'
                ])
                writer.writerows(zipped_data)


        plt.xlabel("Voltage in [V]")
        plt.ylim
        plt.ylabel("Amperage in [A]")
        plt.errorbar(x = test1[0] ,y = test1[1] ,xerr = test1[2], yerr= test1[3], linestyle='')

        return

@cmd_group.command()
def list():
    rm = pyvisa.ResourceManager("@py")
    ports = rm.list_resources()
    return print(ports)

@cmd_group.command()
@click.option(
    "-n",
    "--port",
    default=9,
    show_default=True,  # show default in help
)

def info(port):
    """Calculate the tan up until input.

    Args:
        number (int): 0 - 2*pi
    """
    Begin = DiodeExperiment(port)
    
    return print(Begin.iden())

if __name__ == "__main__":
    cmd_group()