import json

with open('data/raw-discoveries', encoding='utf-8') as f:
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

    data = []

    for line in lines:
        index, line = line.split(maxsplit=1)
        points = list(map(parse, line.split(', ')))

        data.append(points[0] if len(points) == 1 else points)


with open('data/discoveries.json', 'w') as f:
    json.dump(data, f)
