import os

def main():
    file = find("Dockerfile", "/github/workspace")
    print(file)
    print(f"::set-output name=myOutput::{file}")

def find(name, path):
    for root, dirs, files in os.walk(path):
        if name in files:
            return os.path.join(root, name)

if __name__ == "__main__":
    main()
