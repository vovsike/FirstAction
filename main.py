import os


def main():
    print(list_files("/github"))
    path_to_search = "/github/workspace/"
    print(path_to_search)
    file_locaiton = find_files("Dockerfile", "path_to_search")
    print(file_locaiton)
    print(f"::set-output name=myOutput::{file_locaiton}")

def find_files(filename, search_path):
   result = []

   for root, dir, files in os.walk(search_path):
      if filename in files:
         result.append(os.path.join(root, filename))
   return result

def list_files(startpath):
    for root, dirs, files in os.walk(startpath):
        level = root.replace(startpath, '').count(os.sep)
        indent = ' ' * 4 * (level)
        print('{}{}/'.format(indent, os.path.basename(root)))
        subindent = ' ' * 4 * (level + 1)
        for f in files:
            print('{}{}'.format(subindent, f))

if __name__ == "__main__":
    main()
