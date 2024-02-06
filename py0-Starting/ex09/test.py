from ft_package import ft_tqdm
from time import sleep


def main():
    """test the ft_tqdm function"""
    for elem in ft_tqdm(range(333)):
        sleep(0.005)
    print()


if __name__ == "__main__":
    main()
