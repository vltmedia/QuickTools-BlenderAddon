import bpy
from bpy.props import IntProperty, PointerProperty, BoolProperty, CollectionProperty,FloatProperty

from bpy.types import Panel, PropertyGroup, WindowManager

SourcePostEnum = [
    ("HIDE", "Hide", "", 1),
    ("DELETE", "Delete", "", 2),
    ("NOTHING", "Nothing", "", 3),
    
]
TargetCollectionPostEnum = [
    ("COPY", "Copy", "", 1),
    ("BASE", "Default", "", 2),
    
]
# This is the tab area
class swapObjectVars(PropertyGroup):
    NamePattern: bpy.props.StringProperty(name="Source Name Pattern", default="Cube.*")
    TemplateObject: bpy.props.StringProperty(name="Template Object Name", default="Template")
    NewMeshName: bpy.props.StringProperty(name="New Mesh Name Template", default="NewObjectName_")
    
    SourcePost: bpy.props.EnumProperty(items=SourcePostEnum, name="Source Handling")
    TargetCollectionPost: bpy.props.EnumProperty(items=TargetCollectionPostEnum, name="Target Collection")



# class SwapNameSettings(bpy.types.PropertyGroup):
#     NamePattern: bpy.props.StringProperty()
#     TemplateObjectName: bpy.props.StringProperty()
#     PostScale: bpy.props.FloatProperty()

# bpy.utils.register_class(SwapNameSettings)
class OBJECT_OT_swapobjectsingle(bpy.types.Operator):
    bl_idname = 'object.swapobjectsingle'
    bl_label = 'Swap Objects By Name'
    bl_options = {'REGISTER', 'UNDO'}
    NamePattern: bpy.props.StringProperty(name="Source Name Pattern", default="Cube.*")
    TemplateObject: bpy.props.StringProperty(name="Template Object Name", default="Template")
    NewMeshName: bpy.props.StringProperty(name="New Mesh Name Template", default="NewObjectName_")
    SourcePost: bpy.props.EnumProperty(items=SourcePostEnum, name="Source Handling")
    TargetCollectionPost: bpy.props.EnumProperty(items=TargetCollectionPostEnum, name="Target Collection")
    


    def execute(self, context):
        bpy.ops.object.select_pattern(pattern= self.NamePattern)
        selects = context.selected_objects
        currentcount = 0
        transformss = []
        try:
            # bpy.data.objects[self.TemplateObject].select_set(True)
            objjj = bpy.data.objects[self.TemplateObject]
            print(objjj)
            
            for obj in selects:
            
                bpy.data.objects[self.TemplateObject].select_set(True)
                templatee = bpy.context.selected_objects[0]
            
                if obj != templatee:
                
                    transformss.append([obj.location, obj.rotation_quaternion, obj.scale])
                    collectionss = obj.users_collection
                    
                    # ob = bpy.data.objects.get(self.TemplateObject)
                    
                    ob_dup = templatee.copy()
                    
                    
                    if self.TargetCollectionPost == "COPY":
                        for collection in collectionss:
                            collection.objects.link(ob_dup)
                    if self.TargetCollectionPost == "BASE":
                        bpy.data.collections['Collection'].objects.link(ob_dup)
                    ob_dup.name = self.NewMeshName + str(currentcount)
                
                    # Create the new object by linking to the template's mesh data
                    new_object = ob_dup
                    new_object.location = obj.location
                    new_object.rotation_quaternion = obj.rotation_quaternion
                    new_object.scale = obj.scale


                    if self.SourcePost == "HIDE":
                        obj.hide_viewport = True
                        obj.hide_render = True
                    if self.SourcePost == "DELETE":
                        bpy.ops.object.select_all(action='DESELECT')
                        # select the object
                        obj.select_set(True)
                        # delete all selected objects
                        bpy.ops.object.delete()
                        
                    # Create a new animation for the newly created object
                    nextcount = currentcount + 1
                    currentcount = nextcount
            ShowMessageBox("Finished Swaping objects!", "Quick Tools : Swap Complete!", 'HEART')
        except :
            #Shows a message box with a message, custom title, and a specific icon
            ShowMessageBox("Please Set the Template Object Name Correctly Then Hit Enter.", "Template Object Not Found", 'ERROR')
            
        return {'FINISHED'}


def ShowMessageBox(message = "", title = "Message Box", icon = 'INFO'):

    def draw(self, context):
        self.layout.label(text=message)

    bpy.context.window_manager.popup_menu(draw, title = title, icon = icon)


# bpy.utils.register_class(SwapNameSettings)
class OBJECT_OT_swapobjectselections(bpy.types.Operator):
    bl_idname = 'object.swapobjectselections'
    bl_label = 'Swap Selected Objects'
    bl_options = {'REGISTER', 'UNDO'}
    TemplateObject: bpy.props.StringProperty(name="Template Object Name", default="Template")
    NewMeshName: bpy.props.StringProperty(name="New Mesh Name Template", default="NewObjectName_")
    SourcePost: bpy.props.EnumProperty(items=SourcePostEnum, name="Source Handling")
    TargetCollectionPost: bpy.props.EnumProperty(items=TargetCollectionPostEnum, name="Target Collection")
    


    def execute(self, context):
        selects = bpy.context.selected_objects
        currentcount = 0
        transformss = []
        lastindex = len(selects) - 1
        try:
            objjj = bpy.data.objects[self.TemplateObject]
            print(objjj)
            for obj in selects:
                bpy.data.objects[self.TemplateObject].select_set(True)
                templatee = bpy.context.selected_objects[0]
                if obj != templatee:
                    transformss.append([obj.location, obj.rotation_quaternion, obj.scale])
                    collectionss = obj.users_collection
        
                    
                    # ob = bpy.data.objects.get(self.TemplateObject)
                    
                    ob_dup = templatee.copy()
                    
                    
                    if self.TargetCollectionPost == "COPY":
                        for collection in collectionss:
                            collection.objects.link(ob_dup)
                    if self.TargetCollectionPost == "BASE":
                        bpy.data.collections['Collection'].objects.link(ob_dup)
                    ob_dup.name = self.NewMeshName + str(currentcount)
                
                    # Create the new object by linking to the template's mesh data
                    new_object = ob_dup
                    new_object.location = obj.location
                    new_object.rotation_quaternion = obj.rotation_quaternion
                    new_object.scale = obj.scale

                    if self.SourcePost == "HIDE":
                        obj.hide_viewport = True
                        obj.hide_render = True
                    if self.SourcePost == "DELETE":
                        bpy.ops.object.select_all(action='DESELECT')
                        # select the object
                        obj.select_set(True)
                        # delete all selected objects
                        bpy.ops.object.delete()
                        
                    # Create a new animation for the newly created object
                    nextcount = currentcount + 1
                    currentcount = nextcount
            ShowMessageBox("Finished Swaping objects!", "Quick Tools : Swap Complete!", 'HEART')
        
        except :
            #Shows a message box with a message, custom title, and a specific icon
            ShowMessageBox("Please set the Template Object Name correctly then hit enter.", "Template Object Not Found", 'ERROR')
            
        return {'FINISHED'}




class OBJECT_MT_swapmenu(bpy.types.Menu):
    bl_idname = 'object.swapmenu'
    bl_label = 'Swap Objects'

    def draw(self, context):
        layout = self.layout
        layout.operator(OBJECT_OT_swapobjectsingle.bl_idname)
        layout.operator(OBJECT_OT_swapobjectselections.bl_idname)
classes = [
	OBJECT_OT_swapobjectsingle,
	OBJECT_OT_swapobjectselections,
	OBJECT_MT_swapmenu
]


class swapObject_PT_panel(Panel):
    bl_idname = 'swapObject_PT_panel'
    bl_label = 'Quick Tools'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'QuickTools'

    def draw(self, context):
        operator = self.layout.operator('object.swapobjectsingle', icon='SMALL_CAPS', text='Swap Objects By Name')
        operatorb = self.layout.operator('object.swapobjectselections', icon='SYSTEM', text='Swap Selected Objects')
        operator.NamePattern = context.window_manager.swapObject_vars.NamePattern
        operator.TemplateObject = context.window_manager.swapObject_vars.TemplateObject
        operator.NewMeshName = context.window_manager.swapObject_vars.NewMeshName
        operator.SourcePost = context.window_manager.swapObject_vars.SourcePost
        operator.TargetCollectionPost = context.window_manager.swapObject_vars.TargetCollectionPost
        
        operatorb.TemplateObject = context.window_manager.swapObject_vars.TemplateObject
        operatorb.NewMeshName = context.window_manager.swapObject_vars.NewMeshName
        operatorb.SourcePost = context.window_manager.swapObject_vars.SourcePost
        operatorb.TargetCollectionPost = context.window_manager.swapObject_vars.TargetCollectionPost
        
        self.layout.prop(context.window_manager.swapObject_vars, 'NamePattern')
        self.layout.prop(context.window_manager.swapObject_vars, 'TemplateObject')
        self.layout.prop(context.window_manager.swapObject_vars, 'NewMeshName')
        self.layout.prop(context.window_manager.swapObject_vars, 'SourcePost')
        self.layout.prop(context.window_manager.swapObject_vars, 'TargetCollectionPost')



def register():
    bpy.utils.register_class(swapObjectVars)
    bpy.utils.register_class(swapObject_PT_panel)
    WindowManager.swapObject_vars = PointerProperty(type=swapObjectVars)

    for cls in classes:
        try:
            bpy.utils.register_class(cls)
        except ValueError as e:
            bpy.utils.unregister_class(cls)
            bpy.utils.register_class(cls)

def unregister():
	for cls in classes:
		bpy.utils.unregister_class(cls)


