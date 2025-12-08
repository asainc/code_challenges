import sys

data = sys.stdin.read().strip().split("\n")

n = int(data[0])             
header = data[1]              

rows = data[2:]               

months_data = []
missing_positions = []       

for i, line in enumerate(rows):
    parts = line.split("\t")

    year = parts[0]
    month = parts[1]
    tmax_raw = parts[2]
    tmin_raw = parts[3]

    if tmax_raw.startswith("Missing"):
        tmax = None
        missing_positions.append((i, "tmax"))
    else:
        tmax = float(tmax_raw)

    if tmin_raw.startswith("Missing"):
        tmin = None
        missing_positions.append((i, "tmin"))
    else:
        tmin = float(tmin_raw)

    months_data.append([tmax, tmin])


def interpolate(column_index):
    
    for i in range(len(months_data)):
        if months_data[i][column_index] is None:

            up = i - 1
            while up >= 0 and months_data[up][column_index] is None:
                up -= 1

            down = i + 1
            while down < len(months_data) and months_data[down][column_index] is None:
                down += 1

            if up < 0:
                months_data[i][column_index] = months_data[down][column_index]

            elif down >= len(months_data):
                months_data[i][column_index] = months_data[up][column_index]

            else:
                prev_val = months_data[up][column_index]
                next_val = months_data[down][column_index]
                steps = down - up

                step_val = (next_val - prev_val) / steps
                offset = i - up
                months_data[i][column_index] = prev_val + step_val * offset


interpolate(0)

interpolate(1)

for idx, field in missing_positions:
    col = 0 if field == "tmax" else 1
    n = months_data[idx][col]
    print('%.1f'%(n))
