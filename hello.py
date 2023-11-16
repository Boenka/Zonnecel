import click
import time

@click.command()
@click.argument("name")
@click.option(
    "-c",
    "--count",
    default=1,
    help="Number of times to print greeting.",
    show_default=True,  # show default in help
)
@click.option(
    "-cp",
    "--countp",
    default=1,
    help="Number of times to print greeting.",
    show_default=True,  # show default in help
)



def hello(name,count,countp):
    for _ in range(count):
        print(f"Hello {name}!")
        time.sleep(countp)



if __name__ == "__main__":
    hello()  
