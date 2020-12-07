import json

class addonInfo():
    bl_info = {
	'name': 'QuickTools',
	'description': 'Various tools for everyday production use',
	'author': 'VLT Media LLC',
	'license': 'GPL',
	'deps': '',
	'version': (0, 1, 10),
	'blender': (2, 90, 1),
	'location': 'View3D > Quick Tools',
	'warning': '',
	'wiki_url': 'https://github.com/vltmedia/QuickTools-BlenderAddon',
	'tracker_url': 'https://github.com/vltmedia/QuickTools-BlenderAddon/issues',
	'link': '',
	'support': 'COMMUNITY',
	'category': '3D View'
	}

def getInfo():
    return addonInfo.bl_info

def getVersionString(): 
    
    strr =  '.'.join(str(addonInfo.bl_info.get("version")).replace(".", "").replace(",", "")) 
    finall = strr.replace(". ", "").replace("(", "").replace(")", "")[1:-1]
    return finall
def getNextVersionString(): 
    vers = addonInfo.bl_info.get("version")
    verslist = list(vers)
    
    lastindex = len(vers) - 1
    nextversion = verslist[lastindex] + 1
    verslist[lastindex] = nextversion
    x = tuple(verslist)
    strr =  '.'.join(str(x).replace(".", "").replace(",", "")) 
    finall = strr.replace(". ", "").replace("(", "").replace(")", "")[1:-1]
    return finall
  