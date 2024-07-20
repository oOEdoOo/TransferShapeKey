bl_info = {
    "name": "Shapekey Copy",
    "blender": (4, 1, 0),
    "category": "Tool",
    "author": "Liu Min, Blender Bob, Chat GPT",
}

import bpy
from bpy.props import PointerProperty

class ShapekeyTransferPanel(bpy.types.Panel):
    bl_label = "Shapekeys Copy"
    bl_idname = "PT_ShapekeyTransfer"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Tool'

    def draw(self, context):
        layout = self.layout
        layout.prop_search(context.scene, "shapekey_source", context.scene, "objects", text="Source")
        layout.prop_search(context.scene, "shapekey_target", context.scene, "objects", text="Target")
        layout.operator("object.shapekey_transfer", text="Copy")

class ShapekeyTransferOperator(bpy.types.Operator):
    bl_idname = "object.shapekey_transfer"
    bl_label = "Transfer Shapekeys"
    bl_description = "Transfer shapekeys from source to target object"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        source_object = context.scene.shapekey_source
        target_object = context.scene.shapekey_target

        if source_object is None or target_object is None:
            self.report({'ERROR'}, "Please select both source and target objects.")
            return {'CANCELLED'}

        if not source_object.data.shape_keys:
            self.report({'ERROR'}, f"'{source_object.name}' does not have shape keys.")
            return {'CANCELLED'}

        # 打开此处，禁止不同顶点数量的对象之间进行形状键的复制
        # if len(source_object.data.vertices) != len(target_object.data.vertices):
        #     self.report({'WARN'}, "Source and target objects must have the same number of vertices.")
            # return {'CANCELLED'}

        with bpy.context.temp_override(active_object=target_object):
            for key in source_object.data.shape_keys.key_blocks:
                if key.name not in target_object.data.shape_keys.key_blocks:
                    bpy.ops.object.shape_key_add(from_mix=False)
                    target_object.data.shape_keys.key_blocks[-1].name = key.name

                for vert_src, vert_tgt in zip(key.data, target_object.data.shape_keys.key_blocks[key.name].data):
                    vert_tgt.co = vert_src.co

        self.report({'INFO'}, f"Shape keys copied from '{source_object.name}' to '{target_object.name}'.")
        return {'FINISHED'}

def register():
    bpy.utils.register_class(ShapekeyTransferPanel)
    bpy.utils.register_class(ShapekeyTransferOperator)
    bpy.types.Scene.shapekey_source = PointerProperty(type=bpy.types.Object, name="Source Object")
    bpy.types.Scene.shapekey_target = PointerProperty(type=bpy.types.Object, name="Target Object")

def unregister():
    bpy.utils.unregister_class(ShapekeyTransferPanel)
    bpy.utils.unregister_class(ShapekeyTransferOperator)
    del bpy.types.Scene.shapekey_source
    del bpy.types.Scene.shapekey_target

if __name__ == "__main__":
    register()