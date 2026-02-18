from abilities import *

ability_bar = { # put auto as last abil always
    1: abil1,
    2: abil2,
    3: abil3,
    4: BLOAT,
    5: NECRO_AUTO
}

# construct ability_bar with cooldowns
for key in ability_bar:
    ability_bar[key] = [ability_bar[key], 0]


def left_most_off_cd_abil(ability_bar, adren):
    for key in ability_bar:
        if ability_bar[key][1] == 0 and adren >= -ABILITIES[ability_bar[key][0]]['adren']:
            return key # return the slot which should be fired off

# rotation
rotation_duration = rot_duration
adren = start_adren 
gcd = 1
for tick in range(rotation_duration):
    gcd -= 1
    if gcd == 0: # fire next abil
        key = left_most_off_cd_abil(ability_bar,adren)
        gcd = ABILITIES[ability_bar[key][0]]['duration']
        adren += ABILITIES[ability_bar[key][0]]['adren']
        ability_bar[key][1] = ABILITIES[ability_bar[key][0]]['cooldown']
        print(tick, ability_bar[key][0])

    # reduce cd of all abils by 1
    for key in ability_bar:
        if ability_bar[key][1] > 0:
            ability_bar[key][1] -= 1
    