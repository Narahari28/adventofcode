import intervaltree

def get_invalid_range_in_row(sensor, beacon, row, min_val, max_val):
    ans = []
    s_x = sensor[0]
    s_y = sensor[1]
    b_x = beacon[0]
    b_y = beacon[1]
    dist = abs(s_x - b_x) + abs(s_y - b_y)

    max_cur_x = dist - abs(row - s_y) + s_x
    min_cur_x = abs(row - s_y) - dist + s_x
    if max_cur_x < min_val:
        max_cur_x = min_val
    elif max_cur_x > max_val:
        max_cur_x = max_val
    if min_cur_x < min_val:
        min_cur_x = min_val
    elif min_cur_x > max_val:
        min_cur_x = max_val
    return [min_cur_x, max_cur_x]

def unify_invalid_ranges(invalid_ranges):
    invalid_ranges = [[x[0], x[1] + 1] for x in invalid_ranges if x[0] < x[1]]
    tree = intervaltree.IntervalTree.from_tuples(invalid_ranges)
    tree.merge_overlaps()
    tree.merge_overlaps(strict=False)
    return tree

def get_invalid_in_row_for_sensor(sensor, beacon, row, occupied):
    ans = []
    s_x = sensor[0]
    s_y = sensor[1]
    b_x = beacon[0]
    b_y = beacon[1]
    dist = abs(s_x - b_x) + abs(s_y - b_y)
    cur_x = s_x
    mirror_cur_x = s_x
    cur_y = row
    cur_dist = abs(cur_x - s_x) + abs(row - s_y)
    if cur_dist <= dist:
        if not str(cur_x) + "_" + str(row) in occupied:
            ans.append(cur_x)
    while True:
        cur_x += 1
        mirror_cur_x -= 1
        cur_dist = abs(cur_x - s_x) + abs(row - s_y)
        if cur_dist <= dist:
            if not str(cur_x) + "_" + str(row) in occupied and cur_x <= max_val:
                ans.append(cur_x)
            if not str(mirror_cur_x) + "_" + str(row) in occupied and mirror_cur_x >= 0:
                ans.append(mirror_cur_x)
        else:
            break
    return ans

def get_ans(sensors, beacons, row, occupied):
    invalid_in_row = {}
    for i in range(len(sensors)):
        sensor = sensors[i]
        beacon = beacons[i]
        invalid_in_row_for_sensor = get_invalid_in_row_for_sensor(sensor, beacon, row, occupied)
        for val in invalid_in_row_for_sensor:
            invalid_in_row[val] = True
    return invalid_in_row

def get_allowed_in_row(sensors, beacons, row, occupied, min_val, max_val):
    invalid_ranges = []
    for i in range(len(sensors)):
        sensor = sensors[i]
        beacon = beacons[i]
        invalid_range = get_invalid_range_in_row(sensor, beacon, row, min_val, max_val)
        invalid_ranges.append(invalid_range)
    unified_invalid_ranges = unify_invalid_ranges(invalid_ranges)
    if len(unified_invalid_ranges) == 2:
        for interval_obj in unified_invalid_ranges:
            if interval_obj[1] != max_val + 1:
                return [interval_obj[1]]
    return []

def get_ans_2(sensors, beacons, max_val, occupied):
    for row in range(600000, max_val):
        allowed_in_row = get_allowed_in_row(sensors, beacons, row, occupied, 0, max_val)
        if len(allowed_in_row) > 0:
            return allowed_in_row[0] * 4000000 + row

def p1():
    with open('beacon_exclusion.txt') as f:
        lines = f.readlines()
        sensors = []
        beacons = []
        occupied = {}
        for line in lines:
            split = line.split(":")
            sensor = split[0]
            beacon = split[1]
            sensor_split_by_comma = sensor.split(",")
            beacon_split_by_comma = beacon.split(",")
            sensor_x_coord = int(sensor_split_by_comma[0].split("=")[1])
            sensor_y_coord = int(sensor_split_by_comma[1].split("=")[1])
            beacon_x_coord = int(beacon_split_by_comma[0].split("=")[1])
            beacon_y_coord = int(beacon_split_by_comma[1].split("=")[1])
            occupied[str(beacon_x_coord) + "_" + str(beacon_y_coord)] = True
            sensors.append([sensor_x_coord, sensor_y_coord])
            beacons.append([beacon_x_coord, beacon_y_coord])
        ans = len(get_ans(sensors, beacons, 2000000, occupied))
        print(ans, flush=True)

def p2():
    with open('beacon_exclusion.txt') as f:
        lines = f.readlines()
        sensors = []
        beacons = []
        occupied = {}
        for line in lines:
            split = line.split(":")
            sensor = split[0]
            beacon = split[1]
            sensor_split_by_comma = sensor.split(",")
            beacon_split_by_comma = beacon.split(",")
            sensor_x_coord = int(sensor_split_by_comma[0].split("=")[1])
            sensor_y_coord = int(sensor_split_by_comma[1].split("=")[1])
            beacon_x_coord = int(beacon_split_by_comma[0].split("=")[1])
            beacon_y_coord = int(beacon_split_by_comma[1].split("=")[1])
            occupied[str(beacon_x_coord) + "_" + str(beacon_y_coord)] = True
            sensors.append([sensor_x_coord, sensor_y_coord])
            beacons.append([beacon_x_coord, beacon_y_coord])
        ans = get_ans_2(sensors, beacons, 4000000, occupied)
        print(ans, flush=True)

if __name__ == "__main__":
    p2()