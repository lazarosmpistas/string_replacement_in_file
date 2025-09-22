import sys
from pathlib import Path

def main(old_path, new_path, str_to_replace, new_str):
    #filename = old_path.split('/')[-1]

    old_p = Path(old_path)
    if not old_p.is_file():
        print('No such file in this location')
        return

    #filename = old_p.name
    with open(old_p, "r") as f:
        string = f.read()

    string = string.replace(str_to_replace, new_str)

    new_p = Path(new_path)
    Path(new_p.parent).mkdir(parents=True, exist_ok=True)

    with open(new_p, "w") as f:
        f.write(string)
        print(f"your new file is at {new_p}")

if __name__ == "__main__":
    if len(sys.argv) != 5 :
        print("Usage: python string_replacer.py <old_filepath> <new_filepath> <string_to_change> <new_string>")
        sys.exit(1)
    main(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
