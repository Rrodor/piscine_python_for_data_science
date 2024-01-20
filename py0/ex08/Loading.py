def ft_tqdm(lst: range) -> None:
    """Prints a progress bar for the given range."""
    nmax = len(lst)
    n = 0
    while n <= nmax:
        print("\r{:3.0f}%|".format(n / nmax * 100), end="")
        print("█" * int(n / nmax * 100), end="")
        print(" " * (100 - int(n / nmax * 100)), end="")
        print("| {}/{}".format(n, nmax), end="")
        yield
        n += 1
