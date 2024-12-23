import os

#treba odraditi regex ili nekakvo prepoznavanje odakle krece ime izvodjaca
#ili sta god treba da se edituje, da se ne zezam samo sa stringovima

source_folder = r'C:\Users\obren\OneDrive\Desktop\dalibor\dalibor'

for item in os.listdir(source_folder):
    #check if an item is a file or not
    if os.path.isfile(os.path.join(source_folder, item)):
        if(item.endswith('.mp3')):
            #if a file is open, we cant rename it
            try:
                os.rename(
                    os.path.join(source_folder, item),
                    os.path.join(source_folder,item[14:-43]+' - '+item[:11]+'.mp3')
                )
            except PermissionError:
                continue
            except Exception as e:
                raise Exception(e)