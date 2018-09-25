import json

with open('fetched-discoveries.json') as f:
    meta_d = json.load(f)

with open('raw', encoding='utf-8') as f:
    head, *lines = f.readlines()
    width, height = map(float, head.split())

    def parse(point):
        x, y = point.split(maxsplit=1)

        try:
            y, z = y.split()
        except ValueError:
            z = 'm'

        x, y = map(float, [x, y])

        x = x / width
        y = y / height

        return {'x': x, 'y': y, 'z': z}

    discos = []

    for line in lines:
        index, line = line.split(maxsplit=1)
        points = list(map(parse, line.split(', ')))

        meta = meta_d[str(index)]

        disco = {
            'point': points[0].copy(),
            'name': meta['name'],
            'href': meta['href'],
        }

        if len(points) > 1:
            disco.update(path=points)

        discos.append(disco)


with open('discoveries.json', 'w') as f:
    json.dump(discos, f, indent=2)
