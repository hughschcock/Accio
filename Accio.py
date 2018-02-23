#!/usr/bin/env python

def image_index(directory):
    '''function that uses os.walk(directory) - to output an index of all images
    in directory and subdirectories of extensions: ("jpg", "JPG", "jpeg", "JPEG", "png", "PNG")'''


    from os import walk
    from shutil import get_terminal_size as tsize
    l = list(walk(directory))
    width = tsize()[0]
    imgcount = 0
    counter = 0
    filenum = 0
    
    while counter < len(l):
        for i in range(len(l[counter][2])):
            filenum += 1    
        if len(l[counter][2]) >= 1:
            imagelist = [i for i in l[counter][2] if i.endswith(("jpg","JPG","jpeg","JPEG","png","PNG"))]
            if len(imagelist) > 0:
                print('\n')
                print("FOLDER:".center(width))
                print(str(l[counter][0]).center(width))
                print("#",counter)
                hr = print("-"*width)
                hr
                print("FILES: {}".format(len(l[counter][2])).center(width))
                print("IMAGES: {}".format(len(imagelist)).center(width))
                for x in imagelist:
                    print("[!]\t{}".format(x))
                    imgcount +=1
                counter+=1
            else:
                pass
        
        counter +=1

    else:
        print("\n{} subdirectories,\n{} files scanned\n{} images".format(len(l), filenum, imgcount))


   
def move_contents(origin, destination):
    '''function that moves all images in [origin] into [destination]'''
    from os import chdir, listdir, getcwd, system, curdir
    import sys

    
    select = []
    imagecount = 0
    files = listdir(origin)
    before= listdir(destination)
    cd = lambda u: chdir(u)

    #try changing directory to where images are, print actual cwd on fail
    try:
        cd(origin)
        print("Changing directory to {}...".format(origin))
    except:
        print("That didn't work...")
        print("Current Working Directory: {}".format(getcwd()))
        sys.exit()
    #print how many files there are, and how many are images
    itemsin = len(listdir(curdir))
    print("{} files in {}".format(itemsin, getcwd()))
    #select images 
    for f in listdir(curdir):
        if f.endswith(("jpg","JPG","jpeg","JPEG","png","PNG","gif","GIF","bmp","BMP")):
            imagecount += 1
            select.append(f)
    print("{} of which are images...".format(imagecount))
    #move them into destination
    try:
        for i in select:
            print("Moving image {}".format(i))
            if sudo in yes:
                system("sudo mv '{}' {}".format(i, destination))
            else:
                system("mv {} {}".format(i, destination))
    except:
        print("file relocation failed!")
        raise
    
    else:
        #check if the transfer actually happened
        after = listdir(destination)
        tot= (len(after) - len(before))
        print("{} new items in {}".format(tot, destination))
        if tot > 0:
            print("Success")
        else:
            print("That didn't work...\nCheck ownership")




def FengSushi(funk):
    def Burrito():
        from shutil import get_terminal_size as ts
        width = ts()[0]
        print("<>"*(round(width/2)))
        funk()
        print("<>"*(round(width/2)))
    return Burrito


@FengSushi
def maine():
    from shutil import get_terminal_size as tsize
    from os import listdir, getcwd
    import sys

    global sudo
    global yes
    
    print("Accio\n".center(tsize()[0]))
    print('Program that finds images (jpg, jpeg, png, gif, bmp) in a given directory \nand subdirectories, and optionally transfers them into another one.\n')
    print("Enter path/to/parent/directory to be scanned: \n")
    loc = str(input(">>> ").strip(" "))
   
    wd = lambda: getcwd()
    try:
        tl = listdir(loc)
        assert len(tl)>=1
        image_index(loc)
    except FileNotFoundError:
        print("Not found")
    except AssertionError:
        print("Empty")

    yes =['y','Y','yes','YES']
    
    while 1:
        try:
            print("Directory to be extracted: ")
            origin = loc +"/"+ str(input(">>> {}/".format(loc)).strip(" "))
            print("Destination: ")
            destination = str(input(">>> ").strip(" "))
            print("Run as superuser? (Better chance of success):")
            sudo = input(">>> ")
            move_contents(origin,destination)
        except KeyboardInterrupt:
            print("Good Bye!")
            sys.exit()
               


      

maine()
