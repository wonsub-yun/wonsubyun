import os
# Function to rename multiple files
def main():
   i = 0
   path="/home/wonsub/Downloads/총채벌레(only 볼록)- 제주도 8.20 출장/201907251110/190613_포장_4_B/final image"
   for filename in os.listdir(path):
      my_dest =".jpg"
      my_source =path + filename
      my_dest =path + my_dest
      # rename() function will
      # rename all the files
      os.rename(my_source, my_dest)
      i += 85
# Driver Code
if __name__ == '__main__':
   # Calling main() function
   main()

