from ursina import *
from ursina.shaders import lit_with_shadows_shader
from ursina.prefabs.first_person_controller import FirstPersonController


class Game:
    def __init__(self):
        self.app = Ursina(title="Temu Minecraft", size=(1200, 800))
        Entity.default_shader = lit_with_shadows_shader
        self.sun = DirectionalLight(shadows=True)
        self.sun.look_at(Vec3(1, -1, 1))
        self.player = FirstPersonController(y=10, height=3)
        star_sky = Sky(texture="StarSky")
        star_sky.texture_scale = (4, 4)

    def create_blocks(self, posy: int, texture: str, collider: str, model: str):
        for a in range(10):
            for b in range(10):
                Entity(
                    model=model,
                    texture=texture,
                    scale=(2, 2, 2),
                    position=(a * 2, posy, b * 2),
                    collider=collider,
                    shader=lit_with_shadows_shader,
                )

    def run(self):
        self.app.run()


def input(key):
    hit_info = mouse.hovered_entity
    if key == "left mouse down":
        if hit_info:
            destroy(hit_info)
    if key == "right mouse down":
        if hit_info:
            pos = mouse.world_point + mouse.normal
            actualposx, actualposy, actualposz = (
                round(pos.x / 2) * 2,
                round(pos.y / 2) * 2,
                round(pos.z / 2) * 2,
            )
            actualpos = actualposx, actualposy, actualposz
            if actualposy >= 1:
                Entity(
                    model="cube",
                    scale=(2, 2, 2),
                    position=actualpos,
                    collider="box",
                    color=color.red,
                    shader=lit_with_shadows_shader,
                    texture="brick",
                )
            if actualposy <= 0 and actualposy >= -4:
                Entity(
                    model="cube",
                    scale=(2, 2, 2),
                    position=actualpos,
                    collider="box",
                    texture="grass",
                    shader=lit_with_shadows_shader,
                )
            if actualposy <= -6:
                Entity(
                    model="cube",
                    scale=(2, 2, 2),
                    position=actualpos,
                    collider="box",
                    texture="cobblestone",
                    shader=lit_with_shadows_shader,
                )
    if key == "r":
        root.player.position = (0, 10, 0)
    if key == "escape":
        mouse.locked = not mouse.locked


if __name__ == "__main__":
    root = Game()
    root.create_blocks(0, "grass", "box", "cube")
    root.create_blocks(-2, "grass", "box", "cube")
    root.create_blocks(-4, "grass", "box", "cube")
    root.create_blocks(-6, "cobblestone", "box", "cube")
    root.create_blocks(-8, "cobblestone", "box", "cube")
    root.create_blocks(-10, "cobblestone", "box", "cube")
    root.run()
