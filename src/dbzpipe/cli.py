"""
The command-line interface for dbzpipe
"""
import argparse
from .dbzpipe import dbzpipe


def main():
    print('test12345')
    # parser = argparse.ArgumentParser(
    #     description="An over-simplified dbzpipe to demonstrate python packaging."
    # )
    # parser.add_argument(
    #     "url", type=str,
    #     help="The URL of the resource to be downloaded."
    # )
    # parser.add_argument(
    #     "--output", "-o",
    #     help=("Destination local file path. If not set, the resource "
    #             "will be downloaded to the current working directory, with filename "
    #             "same as the basename of the URL")
    # )
    # args = parser.parse_args()
    # file_size = download(args.url, dest_path=args.output)
    # print("Download successful! (size: {} B)".format(file_size))


if __name__ == "__main__":
    main()