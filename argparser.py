import argparse

def parse_arguments():
    default_and_required = ". Default: %(default)s, Required: %(required)s"
    parser = argparse.ArgumentParser(
        description="Script to ...")
    parser.add_argument(
        "-a", "--option_a",
        default="Hello",
        required=True,
        help="Default help" + default_and_required,
    )
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_arguments()