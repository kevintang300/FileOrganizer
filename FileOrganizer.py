import os
import shutil
import getpass

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

        possibleExit = input("Cleaning Completed... Continue? y/n:")

        if possibleExit == 'N' or possibleExit == 'n': 
            break



#These are folders that should not be modified.
def acceptedFolder(strFileName):
    
    if strFileName == "pdf":
        return False
    elif strFileName == "text":
        return False
    elif strFileName == "zips":
        return False
    else:
        return True

def rename_file( filename, newFileName ):

    un = str( getpass.getuser() )
    os.rename(f"/Users/{username}/Downloads/{filename}", f"/Users/{username}/Downloads/{newFileName}" )
    
    

def Clean():

    #Static Directory

    #grabs computer username
    username = str( getpass.getuser() )

    downloadDir = (f'/Users/{username}/Downloads')
    for filename in os.listdir(downloadDir):
        
        strFileName = str(filename)

        if acceptedFolder(strFileName):
            try:
                if image(filename):
                    shutil.move( f'/Users/{username}/Downloads/{filename}' , f'/Users/{username}/Pictures')
                elif pdf(filename):
                    shutil.move( f'/Users/{username}/Downloads/{filename}', f'/Users/{username}/Downloads/pdf')
                elif writings(filename):
                    shutil.move( f'/Users/{username}/Downloads/{filename}', f'/Users/{username}/Downloads/text')
                elif compressed(filename):
                    shutil.move( f'/Users/{username}/Downloads/{filename}', f'/Users/{username}/Downloads/zips')
                else:
                    shutil.move( f'/Users/{username}/Downloads/{filename}', f'/Users/{username}/Downloads/junk')
            except:

                print("A file transfer contains a duplicate name.")
                print("rename(r)")
                print("overwrite(o)")
                print("ignore(i)")

                ROI = input()

                if ROI == "r":
                    #Implement store after renaming
                    newFileName = input("New File Name: ")
                    rename_file(filename, newFileName)


        
        
        
            
           
            


        
    print("Clean")

def Manual():
    print("Manual")



def image(filename):

    if filename.endswith(".jpg") or filename.endswith(".JPG"):
        return True
    elif filename.endswith(".png") or filename.endswith(".PNG"):
        return True
    elif filename.endswith(".jpeg") or filename.endswith(".JPEG"):
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

                         

    
username = str( getpass.getuser() )
downloadDir = (f'/Users/{username}/Downloads')
print(downloadDir)
OptionMenu()
#os.remove('/Users/kevintang/Downloads/output-dp.txt')


#Gets current working directory
#print( os.getcwd() )

#Lists everything in the current directory we're in.
#print( os.listdir() )
