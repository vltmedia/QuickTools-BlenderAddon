import os
import zipfile
import json
from datetime import date

from addoninfo import getInfo, addonInfo, getVersionString, getNextVersionString
today = date.today()
currentdir = os.path.dirname(os.path.realpath(__file__)) 
parentdir = os.path.dirname(currentdir) 
addonInfoJson = getInfo() 

addonname = addonInfoJson.get("name")
version = getVersionString()
datee = today.strftime("%d%m%Y")
def zip_dir(directory, zipname):
    """
    Compress a directory (ZIP file).
    """
    if os.path.exists(directory):
        outZipFile = zipfile.ZipFile(zipname, 'w', zipfile.ZIP_DEFLATED)

        # The root directory within the ZIP file.
        rootdir = os.path.basename(directory)

        for dirpath, dirnames, filenames in os.walk(directory):
            for filename in filenames:

                # Write the file named filename to the archive,
                # giving it the archive name 'arcname'.
                filepath   = os.path.join(dirpath, filename)
                parentpath = os.path.relpath(filepath, directory)
                arcname    = os.path.join(rootdir, parentpath)

                outZipFile.write(filepath, arcname)

    outZipFile.close()

def convertTuple(tup): 
    
    strr =  '.'.join(str(tup).replace(".", "").replace(",", "")) 
    finall = strr.replace(". ", "").replace("(", "").replace(")", "")[1:-1]
    return finall

def updateAddonInfoFile(version):
    # Update the Addon info
    file1 = open("addoninfo.py","r+")
    liness = file1.read()
    file1.close()
    currentversion = getVersionString()
    nextversion = getnextVersionsolo(version)
    tuplestring = "("+nextversion.split('.')[0]+", " +nextversion.split('.')[1]+", " +nextversion.split('.')[2]+")"   
    tuplestringoriginal = "("+currentversion.split('.')[0]+", " +currentversion.split('.')[1]+", " +currentversion.split('.')[2]+")"   
    print(tuplestring)
    print(tuplestringoriginal)
    linessfixed = liness.replace(tuplestringoriginal,tuplestring)
    file1 = open("addoninfo.py","w")
    file1.write(linessfixed)
    file1.close()
    # Update the Addon for Blender now
    file2 = open("__init__.py","r+")
    liness2 = file2.read()
    file2.close()
    liness2fixed = liness2.replace(tuplestringoriginal,tuplestring)
    file2 = open("__init__.py","w")
    file2.write(liness2fixed)
    file2.close()
 

def getnextVersion(currentverion):
    lastindex = len(currentverion.split(".")) - 1 
    lastsplit = currentverion.split(".")[lastindex]
    nextnum = int(lastsplit) + 1
    print(nextnum)
    outversion = currentverion[:-1] + str(nextnum)
    print(outversion)
    
    initialpath = [parentdir + "\\"+addonname +"_"+ outversion +"_"+ datee+"_.zip",outversion]
    initialexists = os.path.exists(initialpath[0])
    
    if(initialexists):
        initialpath = getnextVersion(outversion)
    
    return initialpath

def getnextVersionsolo(currentverion):
    lastindex = len(currentverion.split(".")) - 1 
    lastsplit = currentverion.split(".")[lastindex]
    nextnum = int(lastsplit) + 1
    print(nextnum)
    outversion = currentverion[:-1] + str(nextnum)
    print(outversion)
    
    return outversion

if __name__ == '__main__':
    
    print(os.path.dirname(os.path.realpath(__file__)))

    
    outpath = parentdir + "\\"+addonname +"_"+ version +"_"+ datee+"_.zip"
    initialexists = os.path.exists(outpath)
    
    if(initialexists):
        outtuple = getnextVersion(version)
        outpath = outtuple[0]
        version = outtuple[1]
        print(outpath)
        print(version)
    updateAddonInfoFile(version)

    zip_dir(currentdir, outpath)
    
    print("````````````````````````````````````````````````````````````````")
    print("Finished Creating the Zip File!")
    print(outpath)
    print(version)
    print("````````````````````````````````````````````````````````````````")
    