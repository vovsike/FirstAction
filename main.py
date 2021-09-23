import os

def main():
    file = find("Dockerfile", "/github/workspace/")
    relative_path = "/github/workspace/"
    dockerfilelocaiton = (os.path.relpath(file, relative_path))
    print(f"::set-output name=myOutput::{dockerfilelocaiton}")

def find(name, path):
    for root, dirs, files in os.walk(path):
        if name in files:
            return os.path.join(root, name)

if __name__ == "__main__":
    main()
