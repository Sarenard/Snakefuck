import argparse

from run import run_program


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, dest="input_file")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    run_program(args.input_file)


if __name__ == "__main__":
    main()
