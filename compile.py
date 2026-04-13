import argparse

from compile import run_compile


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, dest="input_file")
    parser.add_argument("--output", required=True, dest="output_file")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    run_compile(args.input_file, args.output_file)


if __name__ == "__main__":
    main()
