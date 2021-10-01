import os
import json

def main():
    files_list = find("Dockerfile", "/github/workspace/")
    print(files_list)
    # relative_path = "/github/workspace/"
    # dockerfilelocaiton = (os.path.relpath(file, relative_path))
    # print(f"::set-output name=myOutput::{dockerfilelocaiton}")
    new_l = [{"DockerName":"docker/Dockerfile"},{"DockerName":"docker/Dockerfile"}]
    print(f"::set-output name=myOutput::{list(new_l)}")


def find(name, path):
    files_l = []
    for root, dirs, files in os.walk(path):
        if name in files:
            files_l.append(os.path.join(root, name))
    return files_l

if __name__ == "__main__":
    main()
