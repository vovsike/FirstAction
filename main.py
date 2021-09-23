import os


def main():
    path_to_search = os.listdir("/github")
    file_locaiton = find_files("Dockerfile", "path_to_search")
    print(f"::set-output name=myOutput::{path_to_search}")

def find_files(filename, search_path):
   result = []

   for root, dir, files in os.walk(search_path):
      if filename in files:
         result.append(os.path.join(root, filename))
   return result

if __name__ == "__main__":
    main()
