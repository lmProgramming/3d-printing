import trimesh

outer_width = 2.6
outer_depth = 17.0
outer_height = 22.0
wall_thickness = 0.3

left_wall = trimesh.creation.box(
    extents=[wall_thickness, outer_depth, outer_height])
right_wall = trimesh.creation.box(
    extents=[wall_thickness, outer_depth, outer_height])

front_wall = trimesh.creation.box(
    extents=[outer_width, wall_thickness, outer_height])

left_wall.apply_translation(
    [-outer_width / 2 + wall_thickness / 2, 0, outer_height / 2])
right_wall.apply_translation(
    [outer_width / 2 - wall_thickness / 2, 0, outer_height / 2])
front_wall.apply_translation(
    [0, -outer_depth / 2 + wall_thickness / 2, outer_height / 2])

stl = trimesh.util.concatenate([left_wall, right_wall, front_wall])

filename = "kitchen_fix/sliding_cover.stl"
stl.export(filename)
