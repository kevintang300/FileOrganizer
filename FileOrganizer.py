import os
import shutil

def OptionMenu():

    

    while(True):

        
        print()
        print("-------------------------Folder Organizer 2021-------------------------")

        print("Command List")
        print("------------")
        print("Clean: Cleans and organizes download folder")
        print("Manual: Iterate through folder for manual deletion")
        print("Quit: Exit Organizer")
        
        command = input("\nEnter Command: ")

        if command == "Clean" or command == "clean":
            Clean()

        elif command == "Manual" or command == "manual":
            Manual()

        elif command == "Quit" or command == "quit":
            break

        else:
            print("Invalid Command")

    
    

def Clean():

    downloadDir = ('/Users/kevintang/Downloads')
    for filename in os.listdir(downloadDir):

        try:
            if image(filename):
                shutil.move( f'/Users/kevintang/Downloads/{filename}' , '/Users/kevintang/Pictures')
            elif pdf(filename):
                shutil.move( f'/Users/kevintang/Downloads/{filename}', '/Users/kevintang/Downloads/pdf')
            elif writings(filename):
                shutil.move( f'/Users/kevintang/Downloads/{filename}', '/Users/kevintang/Downloads/text')
            elif compressed(filename):
                shutil.move( f'/Users/kevintang/Downloads/{filename}', '/Users/kevintang/Downloads/zips')
            else:
                shutil.move( f'/Users/kevintang/Downloads/{filename}', '/Users/kevintang/Downloads/junk')
        except:
            print("File you want to transfer already exists")
        
        
        
            
           
            


        
    print("Clean")

def Manual():
    print("Manual")



def image(filename):

    if filename.endswith(".jpg") or filename.endswith(".JPG"):
        return True
    elif filename.endswith(".png") or filename.endswith(".PNG"):
        return True
    else:
        return False


def pdf(filename):
    
    if filename.endswith(".pdf") or filename.endswith(".PDF"):
        return True
    else:
        return False

def writings(filename):
    
    if filename.endswith(".txt") or filename.endswith(".docx") or filename.endswith(".doc"):
        return True
    else:
        return False

def compressed(filename):

    if filename.endswith(".zip"):
        return True
    else:
        return False

                         

    
    
print("Testing git push")
OptionMenu()
#os.remove('/Users/kevintang/Downloads/output-dp.txt')


#Gets current working directory
#print( os.getcwd() )

#Lists everything in the current directory we're in.
#print( os.listdir() )
