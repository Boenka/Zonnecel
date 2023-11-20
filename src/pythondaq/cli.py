import click
import numpy as np
from numpy import pi
import pandas as pd


@click.group()
def cmd_group():
    pass

@cmd_group.command("list")
@click.option(
    "-n",
    "--number",
    default=1,
    show_default=True,  # show default in help
)

def list(number):
    """Calculate sin up until input.

    Args:
        number (int): 0 - 2*pi
    """
    x = np.linspace(0, 2 * pi, number)
    df = pd.DataFrame({"x": x, "sin (x)": np.sin(x)})
    print(df)
    return

@cmd_group.command("scan")
@click.option(
    "-n",
    "--number",
    default=1,
    show_default=True,  # show default in help
)

def scan(number):
    """Calculate the tan up until input.

    Args:
        number (int): 0 - 2*pi
    """
    print('hoppa')
    return

if __name__ == "__main__":
    cmd_group()