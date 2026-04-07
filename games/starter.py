from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from ursina.shaders.lit_with_shadows_shader import lit_with_shadows_shader

game = Ursina(title="Starter", size=(1200, 800))
player = FirstPersonController()
ground = Entity(
    model="plane",
    collider="box",
    texture="baseplate",
    scale=32,
    texture_scale=(16, 16),
    shader=lit_with_shadows_shader,
)
sky = Sky()
sun = DirectionalLight()
sun.look_at(Vec3(1, -1, 1))
sun.shadows = True


def input(key):
    hit_info = mouse.hovered_entity
    if key == "right mouse down":
        if hit_info:
            Entity(
                model="cube",
                texture="brick",
                color=color.red,
                position=hit_info.position + mouse.normal,
                collider="box",
                shader=lit_with_shadows_shader,
            )
    if key == "left mouse down":
        if hit_info:
            destroy(hit_info)


game.run()
