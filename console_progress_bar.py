def console_progress_bar(iteration, total, prefix='', suffix='', decimals=1, length=50, fill='█', print_end="\r") -> \
        None:
    """
    Call in a loop to create terminal progress bar

    :param iteration: Current iteration.
    :param total: Total iterations.
    :param prefix: Prefix string.
    :param suffix: Suffix string.
    :param decimals: Positive number of decimals in percent complete.
    :param length: Character length of bar.
    :param fill: Bar fill character.
    :param print_end: End character.
    """

    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filled_length = int(length * iteration // total)
    bar = fill * filled_length + '-' * (length - filled_length)
    print(f'\r{prefix} |{bar}| {percent}% {suffix}', end=print_end)
    # Print New Line on Complete
    if iteration == total:
        print()
