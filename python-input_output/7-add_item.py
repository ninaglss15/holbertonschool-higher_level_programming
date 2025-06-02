#!/usr/bin/python3
import sys

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


def main():
    filename = "add_item.json"

    try:
        existing_list = load_from_json_file(filename)
    except Exception:
        existing_list = []

    new_items = sys.argv[1:]

    existing_list.extend(new_items)

    save_to_json_file(existing_list, filename)


if __name__ == "__main__":
    main()
