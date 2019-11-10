import os
import sys
# Function to rename multiple files
iter_num = 1
fix_name = "helpme"
# "/home/wonsub/Downloads/총채벌레(only 볼록)- 제주도 8.20 출장/"
path = os.getcwd()
print(path)
a = os.listdir(path)
big_path_list = []
sub_dir = []
for i in range(2):
    sub_dir = os.listdir(a[i])
    for dirs in sub_dir:
        checkdir = path + "/" + a[i]+ "/"  + dirs + "/final image/"
        big_path_list.append(checkdir)

print(big_path_list)

for folder in big_path_list:
    if ".py" not in folder:
        filelist = os.listdir(folder)
        for i in range(7):
            checkxml = "Merged_image" + str(i+1) + ".xml"
            checkjpg = "Merged_image" + str(i+1) + ".jpg"
            check_full_path = [folder + checkxml, folder + checkjpg]
            changing_name = [folder + fix_name + str(iter_num) + ".xml" , folder + fix_name + str(iter_num) + ".jpg"]
            if os.path.isfile(check_full_path[0]):
                # for xml
                os.rename(check_full_path[0], changing_name[0])
                # for jpg
                os.rename(check_full_path[1], changing_name[1])
                iter_num += 1
            # if '.jpg' in filelist:
            #     jpglist.append(os.path.join(folder, filelist))
            # elif '.xml' in filelist:
            #     xmllist.append(os.path.join(folder, filelist))

print(fix_name)
    # os.rename(, my_dest)
    # iter_num += 1


# wonsub homework
# sub_dir = os.walk(path)
# for dir in sub_dir:
#     if iter_num < 4:
#         print(dir)
#         iter_num += 1
#     else:
#         break
# path="201907251110/190613_포장_4_B/final image"
# for filename in os.listdir(path):
#     my_dest =".jpg"
#     my_source =path + filename
#     my_dest =path + my_dest
#     # rename() function will
#     # rename all the files
#     os.rename(my_source, my_dest)
#     i += 85

