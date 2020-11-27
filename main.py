@namespace
class SpriteKind:
    grafikk = SpriteKind.create()
    fornybar = SpriteKind.create()
    lokkemat = SpriteKind.create()

def on_button_pressed():
    if controller.right.is_pressed():
        mySprite.set_image(img("""
            . f f f . f f f f f . . . . 
                        f f f f f c c c c f f . . . 
                        f f f f b c c c c c c f . . 
                        f f f c 3 c c c c c c f . . 
                        . f 3 3 c c c c c c c c f . 
                        . f f f c c c c c 4 c c f . 
                        . f f f f c c c 4 4 e f f . 
                        . f f 4 4 f b f 4 4 e f f . 
                        . . f 4 d 4 1 f d d f f . . 
                        . . f f f 4 d d d d f . . . 
                        . . . f e e 4 4 4 e f . . . 
                        . . . 4 d d e 3 3 3 f . . . 
                        . . . e d d e 3 3 3 f . . . 
                        . . . f e e f 6 6 6 f . . . 
                        . . . . f f f f f f . . . . 
                        . . . . . f f f . . . . . .
        """))
    elif controller.left.is_pressed():
        mySprite.set_image(img("""
            . . . . . . . . . . . . . . 
                        . . . . f f f f f . f f f . 
                        . . . f f c c c c f f f f f 
                        . . f c c c c c c b f f f f 
                        . . f c c c c c c 3 c f f f 
                        . f c c c c c c c c 3 3 f . 
                        . f c c 4 c c c c c f f f . 
                        . f f c 4 4 c c c f f f f . 
                        . f f f 4 4 f b f 4 4 f f . 
                        . . f f d d f 1 4 d 4 f . . 
                        . . . f d d d e e f f f . . 
                        . . . f e 4 e d d 4 f . . . 
                        . . . f 3 3 e d d e f . . . 
                        . . f f 6 6 f e e f f f . . 
                        . . f f f f f f f f f f . . 
                        . . . f f f . . . f f . . .
        """))
    elif controller.up.is_pressed():
        mySprite.set_image(img("""
            . . . . . . . . . . . . . . 
                        . f f f . f f f f . f f f . 
                        f f f f f c c c c f f f f f 
                        f f f f b c c c c b f f f f 
                        f f f c 3 c c c c 3 c f f f 
                        . f 3 3 c c c c c c 3 3 f . 
                        . f c c c c c c c c c f f . 
                        . f f c c c c c c c c f f . 
                        . f f c c c c c c f f f f . 
                        . f f f f f f f f f f f f . 
                        . . f f f f f f f f f f . . 
                        . . e f f f f f f f f e . . 
                        . . e f f f f f f f f 4 e . 
                        . . 4 f 3 3 3 3 3 e d d 4 . 
                        . . e f f f f f f e e 4 . . 
                        . . . f f f . . . . . . . .
        """))
    elif controller.down.is_pressed():
        mySprite.set_image(img("""
            . f f f . f f f f . f f f . 
                        f f f f f c c c c f f f f f 
                        f f f f b c c c c b f f f f 
                        f f f c 3 c c c c 3 c f f f 
                        . f 3 3 c c c c c c 3 3 f . 
                        . f c c c c 4 4 c c c c f . 
                        . f f c c 4 4 4 4 c c f f . 
                        . f f f b f 4 4 f b f f f . 
                        . f f 4 1 f d d f 1 4 f f . 
                        . . f f d d d d d d f f . . 
                        . . e f e 4 4 4 4 e f e . . 
                        . e 4 f b 3 3 3 3 b f 4 e . 
                        . 4 d f 3 3 3 3 3 3 c d 4 . 
                        . 4 4 f 6 6 6 6 6 6 f 4 4 . 
                        . . . . f f f f f f . . . . 
                        . . . . f f . . f f . . . .
        """))
    else:
        pass
controller.any_button.on_event(ControllerButtonEvent.PRESSED, on_button_pressed)

def on_overlap_tile(sprite, location):
    vann.set_image(img("""
        . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . .
    """))
    effects.clear_particles(mySprite)
scene.on_overlap_tile(SpriteKind.player, myTiles.transparency16, on_overlap_tile)

def on_a_pressed():
    global lokkemat2
    lokkemat2 = sprites.create(img("""
            . . . . c c c b b b b b . . . . 
                    . . c c b 4 4 4 4 4 4 b b b . . 
                    . c c 4 4 4 4 4 5 4 4 4 4 b c . 
                    . e 4 4 4 4 4 4 4 4 4 5 4 4 e . 
                    e b 4 5 4 4 5 4 4 4 4 4 4 4 b c 
                    e b 4 4 4 4 4 4 4 4 4 4 5 4 4 e 
                    e b b 4 4 4 4 4 4 4 4 4 4 4 b e 
                    . e b 4 4 4 4 4 5 4 4 4 4 b e . 
                    8 7 e e b 4 4 4 4 4 4 b e e 6 8 
                    8 7 2 e e e e e e e e e e 2 7 8 
                    e 6 6 2 2 2 2 2 2 2 2 2 2 6 c e 
                    e c 6 7 6 6 7 7 7 6 6 7 6 c c e 
                    e b e 8 8 c c 8 8 c c c 8 e b e 
                    e e b e c c e e e e e c e b e e 
                    . e e b b 4 4 4 4 4 4 4 4 e e . 
                    . . . c c c c c e e e e e . . .
        """),
        SpriteKind.lokkemat)
    lokkemat2.set_position(mySprite.x, mySprite.y)
    info.change_score_by(-10)
    gakkGakk.follow(lokkemat2)
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def on_countdown_end():
    if info.score() < 30:
        game.over(False)
    else:
        game.over(True)
info.on_countdown_end(on_countdown_end)

def on_on_overlap(sprite, otherSprite):
    tiles.place_on_random_tile(otherSprite, myTiles.tile1)
    info.change_score_by(1)
sprites.on_overlap(SpriteKind.player, SpriteKind.fornybar, on_on_overlap)

def on_on_overlap2(sprite, otherSprite):
    info.change_life_by(-1)
    gakkGakk.say("GNAFS GNAFS", 500)
    gakkGakk.start_effect(effects.fire, 500)
    pause(500)
    tiles.place_on_random_tile(gakkGakk, myTiles.tile1)
sprites.on_overlap(SpriteKind.enemy, SpriteKind.player, on_on_overlap2)

def on_on_overlap3(sprite, otherSprite):
    otherSprite.destroy(effects.disintegrate, 1000)
    gakkGakk.say("GNAFS GNAFS", 500)
    gakkGakk.start_effect(effects.fire, 500)
    pause(5000)
    gakkGakk.follow(mySprite, 50)
sprites.on_overlap(SpriteKind.enemy, SpriteKind.lokkemat, on_on_overlap3)

def on_on_overlap4(sprite, otherSprite):
    otherSprite.destroy()
    info.change_score_by(2)
sprites.on_overlap(SpriteKind.player, SpriteKind.food, on_on_overlap4)

def on_overlap_tile2(sprite, location):
    vann.set_image(img("""
        . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 
                9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 
                9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 
                9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 
                9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 
                9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 
                9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 
                9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9
    """))
    vann.set_position(mySprite.x, mySprite.y)
    mySprite.start_effect(effects.spray)
    mySprite.say("blubb blubb", 200)
scene.on_overlap_tile(SpriteKind.player, myTiles.tile1, on_overlap_tile2)

def on_overlap_tile3(sprite, location):
    if info.score() < 50:
        game.splash("Du reiser hjem tomhendt, og alle er veldig skuffet over deg")
        game.over(False)
    else:
        game.splash("Du kommer hjem og blir mottatt som en helt!")
        game.over(True)
scene.on_overlap_tile(SpriteKind.player,
    sprites.dungeon.collectible_insignia,
    on_overlap_tile3)

lokkemat2: Sprite = None
gakkGakk: Sprite = None
vind: Sprite = None
vann: Sprite = None
energi: Sprite = None
mySprite: Sprite = None
tiles.set_tilemap(tilemap("""
    level
"""))
scene.set_background_color(9)
mySprite = sprites.create(img("""
        . f f f . f f f f . f f f . 
            f f f f f c c c c f f f f f 
            f f f f b c c c c b f f f f 
            f f f c 3 c c c c 3 c f f f 
            . f 3 3 c c c c c c 3 3 f . 
            . f c c c c 4 4 c c c c f . 
            . f f c c 4 4 4 4 c c f f . 
            . f f f b f 4 4 f b f f f . 
            . f f 4 1 f d d f 1 4 f f . 
            . . f f d d d d d d f f . . 
            . . e f e 4 4 4 4 e f e . . 
            . e 4 f b 3 3 3 3 b f 4 e . 
            . 4 d f 3 3 3 3 3 3 c d 4 . 
            . 4 4 f 6 6 6 6 6 6 f 4 4 . 
            . . . . f f f f f f . . . . 
            . . . . f f . . f f . . . .
    """),
    SpriteKind.player)
if Math.percent_chance(20):
    tiles.place_on_random_tile(mySprite, sprites.castle.tile_path5)
else:
    tiles.place_on_random_tile(mySprite, sprites.castle.tile_grass1)
controller.move_sprite(mySprite)
scene.camera_follow_sprite(mySprite)
for index in range(randint(90, 110)):
    energi = sprites.create(img("""
            . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . f f f f . . . . . 
                    . . . . . . f f 4 5 f . . . . . 
                    . . . . . . f 4 4 f f . . . . . 
                    . . . . . f f 4 f f . . . . . . 
                    . . . . f f 4 4 f f f . . . . . 
                    . . . . f 5 4 4 4 4 f . . . . . 
                    . . . . f f f f 4 5 f . . . . . 
                    . . . . . . f 5 4 f f . . . . . 
                    . . . . . f f 5 f f . . . . . . 
                    . . . . . f 5 f f . . . . . . . 
                    . . . . . f f f . . . . . . . . 
                    . . . . . . . . . . . . . . . .
        """),
        SpriteKind.food)
    if Math.percent_chance(80):
        tiles.place_on_random_tile(energi, sprites.castle.tile_path5)
    else:
        tiles.place_on_random_tile(energi, sprites.castle.tile_grass1)
vann = sprites.create(img("""
        . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 
            9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 
            9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 
            9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 
            9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 
            9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 
            9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 
            9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9
    """),
    SpriteKind.grafikk)
for index2 in range(randint(20, 30)):
    vind = sprites.create(img("""
            . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . 8 8 8 8 8 . . . . 
                    . . . . . 8 8 1 1 1 1 8 . . . . 
                    . . . 8 8 1 1 . . . 1 8 . . . . 
                    . . . 8 . . . . . 1 8 . . . . . 
                    . . . 8 8 . . . . . . . . . . . 
                    . . . 1 8 8 8 . . 8 8 8 8 8 . . 
                    . . . . 1 1 1 8 8 1 1 1 1 1 . . 
                    . . . . . . . 1 1 . . . . . . . 
                    . . . 8 8 8 8 . . . . . . . . . 
                    . . . 8 1 1 8 . . . . 8 8 8 . . 
                    . . . 8 8 . . . 8 8 8 1 1 1 8 . 
                    . . . 1 8 8 8 8 8 1 1 . . . 1 . 
                    . . . . . 1 1 1 1 . . . . . . .
        """),
        SpriteKind.fornybar)
    tiles.place_on_random_tile(vind, myTiles.tile1)
info.set_life(3)
gakkGakk = sprites.create(img("""
        . . . . . . . . . b 5 b . . . . 
            . . . . . . . . . b 5 b . . . . 
            . . . . . . b b b b b b . . . . 
            . . . . . b b 5 5 5 5 5 b . . . 
            . . . . b b 5 b c 5 5 d 4 c . . 
            . b b b b 5 5 5 b f d d 4 4 4 b 
            . b d 5 b 5 5 b c b 4 4 4 4 b . 
            . . b 5 5 b 5 5 5 4 4 4 4 b . . 
            . . b d 5 5 b 5 5 5 5 5 5 b . . 
            . b d b 5 5 5 d 5 5 5 5 5 5 b . 
            b d d c d 5 5 b 5 5 5 5 5 5 b . 
            c d d d c c b 5 5 5 5 5 5 5 b . 
            c b d d d d d 5 5 5 5 5 5 5 b . 
            . c d d d d d d 5 5 5 5 5 d b . 
            . . c b d d d d d 5 5 5 b b . . 
            . . . c c c c c c c c b b . . .
    """),
    SpriteKind.enemy)
gakkGakk.follow(mySprite, 50)