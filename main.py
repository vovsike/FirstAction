import os


def main():
    my_output = os.listdir('/')
    print(f"::set-output name=myOutput::{my_output}")

if __name__ == "__main__":
    main()
