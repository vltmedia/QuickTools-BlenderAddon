# Quick Tools Docs

# Description

Quick Tools is a Blender addon to be used on Blender 2.8 +. The tools in this addon are made to consolidate a bunch of helpful tools under a Menu.



# Commands

## Swap Objects

### Location

- View3D > Quick Tools > Swap Objects
- View3D > N Addon Bar > Quick Tools
  - Open with the ```N``` key.

| Name                  | Description                                                  | Location                                                    |
| --------------------- | ------------------------------------------------------------ | ----------------------------------------------------------- |
| Swap Objects By Name  | Swap objects with the matching name patterns.                | View3D > Quick Tools > Swap Objects > Swap Objects By Name  |
| Swap Selected Objects | Swap selected objects the selected objects with the matching Template Object. | View3D > Quick Tools > Swap Objects > Swap Selected Objects |

![](https://vltmediablog.ml/content/images/2020/12/201207-ARH-QuickToolsv031_SwapByName_01.gif)

![](https://vltmediablog.ml/content/images/2020/12/201207-ARH-QuickToolsv031_SwapSelected_01.gif)

### Guide

1. Input ```Source Name Pattern``` to find **Base Objects to Swap**
   1. ``` CubeBig.*``` Searches for all objects named **CubeBig.** and anything after the Period. 
   2. ```CubeBig.02``` Searches strictly for object named **CubeBig.02 **
2. Input ```Template Object``` Name to find **The Object You Want To Copy**
3. Input ```New Mesh Name Template```  string for the new names of the cloned objects
4. Select a choice from ```Source Handling``` .
   1. Hide - Hides the Source objects
   2. Delete - Deletes the Source Objects
   3. Nothing - Nothing, the Source Objects stay after cloning.
5. Select a choice from ```Target Collection``` .
   1. Copy - Will place the cloned objects in the **same Collection** as the Source Objects
   2. Default - The cloned objects will be placed in the base **Collection** collection.
6. Click one of the buttons to run the function
   1. ```Swap Objects By Name``` - Use everything that you previously set. Swap objects with the matching name patterns.
   2. ```Swap Selected Objects``` - Select the objects to replace. ```The Source Name Pattern``` will not be used or referenced if this is clicked.

