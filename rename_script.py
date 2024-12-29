import os
import re

ime_prez = r'[A-Z][a-z]+\s[A-Z][a-z]+\s(-)\s'

#treba odraditi regex ili nekakvo prepoznavanje odakle krece ime izvodjaca
#ili sta god treba da se edituje, da se ne zezam samo sa stringovima svaki put

source_folder = r'C:\Users\obren\OneDrive\Desktop\code\projekti\yt_converter\yt_converter'

for item in os.listdir(source_folder):
    #check if an item is a file or not
    if os.path.isfile(os.path.join(source_folder, item)):
        if(item.endswith('.mp3')):
            #if a file is open, we cant rename it
            try:
                #za sada mora rucno izracunavanje
                new_name = item[:-22] #sklanjamo sa kraja dodatke
                artist = re.match(ime_prez, new_name)
                artist_len = len(artist.group(0))
                new_name = new_name[artist_len:]+" - "+(artist.group(0))[:-3]
                os.rename(
                    os.path.join(source_folder, item),
                    os.path.join(source_folder,new_name+'.mp3')
                )
            except PermissionError:
                continue
            except Exception as e:
                raise Exception(e)