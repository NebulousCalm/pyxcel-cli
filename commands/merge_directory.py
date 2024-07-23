from console_progress_bar import console_progress_bar  # local file
import typer

import pandas as pd
import os


def merge_directory(warn: bool) -> str and bool:
    """
    Merge all files in a directory into a single file.

    :param warn: Warns potentially.
    """
    directory = typer.prompt("Directory to merge")
    sheet_name = typer.prompt("Sheet name (str or int)")
    output_file = typer.prompt("Output file (str)")
    use_same_directory = typer.confirm("Use same directory?")
    if use_same_directory:
        output_dir = directory
    else:
        output_dir = typer.prompt("Output directory")

    try:
        all_files, all_dirs = directory_files_to_array(directory)
        merge_same_sheet_names(sheet_name, all_files, directory, f'{output_file}.xlsx')
    except Exception as e:
        if warn:
            return e, False
        return None, False
    return None, True


def directory_files_to_array(directory: str, valid_files=None, dir_warning=True, include_dir=False):
    """
    Converts all files in a specified directory to an array.

    :param directory: The directory to search for files.
    :param valid_files: A list of valid file extensions to include.
    :param dir_warning: If True, prints a warning for directories found in the path.
    :param include_dir: If True, includes the full directory path in the returned file names.
    :return: A tuple containing a list of file names and a list of directory names.
    """
    if valid_files is None:
        valid_files = ['xls', 'xlsx', 'xlsb']
    returned_files = []
    directories = []

    # Get a list of all files and directories
    for root, dirs, files in os.walk(directory, topdown=False):
        total_files = len(files)
        for count, name in enumerate(files, start=1):
            file_extension = name.split('.')[-1]
            if file_extension in valid_files:
                if include_dir:
                    returned_files.append(os.path.join(root, name))
                else:
                    returned_files.append(name)
            # Update progress bar
            console_progress_bar(count, total_files, prefix='Processing files:', suffix='Complete', length=50)

        for name in dirs:
            directories.append(os.path.join(root, name))

    if dir_warning:
        for dirs in directories:
            print(f"Warning in [directory_files_to_array]: Directory '{dirs}' exists in path")

    return returned_files, directories


def merge_same_sheet_names(sheetname: int or str, workbooks, file_dir: str, output_file='concat_output.xlsx'):
    """
    Concatenate separate workbook sheets into one, ideal for merging multiple sheets of the same type.
    """

    # Check if auto delete is enabled and delete existing file if present
    autodelete = False
    output_path = os.path.join('../', output_file)
    if autodelete and os.path.exists(output_path):
        os.remove(output_path)

    dataframes = []
    total_files = len(workbooks)

    for count, file in enumerate(workbooks, start=1):
        console_progress_bar(count - 1, total_files, prefix='Merging Progress:', suffix='Complete', length=50)
        try:
            # Read the specific sheet from each workbook
            df = pd.read_excel(os.path.join(file_dir, file), sheet_name=sheetname)
            dataframes.append(df)
        except Exception as e:
            print(f"Error reading {file}: {e}")

    # Concatenate all dataframes into a single dataframe
    if dataframes:
        merged_df = pd.concat(dataframes, ignore_index=True)
        # Write merged dataframe to Excel
        merged_df.to_excel(output_path, index=False)
        console_progress_bar(total_files, total_files, prefix='Merging Progress:', suffix='Complete', length=50)
        print("Success in merging sheets.")
        return output_file
    else:
        print("No dataframes to merge.")
        return False
