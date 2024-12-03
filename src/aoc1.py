
import re

from bisect import insort
from dataclasses import dataclass, field
from helpers import read_file, setup_custom_logger

log = setup_custom_logger("aoc-2024")

@dataclass
class PuzzleInput:
    left_list: list = field(default_factory=list)
    right_list: list = field(default_factory=list)

def order_puzzle_data(file_content, puzzle_input: PuzzleInput) -> PuzzleInput:
    for item in file_content:
        regex_match = re.findall("\\b(\d+)\\b", item)
        insort(puzzle_input.left_list, int(regex_match[0]))
        insort(puzzle_input.right_list, int(regex_match[1]))
    return puzzle_input

def calculate_total_distance(puzzle_data: PuzzleInput) -> int:
    distance = 0
    for item in range(0, len(puzzle_data.left_list)):
        distance += abs(puzzle_data.right_list[item] - puzzle_data.left_list[item])
    return distance

def calculate_similarity(puzzle_data: PuzzleInput) -> int:
    similarity = 0
    for item in range(0, len(puzzle_data.left_list)):
        similarity += puzzle_data.left_list[item] * puzzle_data.right_list.count(puzzle_data.left_list[item])
    return similarity

if __name__ == "__main__":
    file_content = read_file("../files/aoc1.txt")
    puzzle_input = PuzzleInput()
    puzzle_data = order_puzzle_data(file_content, puzzle_input)
    log.info(f"Distance {calculate_total_distance(puzzle_data)} and Similarity {calculate_similarity(puzzle_data)}")