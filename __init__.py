import bpy
bl_info = {
	'name': 'QuickTools',
	'description': 'Various tools for everyday production use',
	'author': 'VLT Media LLC',
	'license': 'GPL',
	'deps': '',
	'version': (1, 0),
	'blender': (2, 90, 1),
	'location': 'View3D > Quick Tools',
	'warning': '',
	'wiki_url': 'https://github.com/domlysz/BlenderGIS/wiki',
	'tracker_url': 'https://github.com/domlysz/BlenderGIS/issues',
	'link': '',
	'support': 'COMMUNITY',
	'category': '3D View'
	}
class OBJECT_OT_myoperator(bpy.types.Operator):
    bl_idname = 'object.myoperator'
    bl_label = 'rtMyOperator'
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        # ...affairs...
        return {'FINISHED'}

class OBJECT_MT_mymenu(bpy.types.Menu):
    bl_idname = 'object.mymenu'
    bl_label = 'rtMyMenu'

    def draw(self, context):
        layout = self.layout
        layout.operator(OBJECT_OT_myoperator.bl_idname)

def menu_func(self, context):
    self.layout.menu(OBJECT_MT_mymenu.bl_idname)

class VIEW3D_MT_menu_treats(bpy.types.Menu):
    bl_label = "Quick Tools"
    # Set the menu operators and draw functions
    def draw(self, context):
        layout = self.layout
        layout.operator("bgis.pref_show", icon='PREFERENCES')
        
       
def add_gis_menu(self, context):
    if context.mode == 'OBJECT':
        self.layout.menu('VIEW3D_MT_menu_treats')

def register():
    bpy.utils.register_class(OBJECT_OT_myoperator)
    bpy.utils.register_class(OBJECT_MT_mymenu)
    try:
        bpy.utils.register_class(VIEW3D_MT_menu_treats)
    except ValueError as e:
        logger.warning('{} is already registered, now unregister and retry... '.format(menu))
        bpy.utils.unregister_class(VIEW3D_MT_menu_treats)
        bpy.utils.register_class(VIEW3D_MT_menu_treats)
    bpy.types.VIEW3D_MT_editor_menus.append(add_gis_menu)
    bpy.types.VIEW3D_MT_menu_treats.append(menu_func)

def unregister():
    bpy.utils.unregister_class(OBJECT_OT_myooperator)
    bpy.utils.unregister_class(OBJECT_MT_mymenu)
    
    bpy.types.VIEW3D_MT_add.remove(menu_func)

if __name__ == "__main__":
    register()