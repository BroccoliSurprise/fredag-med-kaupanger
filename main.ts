namespace SpriteKind {
    export const grafikk = SpriteKind.create()
    export const fornybar = SpriteKind.create()
    export const lokkemat = SpriteKind.create()
}
controller.anyButton.onEvent(ControllerButtonEvent.Pressed, function () {
    if (controller.right.isPressed()) {
        mySprite.setImage(img`
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
            `)
    } else if (controller.left.isPressed()) {
        mySprite.setImage(img`
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
            `)
    } else if (controller.up.isPressed()) {
        mySprite.setImage(img`
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
            `)
    } else if (controller.down.isPressed()) {
        mySprite.setImage(img`
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
            `)
    } else {
    	
    }
})
scene.onOverlapTile(SpriteKind.Player, myTiles.transparency16, function (sprite, location) {
    vann.setImage(img`
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
        `)
    effects.clearParticles(mySprite)
})
controller.A.onEvent(ControllerButtonEvent.Pressed, function () {
    lokkemat2 = sprites.create(img`
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
        `, SpriteKind.lokkemat)
    lokkemat2.setPosition(mySprite.x, mySprite.y)
    info.changeScoreBy(-10)
    gakkGakk.follow(lokkemat2)
})
info.onCountdownEnd(function () {
    if (info.score() < 30) {
        game.over(false)
    } else {
        game.over(true)
    }
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.fornybar, function (sprite, otherSprite) {
    tiles.placeOnRandomTile(otherSprite, myTiles.tile1)
    info.changeScoreBy(1)
})
sprites.onOverlap(SpriteKind.Enemy, SpriteKind.Player, function (sprite, otherSprite) {
    info.changeLifeBy(-1)
    gakkGakk.say("GNAFS GNAFS", 500)
    gakkGakk.startEffect(effects.fire, 500)
    pause(500)
    tiles.placeOnRandomTile(gakkGakk, myTiles.tile1)
})
sprites.onOverlap(SpriteKind.Enemy, SpriteKind.lokkemat, function (sprite, otherSprite) {
    otherSprite.destroy(effects.disintegrate, 1000)
    gakkGakk.say("GNAFS GNAFS", 500)
    gakkGakk.startEffect(effects.fire, 500)
    pause(5000)
    gakkGakk.follow(mySprite, 50)
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.Food, function (sprite, otherSprite) {
    otherSprite.destroy()
    info.changeScoreBy(2)
})
scene.onOverlapTile(SpriteKind.Player, myTiles.tile1, function (sprite, location) {
    vann.setImage(img`
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
        `)
    vann.setPosition(mySprite.x, mySprite.y)
    mySprite.startEffect(effects.spray)
    mySprite.say("blubb blubb", 200)
})
scene.onOverlapTile(SpriteKind.Player, sprites.dungeon.collectibleInsignia, function (sprite, location) {
    if (info.score() < 50) {
        game.splash("Du reiser hjem tomhendt, og alle er veldig skuffet over deg")
        game.over(false)
    } else {
        game.splash("Du kommer hjem og blir mottatt som en helt!")
        game.over(true)
    }
})
let lokkemat2: Sprite = null
let gakkGakk: Sprite = null
let vind: Sprite = null
let vann: Sprite = null
let energi: Sprite = null
let mySprite: Sprite = null
tiles.setTilemap(tilemap`level`)
scene.setBackgroundColor(9)
mySprite = sprites.create(img`
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
    `, SpriteKind.Player)
if (Math.percentChance(20)) {
    tiles.placeOnRandomTile(mySprite, sprites.castle.tilePath5)
} else {
    tiles.placeOnRandomTile(mySprite, sprites.castle.tileGrass1)
}
controller.moveSprite(mySprite)
scene.cameraFollowSprite(mySprite)
for (let index = 0; index < randint(90, 110); index++) {
    energi = sprites.create(img`
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
        `, SpriteKind.Food)
    if (Math.percentChance(80)) {
        tiles.placeOnRandomTile(energi, sprites.castle.tilePath5)
    } else {
        tiles.placeOnRandomTile(energi, sprites.castle.tileGrass1)
    }
}
vann = sprites.create(img`
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
    `, SpriteKind.grafikk)
for (let index = 0; index < randint(20, 30); index++) {
    vind = sprites.create(img`
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
        `, SpriteKind.fornybar)
    tiles.placeOnRandomTile(vind, myTiles.tile1)
}
info.setLife(3)
gakkGakk = sprites.create(img`
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
    `, SpriteKind.Enemy)
gakkGakk.follow(mySprite, 50)
