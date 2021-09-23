import os


def main():
    file = find("Dockerfile", "/github/workspace")
    # print(f"::set-output name=myOutput::{file_locaiton}")

def find(name, path):
    for root, dirs, files in os.walk(path):
        if name in files:
            return os.path.join(root, name)

if __name__ == "__main__":
    main()
