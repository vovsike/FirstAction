import os
import json

def main():
    new_l = []
    files_list = find("Dockerfile", "/github/workspace/")
    print(files_list)
    for path in files_list:
        docker_dict={}
        relative_path = "/github/workspace/"
        dockerfilelocaiton = (os.path.relpath(path, relative_path))
        print(os.path.dirname(dockerfilelocation))
        docker_dict["DockerFile"] = dockerfilelocaiton
        new_l.append(docker_dict)
    # relative_path = "/github/workspace/"
    # dockerfilelocaiton = (os.path.relpath(file, relative_path))
    # print(f"::set-output name=myOutput::{dockerfilelocaiton}")
    print(new_l)
    # new_l = [{"DockerName":"docker/Dockerfile"},{"DockerName":"docker/Dockerfile"}]
    # print(f"::set-output name=myOutput::{list(new_l)}")


def find(name, path):
    files_l = []
    for root, dirs, files in os.walk(path):
        if name in files:
            files_l.append(os.path.join(root, name))
    return files_l

if __name__ == "__main__":
    main()
