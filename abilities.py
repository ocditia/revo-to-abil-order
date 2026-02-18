global start_adren, rot_duration
start_adren = 1000 # multiplied by 10 to remove decimal
rot_duration = 100 # in ticks



global NECRO_AUTO, BLOAT
BLOAT = 'bloat'
NECRO_AUTO = 'necro auto'
abil1 = 'abil1'
abil2 = 'abil2'
abil3 = 'abil3'

ABILITIES = {
    NECRO_AUTO: {
        'cooldown': 3,
        'adren': 90,
        'duration': 3
    },
    BLOAT: {
        'cooldown': 0,
        'adren': -200,
        'duration': 3
    },

    abil1: {
        'cooldown': 13,
        'adren': 30,
        'duration': 3
    },
    abil2: {
        'cooldown': 17,
        'adren': -250,
        'duration': 6
    },
    abil3: {
        'cooldown': 22,
        'adren': 450,
        'duration': 4
    },
}