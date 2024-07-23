import typer
import pandas as pd


def create_file(warn: bool) -> str or bool:
    """
    Creates file if it does not exist.

    :param warn: Potentially warns.
    """

    directory = typer.prompt('File directory')
    filename = typer.prompt('filename.extension')
    sample_data = typer.confirm('Populate file with sample data?')

    if sample_data:
        df = pd.DataFrame({'num_legs': [2, 4, 8, 0],
                           'num_wings': [2, 0, 0, 0],
                           'num_specimen_seen': [10, 2, 1, 8]},
                          index=['falcon', 'dog', 'spider', 'fish']
                          )

        df = df.sample(frac=2, replace=True, random_state=1)

        df.to_excel(f'{directory}/{filename}', index=False)
        return None, True
    return None, False
