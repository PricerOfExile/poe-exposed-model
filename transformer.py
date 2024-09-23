# input will be the result of json.load(f)
def rarity_array(data):
    rarity = data['rarity']
    if rarity == "Normal":
        return [1, 0, 0]
    elif rarity == "Magic":
        return [0, 1, 0]
    elif rarity == "Rare":
        return [0, 0, 1]
    else:
        return [0, 0, 0]


def socket_array(data):
    socket = data['socket']
    if socket == 'N':
        return [1, 0, 0, 0, 0, 0]
    elif socket == 'A':
        return [0, 1, 0, 0, 0, 0]
    elif socket == 'B':
        return [0, 0, 1, 0, 0, 0]
    elif socket == 'R':
        return [0, 0, 0, 1, 0, 0]
    elif socket == 'G':
        return [0, 0, 0, 0, 1, 0]
    elif socket == 'W':
        return [0, 0, 0, 0, 0, 1]
    else:
        return [0, 0, 0, 0, 0, 0]


def identified_array(data):
    identified = data['identified']
    if identified:
        return [1, 0]
    else:
        return [0, 1]


def influence_array(data):
    influences = data['influences']
    return [
        1 if influences['warlord'] else 0,
        1 if influences['hunter'] else 0,
        1 if influences['redeemer'] else 0,
        1 if influences['crusader'] else 0,
        1 if influences['shaper'] else 0,
        1 if influences['elder'] else 0,
    ]


def fractured_array(data):
    fractured = data['fractured']
    if fractured:
        return [1, 0]
    else:
        return [0, 1]


def synthesised_array(data):
    synthesised = data['synthesised']
    if synthesised:
        return [1, 0]
    else:
        return [0, 1]


def duplicated_array(data):
    duplicated = data['duplicated']
    if duplicated:
        return [1, 0]
    else:
        return [0, 1]


def split_array(data):
    split = data['split']
    if split:
        return [1, 0]
    else:
        return [0, 1]


def corrupted_array(data):
    corrupted = data['corrupted']
    if corrupted:
        return [1, 0]
    else:
        return [0, 1]


def qualities_array(data):
    qualities = data['qualities']
    return [
        qualities["attack"],
        qualities["attribute"],
        qualities["caster"],
        qualities["critical"],
        qualities["defense"],
        qualities["elemental"],
        qualities["lifeAndMana"],
        qualities["physicalAndChaos"],
        qualities["resistance"],
        qualities["speed"]
    ]


def valuated_stats_array(data):
    valuated = data["valuatedStats"]
    sorted_valuated = sorted(valuated, key=lambda p: p["id"])
    return [p["value"] for p in sorted_valuated]


def transform(data):
    return rarity_array(data) + [data['ilvl']] + identified_array(data) + [data['levelRequirement']] + socket_array(data) + influence_array(data) + fractured_array(data) + synthesised_array(data) + duplicated_array(data) + split_array(data) + corrupted_array(data) + qualities_array(data) + valuated_stats_array(data)