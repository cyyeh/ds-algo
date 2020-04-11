# Uses python3
import sys

def fast_count_segments(starts, ends, points):
    cnt = [0] * len(points)

    segments_points_sorted = sorted(starts + ends + points, key = lambda x: (x[0], x[2]))
    segment_count = 0

    for unit in segments_points_sorted:
        if unit[1] == 'l':
            segment_count += 1
        elif unit[1] == 'r':
            segment_count -= 1
        else:
            cnt[unit[2]] = segment_count

    return cnt

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[1]
    starts = [(start, 'l', -1) for start in data[2:2 * n + 2:2]]
    ends   = [(end, 'r', m) for end in data[3:2 * n + 2:2]]
    points = [(point, 'p', index) for index, point in enumerate(data[2 * n + 2:])]
    cnt = fast_count_segments(starts, ends, points)
    for x in cnt:
        print(x, end=' ')
