import bpy
from .operators import (
    SUFE_OT_AddEditor,
    SUFE_OT_AddShells,
    SUFE_OT_SwitchVertexColors,
    SUFE_OT_SetBrushDir,
)

class SUFT_PT_Tools(bpy.types.Panel):
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Tool"
    bl_options = {'DEFAULT_CLOSED'}
    bl_label = "Sonic Unleashed Fur Editor"

    @classmethod
    def poll(cls, context):
        return context.mode in ["OBJECT", "PAINT_VERTEX"]

    def draw(self, context):
        if context.mode == "OBJECT":
            self.layout.operator(SUFE_OT_AddShells.bl_idname)
            self.layout.operator(SUFE_OT_AddEditor.bl_idname)
            return

        util_props = context.scene.sufe_settings

        self.layout.use_property_split = True
        self.layout.use_property_decorate = False
        color_name = context.active_object.data.color_attributes.active_color_name


        header = self.layout.row()
        header.operator(SUFE_OT_SwitchVertexColors.bl_idname, text="", icon="BRUSH_DATA").attribute_name = "FurDirection"
        header.label(text="Fur direction")

        dirblock = self.layout.column()
        dirblock.active = color_name == "FurDirection"

        split = dirblock.split(factor=0.5)
        split.prop(util_props, "vertex_paint_direction", text="")
        col = split.column()
        col.prop(util_props, "vertex_paint_direction", text="", index=0)
        col.prop(util_props, "vertex_paint_direction", text="", index=1)
        col.prop(util_props, "vertex_paint_direction", text="", index=2)

        row = dirblock.row()
        operator = SUFE_OT_SetBrushDir.bl_idname
        row.operator(operator, text="+X").direction = (1,0,0)
        row.operator(operator, text="-X").direction = (-1,0,0)
        row.operator(operator, text="+Y").direction = (0,1,0)
        row.operator(operator, text="-Y").direction = (0,-1,0)
        row.operator(operator, text="+Z").direction = (0,0,1)
        row.operator(operator, text="-Z").direction = (0,0,-1)
        dirblock.label(text="Pointing towards: " + util_props.vertex_direction_info)

        dirblock.prop(util_props, "vertex_paint_factor", text="Normal <-> Color")

        self.layout.separator(type='LINE')

        header = self.layout.row()
        header.operator(SUFE_OT_SwitchVertexColors.bl_idname, text="", icon="BRUSH_DATA").attribute_name = "FurLength"
        header.label(text="Fur length")

        lengthblock = self.layout.column()
        lengthblock.active = color_name == "FurLength"
        lengthblock.prop(util_props, "vertex_paint_length", text="")