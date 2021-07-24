import bpy
from bpy.props import IntProperty, PointerProperty, BoolProperty, CollectionProperty,FloatProperty

from bpy.types import Panel, PropertyGroup, WindowManager
import os




 

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
class pipelineUpdateSceneVars(PropertyGroup):
    # path = bpy.data.filepath
    # path = bpy.data.filepath
    
    # dirname = os.path.dirname(path) 
    # basename = os.path.basename(path)
    # basenameBlend = basename.split(".blend")[0]
    # namesplit = basenameBlend.split("_")
    # basenamenoversion = ""
    # Version = "01"
    # outfoldereevee = dirname + "\\out\\" + Version + "\\eevee\\"
    # outfoldereeveeFilepath = dirname + "\\out\\" + Version + "\\eevee\\" + basenamenoversion + "_eevee_"
    # outfolderpb = dirname + "\\out\\" + Version + "\\pb\\"
    # outfolderpbFilepath = dirname + "\\out\\" + Version + "\\pb\\" + basenamenoversion + "_pb_"
    # basenamenoversion = namesplit[0]+"_"+ namesplit[1]+"_"+ namesplit[2]

    # ShotID: bpy.props.StringProperty(name="Shot ID", default=basenamenoversion)
    Versionn: bpy.props.StringProperty(name="Version", default="01")
    # dirname: bpy.props.StringProperty(name="Base Export Directory", default=dirname)
    # outfoldereeveeFilepath: bpy.props.StringProperty(name="Eevee Export Path", default=outfoldereeveeFilepath)
    # outfolderpbFilepath: bpy.props.StringProperty(name="Workbench Export Path", default=outfolderpbFilepath)
    
    
    # ShotID: bpy.props.StringProperty(name="Shot ID", default=basenamenoversion)
    # Versionn: bpy.props.StringProperty(name="Version", default="01")
    # dirname: bpy.props.StringProperty(name="BAse Export Directory", default=dirname)
    # outfoldereeveeFilepath: bpy.props.StringProperty(name="Eevee Export Path", default=outfoldereeveeFilepath)
    # outfolderpbFilepath: bpy.props.StringProperty(name="Workbench Export Path", default=outfolderpbFilepath)
    
    # NamePattern: bpy.props.StringProperty(name="Source Name Pattern", default="Cube.*")
    # TemplateObject: bpy.props.StringProperty(name="Template Object Name", default="Template")
    # NewMeshName: bpy.props.StringProperty(name="New Mesh Name Template", default="NewObjectName_")
    
    # SourcePost: bpy.props.EnumProperty(items=SourcePostEnum, name="Source Handling")
    # TargetCollectionPost: bpy.props.EnumProperty(items=TargetCollectionPostEnum, name="Target Collection")



# class SwapNameSettings(bpy.types.PropertyGroup):
#     NamePattern: bpy.props.StringProperty()
#     TemplateObjectName: bpy.props.StringProperty()
#     PostScale: bpy.props.FloatProperty()

# bpy.utils.register_class(SwapNameSettings)
class OBJECT_OT_pipelineupdatescenesingle(bpy.types.Operator):
    
    bl_idname = 'object.pipelineupdatescenesingle'
    bl_label = 'Update Post Scene Files'
    bl_options = {'REGISTER', 'UNDO'}
    # path = bpy.data.filepath
    
    # dirname = os.path.dirname(path) 
    # basename = os.path.basename(path)
    # basenameBlend = basename.split(".blend")[0]
    # namesplit = basenameBlend.split("_")
    # basenamenoversion = ""
    # Version = "01"
    # outfoldereevee = dirname + "\\out\\" + Version + "\\eevee\\"
    # outfoldereeveeFilepath = dirname + "\\out\\" + Version + "\\eevee\\" + basenamenoversion + "_eevee_"
    # outfolderpb = dirname + "\\out\\" + Version + "\\pb\\"
    # outfolderpbFilepath = dirname + "\\out\\" + Version + "\\pb\\" + basenamenoversion + "_pb_"
    # basenamenoversion = namesplit[0]+"_"+ namesplit[1]+"_"+ namesplit[2]

    # ShotID: bpy.props.StringProperty(name="Shot ID", default=basenamenoversion)
    # dirname: bpy.props.StringProperty(name="Base Export Directory", default=dirname)
    # outfoldereeveeFilepath: bpy.props.StringProperty(name="Eevee Export Path", default=outfoldereeveeFilepath)
    # outfolderpbFilepath: bpy.props.StringProperty(name="Workbench Export Path", default=outfolderpbFilepath)
    

    # NamePattern: bpy.props.StringProperty(name="Source Name Pattern", default="Cube.*")
    # TemplateObject: bpy.props.StringProperty(name="Template Object Name", default="Template")
    # NewMeshName: bpy.props.StringProperty(name="New Mesh Name Template", default="NewObjectName_")
    # SourcePost: bpy.props.EnumProperty(items=SourcePostEnum, name="Source Handling")
    # TargetCollectionPost: bpy.props.EnumProperty(items=TargetCollectionPostEnum, name="Target Collection")
    


    def execute(self, context):
        
        path = bpy.data.filepath
        dirname = os.path.dirname(path) 
        bigpath =os.path.abspath(os.path.join(dirname, os.pardir))
        dirname = bigpath
        basename = os.path.basename(path)
        basenameBlend = basename.split(".blend")[0]
        namesplit = basenameBlend.split("_")
        basenamenoversion = ""
        Version = "01"
        good = False
        try:
            for i in range(0, 2):
                newname = basenamenoversion +"_"+ namesplit[i]
                
                if i == 0:
                    newname = basenamenoversion + namesplit[i]
                    
                basenamenoversion = newname
            
            Version = namesplit[2]
            good = True
        except:
            ShowMessageBox("Blend filenaming convention is incorrect SCENE_SHOT_VERSION", "Quick Tools : Post Files BAD NAME!", 'ERROR')
            
        if good == True:
            scenefolder = dirname + "\\out\\" + Version + "\\" + basenamenoversion+ "\\" 
            eeveeblend = scenefolder + basenamenoversion + "_eevee.blend"
            pbblend = scenefolder + basenamenoversion + "_pb.blend"

            # eeveeblend = dirname + "\\" + basenamenoversion + "_eevee.blend"
            # pbblend = dirname + "\\" + basenamenoversion + "_pb.blend"

            outbatpb = dirname + "\\out\\" + Version + "\\batchexportpb.bat"
            outbateevee = dirname + "\\out\\" + Version + "\\batchexporteevee.bat"
            outfoldereevee = scenefolder + "eevee\\"
            outfoldereeveeFilepath = scenefolder + "eevee\\" + basenamenoversion + "_eevee_"
            outfolderpb = scenefolder  + "\\pb\\"
            outfolderpbFilepath = scenefolder+ "pb\\" + basenamenoversion + "_pb_"

            print("`````````````````dirname````````````````````````")
            print(eeveeblend)

            print("`````````````````````````````````````````")
            print("````````````````outfoldereevee`````````````````````````")
            print(outfoldereevee)

            print("`````````````````````````````````````````")


            print("`````````````````dirname````````````````````````")
            print(pbblend)

            print("`````````````````````````````````````````")
            print("````````````````outfoldereevee`````````````````````````")
            print(outfolderpb)

            print("`````````````````````````````````````````")

            # Make Folders
            if os.path.exists(outfoldereevee) == False:
                os.makedirs(outfoldereevee)
            if os.path.exists(outfolderpb) == False:
                os.makedirs(outfolderpb)
                
            # Save Eevee Files
            bpy.context.scene.render.engine = 'BLENDER_EEVEE'

            bpy.context.scene.render.filepath = outfoldereeveeFilepath
            
            bpy.ops.wm.save_as_mainfile(filepath=eeveeblend)
            print("Saved Eevee Blend File: " + outfoldereeveeFilepath)
        
            # Save PB Files
            
            bpy.context.scene.render.engine = 'BLENDER_WORKBENCH'
            bpy.data.scenes['Scene'].display.shading.color_type = 'TEXTURE'
            bpy.data.scenes['Scene'].display.shading.show_cavity = True
            bpy.data.scenes['Scene'].display.shading.light = 'MATCAP'
            bpy.data.scenes['Scene'].display.shading.studio_light = 'basic_side.exr'


            bpy.context.scene.render.filepath = outfolderpbFilepath
            
            bpy.ops.wm.save_as_mainfile(filepath=pbblend)
            print("Saved WorkBench Blend File: " + outfolderpbFilepath)
            
            
            #Update Bat Files
            
                    # Append-adds at last 
            # append mode 
            file1 = open(outbatpb, "a")   

            # writing newline character 
            file1.write("\n") 
            # Write Blender Line
            file1.write('blender -b "'+pbblend+'" -a ') 

            file1.write("\n") 
            #Write FFMPEG
            file1.write('ffmpeg -start_number 1000 -r 24 -f image2 -s 1920x1080 -i "'+outfolderpbFilepath+'%%04d.png" -vcodec libx264 -crf 25  -pix_fmt yuv420p "'+outfolderpbFilepath+'.mp4"') 
            file1.close()
            
            file1 = open(outbateevee, "a")   

            # writing newline character 
            file1.write("\n") 
            # Write Blender Line
            file1.write('blender -b "'+eeveeblend+'" -a ') 

            file1.write("\n") 
            #Write FFMPEG
            file1.write('ffmpeg -start_number 1000 -r 24 -f image2 -s 1920x1080 -i "'+outfoldereeveeFilepath+'%%04d.png" -vcodec libx264 -crf 25  -pix_fmt yuv420p "'+outfoldereeveeFilepath+'.mp4"') 
            
            file1.close()
        
        
        
            ShowMessageBox("Finished Saving Post Files!", "Quick Tools : Post Files Exported!", 'HEART')

        return {'FINISHED'}


def ShowMessageBox(message = "", title = "Message Box", icon = 'INFO'):

    def draw(self, context):
        self.layout.label(text=message)

    bpy.context.window_manager.popup_menu(draw, title = title, icon = icon)


# bpy.utils.register_class(SwapNameSettings)
class OBJECT_OT_pipelineUpdateSceneselections(bpy.types.Operator):
    bl_idname = 'object.pipelineUpdateSceneselections'
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




class OBJECT_MT_pipelineupdate(bpy.types.Menu):
    bl_idname = 'object.pipelineupdate'
    bl_label = 'Pipeline | Update Post Scenes'

    def draw(self, context):
        layout = self.layout
        layout.operator(OBJECT_OT_pipelineupdatescenesingle.bl_idname)
        # layout.operator(OBJECT_OT_pipelineUpdateSceneselections.bl_idname)
classes = [
	OBJECT_OT_pipelineupdatescenesingle,
	# OBJECT_OT_pipelineUpdateSceneselections,
	OBJECT_MT_pipelineupdate
]


class pipelineUpdateScene_PT_panel(Panel):
    bl_idname = 'pipelineUpdateScene_PT_panel'
    bl_label = 'Q3'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'QuickTools'

    def draw(self, context):
        path = bpy.data.filepath
            
        # dirname = os.path.dirname(path) 
        # basename = os.path.basename(path)
        # basenameBlend = basename.split(".blend")[0]
        # namesplit = basenameBlend.split("_")
        # basenamenoversion = ""
        # Version = "01"
        # outfoldereevee = dirname + "\\out\\" + Version + "\\eevee\\"
        # outfoldereeveeFilepath = dirname + "\\out\\" + Version + "\\eevee\\" + basenamenoversion + "_eevee_"
        # outfolderpb = dirname + "\\out\\" + Version + "\\pb\\"
        # outfolderpbFilepath = dirname + "\\out\\" + Version + "\\pb\\" + basenamenoversion + "_pb_"
        # basenamenoversion = namesplit[0]+"_"+ namesplit[1]+"_"+ namesplit[2]

    
        # operator = self.layout.operator('object.pipelineUpdateScenesingle', icon='SMALL_CAPS', text='Pipeline | Update Post Scenes')
        # operatorb = self.layout.operator('object.pipelineUpdateSceneselections', icon='SYSTEM', text='Swap Selected Objects')
        # operator.ShotID = context.window_manager.pipelineUpdateScene_vars.ShotID
        # try:
        #     operator.Versionn = context.window_manager.pipelineUpdateScene_vars.Versionn
        # except :
        #     print("No Version")
        # operator.dirname = context.window_manager.pipelineUpdateScene_vars.dirname
        # operator.outfoldereeveeFilepath = context.window_manager.pipelineUpdateScene_vars.outfoldereeveeFilepath
        # operator.outfolderpbFilepath = context.window_manager.pipelineUpdateScene_vars.outfolderpbFilepath
        
        # operatorb.TemplateObject = context.window_manager.pipelineUpdateScene_vars.TemplateObject
        # operatorb.NewMeshName = context.window_manager.pipelineUpdateScene_vars.NewMeshName
        # operatorb.SourcePost = context.window_manager.pipelineUpdateScene_vars.SourcePost
        # operatorb.TargetCollectionPost = context.window_manager.pipelineUpdateScene_vars.TargetCollectionPost
        
        # self.layout.prop(context.window_manager.pipelineUpdateScene_vars, 'Shot ID')
        # self.layout.prop(context.window_manager.pipelineUpdateScene_vars, 'Version')
        # self.layout.prop(context.window_manager.pipelineUpdateScene_vars, 'Base Export Directory')
        # self.layout.prop(context.window_manager.pipelineUpdateScene_vars, 'Eevee Export Path')
        # self.layout.prop(context.window_manager.pipelineUpdateScene_vars, 'Workbench Export Path')



def register():
    # bpy.utils.register_class(ot)
    bpy.utils.register_class(pipelineUpdateSceneVars)
    # bpy.utils.register_class(pipelineUpdateScene_PT_panel)
    WindowManager.pipelineUpdateScene_vars = PointerProperty(type=pipelineUpdateSceneVars)

    for cls in classes:
        try:
            bpy.utils.register_class(cls)
        except ValueError as e:
            bpy.utils.unregister_class(cls)
            bpy.utils.register_class(cls)

def unregister():
	for cls in classes:
		bpy.utils.unregister_class(cls)


