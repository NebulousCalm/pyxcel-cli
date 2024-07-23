import typer
import pandas as pd


def drop_col(warn: bool) -> str or bool or None:
    """
    Drops specified columns from an Excel file and resaves the file.
    """

    directory = typer.prompt('Filename directory')
    filename = typer.prompt('filename.extension')
    sheetname = typer.prompt('sheet name')
    drop_column = typer.prompt('drop column')

    try:
        df = pd.read_excel(filename, sheet_name=sheetname)
        df.drop(drop_column, axis=1, inplace=True)

        df.to_excel(filename, sheet_name=sheetname, index=False)
    except Exception as e:
        print(f'Error dropping columns: {e}')
