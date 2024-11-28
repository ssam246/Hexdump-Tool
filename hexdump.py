import os
import sys
import argparse


def display_hexdump(file_path, binary_mode=False, group_size=16):
    """
    Display a hexdump of the given file.
    
    :param file_path: Path to the file to be dumped.
    :param binary_mode: If True, displays bytes in binary instead of hex.
    :param group_size: Number of bytes per row.
    """
    try:
        with open(file_path, "rb") as file:
            file_size = os.path.getsize(file_path)
            print(f"Size {file_path}: {file_size} bytes - 0x{file_size:08x}")
            
            n = 0
            while True:
                chunk = file.read(group_size)
                if not chunk:
                    break

                # Formatting the byte values
                if not binary_mode:
                    hex_chunk = " ".join([f"{i:02x}" for i in chunk])
                    hex_chunk = insert_spacing(hex_chunk, 2 * group_size // 2 + group_size // 8)
                    width = group_size * 3
                else:
                    hex_chunk = " ".join([f"{i:08b}" for i in chunk])
                    hex_chunk = insert_spacing(hex_chunk, 8 * group_size // 2 + group_size // 8)
                    width = group_size * 9

                # Convert to ASCII representation
                ascii_chunk = "".join([chr(i) if 32 <= i <= 127 else "." for i in chunk])

                print(f"{n * group_size:08x}  {hex_chunk:<{width}}  |{ascii_chunk}|")

                n += 1

    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.", file=sys.stderr)
    except PermissionError:
        print(f"Error: Permission denied for file '{file_path}'.", file=sys.stderr)
    except Exception as e:
        print(f"Error: {type(e).__name__} - {e}", file=sys.stderr)


def insert_spacing(data, insert_position):
    """
    Inserts a space at a specified position to format the hexdump output.

    :param data: The data string to format.
    :param insert_position: Position to insert the space.
    :return: Formatted string with spacing.
    """
    if len(data) > insert_position:
        return data[:insert_position] + " " + data[insert_position:]
    return data


def parse_arguments():
    """
    Parse command-line arguments.

    :return: Parsed arguments.
    """
    parser = argparse.ArgumentParser(description="A robust hexdump tool.")
    parser.add_argument("FILE", help="File to be dumped.", type=str)
    parser.add_argument(
        "-b", "--binary", 
        help="Display bytes in binary instead of hexadecimal.", 
        action="store_true"
    )
    parser.add_argument(
        "-g", "--group-size", 
        help="Number of bytes per row (default: 16).", 
        type=int, 
        default=16
    )
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_arguments()
    if args.group_size <= 0:
        print("Error: Group size must be a positive integer.", file=sys.stderr)
        sys.exit(1)
    display_hexdump(args.FILE, args.binary, args.group_size)
