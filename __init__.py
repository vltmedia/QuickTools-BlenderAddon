from .addoninfo import addonInfo
import bpy
from .menus import swapObject, pipelineUpdateScene

bl_info = {
	'name': 'QuickTools',
	'description': 'Various tools for everyday production use',
	'author': 'VLT Media LLC',
	'license': 'GPL',
	'deps': '',
	'version': (0, 4, 0, 0),
	'blender': (3, 0, 0),
	'location': 'View3D > Quick Tools',
	'warning': '',
	'wiki_url': 'https://github.com/vltmedia/QuickTools-BlenderAddon',
	'tracker_url': 'https://github.com/vltmedia/QuickTools-BlenderAddon/issues',
	'link': '',
	'support': 'COMMUNITY',
	'category': '3D View'
	}

def menu_func(self, context):
    self.layout.menu(swapObject.OBJECT_MT_swapmenu.bl_idname)
    self.layout.menu(pipelineUpdateScene.OBJECT_MT_pipelineupdate.bl_idname)

class VIEW3D_MT_menu_swapreplace(bpy.types.Menu):
    bl_label = "Quick Tools"
    # Set the menu operators and draw functions
    def draw(self, context):
        layout = self.layout
        layout.operator("bgis.pref_show", icon='PREFERENCES')
        
       
def add_gis_menu(self, context):
    if context.mode == 'OBJECT':
        self.layout.menu('VIEW3D_MT_menu_swapreplace')

def register():
    pipelineUpdateScene.register()
    swapObject.register()
    
    try:
        bpy.utils.register_class(VIEW3D_MT_menu_swapreplace)
    except ValueError as e:
        bpy.utils.unregister_class(VIEW3D_MT_menu_swapreplace)
        bpy.utils.register_class(VIEW3D_MT_menu_swapreplace)
    bpy.types.VIEW3D_MT_editor_menus.append(add_gis_menu)
    bpy.types.VIEW3D_MT_menu_swapreplace.append(menu_func)

def unregister():
    # bpy.utils.unregister_class(OBJECT_OT_myooperator)
    
    bpy.types.VIEW3D_MT_add.remove(menu_func)

if __name__ == "__main__":
    register()
    