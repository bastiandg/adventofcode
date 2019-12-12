#!/usr/bin/env python3

import sys

input = open("day07.txt", "r").read().split("\n")[:-1]


def root_program(input):
    programs = set([p.split(" ")[0] for p in input])
    input_programs = set()
    for line in input:
        bottom_programs = line.split(" -> ")
        if len(bottom_programs) > 1:
            input_programs.update(bottom_programs[1].split(", "))
    return list(programs - input_programs)[0]


def calc_correct_sum(sum_list):
    for i, x in enumerate(sum_list):
        if x in sum_list[:i] or x in sum_list[i + 1:]:
            return x


def sum_weights(programs, name):
    program_sum = 0
    sub_list = []
    for program_name in programs[name][2]:
        if programs[program_name][1] == -1:
            sum_weights(programs, program_name)
        sub_list.append(programs[program_name][1])
        program_sum += programs[program_name][1]
    programs[name][1] = program_sum + programs[name][0]
    if len(set(sub_list)) > 1:
        correct_sum = calc_correct_sum(sub_list)
        for program_name in programs[name][2]:
            if programs[program_name][1] != correct_sum:
                correction = programs[program_name][0] - (programs[program_name][1] - correct_sum)
                print("correction: %s %i -> %i" % (program_name,
                                                   programs[program_name][0],
                                                   correction))
                sys.exit(0)


def weight_balance(input, root):
    programs = dict()
    for line in input:
        line_split = line.split(" -> ")
        dependent_programs = []
        weight = int(line_split[0][:-1].split("(")[1])
        name = line_split[0].split(" ")[0]
        if len(line_split) > 1:
            dependent_programs = line_split[1].split(", ")
            weight_sum = -1
        else:
            weight_sum = weight
        programs[name] = [weight, weight_sum, dependent_programs]
    sum_weights(programs, root)


root = root_program(input)
print("root %s" % root)
weight_balance(input, root)
