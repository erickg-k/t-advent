from dataclasses import dataclass, field
from os import read
from typing import List, Dict, Tuple, Deque, Optional
from collections import deque

def gen_board_slice():
    return [0, 0, 0, 0, 0]

@dataclass
class Position:
    x: int
    y: int

@dataclass
class Reading:
    start: Position
    end: Position

def read_water(input_filepath, straight_constraint):
    readings = []
    max_position = Position(0, 0)

    with open(input_filepath) as infile:
        for line in infile:
            line = line.strip()
            if line == "": continue

            start, end = line.split(" -> ")
            start = list(map(int,start.split(",")))
            end = list(map(int,end.split(",")))

            reading = Reading(start=Position(*start), end=Position(*end))
            if straight_constraint:
                if not (reading.start.x == reading.end.x or reading.start.y == reading.end.y):
                    continue
            max_position.x = max(max(max_position.x, reading.start.x), reading.end.x)
            max_position.y = max(max(max_position.y, reading.start.y), reading.end.y)

            readings.append(reading)

    return readings, max_position

def construct_map(max_position):
    return [[0] * (max_position.x+1) for _ in range(max_position.y+1)]

def detect_water(readings: List[Reading], water_map: List[List[int]]):
    for reading in readings:
        if reading.start.x == reading.end.x:
            for y in range(min(reading.start.y, reading.end.y), max(reading.start.y, reading.end.y)+1):
                water_map[y][reading.start.x] += 1
        elif reading.start.y == reading.end.y:
            for x in range(min(reading.start.x, reading.end.x), max(reading.start.x, reading.end.x)+1):
                water_map[reading.start.y][x] += 1
        else:
            min_y = min(reading.start.y, reading.end.y)
            # max_y = max(reading.start.y, reading.end.y)
            min_x = min(reading.start.x, reading.end.x)
            # max_x = max(reading.start.x, reading.end.x)

            x = reading.start.x
            y = reading.start.y
            while x != reading.end.x:
                water_map[y][x] += 1
                if min_y == reading.start.y:
                    y += 1
                elif min_y != reading.start.y:
                    y -= 1
                if min_x == reading.start.x:
                    x += 1
                elif min_x != reading.start.x:
                    x -= 1
            if x != reading.start.x and y != reading.start.y:
                water_map[y][x] += 1
            # print_map(water_map)


    return count_dangerous_point(water_map)


def detect_water_opt(readings: List[Reading], water_map: List[List[int]]):
    for reading in readings:
        min_y = min(reading.start.y, reading.end.y)
        max_y = max(reading.start.y, reading.end.y)
        min_x = min(reading.start.x, reading.end.x)
        max_x = max(reading.start.x, reading.end.x)

        k_exist = reading.start.x != reading.end.x

        if k_exist:
            k_val = (reading.end.y - reading.start.y) / (reading.end.x - reading.start.x)
            y = min_y if k_val > 0.0 else max_y
            for x in range(min_x, max_x+1):
                if y < 0 or y >= len(water_map):
                    break
                water_map[y][x] += 1
                # print(reading, k_val, f"({x}, {y})")
                
                if k_val > 0.0:
                    y += 1
                elif k_val < 0.0:
                    y -= 1
        else:
            for y in range(min_y, max_y+1):
                water_map[y][min_x] += 1

        # print_map(water_map)

    return count_dangerous_point(water_map)

def print_map(water_map):
    for row in water_map:
        for x in row:
            if x == 0:
                print('.', end="")
            else:
                print(x, end="")
        print("")
    print("")


def count_dangerous_point(water_map):
    cnt_danger = 0
    for row in water_map:
        for num in row:
            if num >= 2:
                cnt_danger += 1
    
    print(cnt_danger)
    return cnt_danger

if __name__ == "__main__":
    readings, max_position = read_water("input", straight_constraint=False)
    # print(readings)
    water_map = construct_map(max_position)
    water = detect_water(readings, water_map)
    water_map = construct_map(max_position)
    assert water == detect_water_opt(readings, water_map)
