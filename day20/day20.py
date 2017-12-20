#!/usr/bin/env python3

import os.path
import re

def distance(particle):
    return abs(particle["px"]) + abs(particle["py"]) + abs(particle["pz"])

def do_stuff(lines):
    particles = []
    for line in lines:
        if len(line) == 0:
            continue
        p, v, a = re.findall("<(.*?)>", line)
        px, py, pz = p.split(",")
        vx, vy, vz = v.split(",")
        ax, ay, az = a.split(",")

        particles.append({"px": int(px), "py": int(py), "pz": int(pz),
                          "vx": int(vx), "vy": int(vy), "vz": int(vz),
                          "ax": int(ax), "ay": int(ay), "az": int(az)})

    for i in range(1000):
        for particle in particles:
            particle["vx"] += particle["ax"]
            particle["vy"] += particle["ay"]
            particle["vz"] += particle["az"]
            particle["px"] += particle["vx"]
            particle["py"] += particle["vy"]
            particle["pz"] += particle["vz"]

    closest = 0
    d = distance(particles[0])

    for i in range(1, len(particles)):
        u = distance(particles[i])
        if u < d:
            closest = i
            d = u

    return closest


def collisions(lines):
    particles = []
    for line in lines:
        if len(line) == 0:
            continue
        p, v, a = re.findall("<(.*?)>", line)
        px, py, pz = p.split(",")
        vx, vy, vz = v.split(",")
        ax, ay, az = a.split(",")

        particles.append({"px": int(px), "py": int(py), "pz": int(pz),
                          "vx": int(vx), "vy": int(vy), "vz": int(vz),
                          "ax": int(ax), "ay": int(ay), "az": int(az)})

    has_collide = [False for _ in range(len(particles))]
    total_collide = 0
    for i in range(200):
        for k in range(len(particles)):
            if has_collide[k]:
                continue
            particles[k]["vx"] += particles[k]["ax"]
            particles[k]["vy"] += particles[k]["ay"]
            particles[k]["vz"] += particles[k]["az"]
            particles[k]["px"] += particles[k]["vx"]
            particles[k]["py"] += particles[k]["vy"]
            particles[k]["pz"] += particles[k]["vz"]


        collides = set()
        for k in range(len(particles)-1):
            if has_collide[k]:
                continue
            for l in range(k+1, len(particles)):
                if has_collide[l]:
                    continue
                if particles[k]["px"] == particles[l]["px"] and \
                   particles[k]["py"] == particles[l]["py"] and \
                   particles[k]["pz"] == particles[l]["pz"]:
                    collides.add(k)
                    collides.add(l)

        total_collide += len(collides)
        print("step", i, "collides:", collides, "total", total_collide)
        for c in collides:
            has_collide[c] = True


    return len(particles) - total_collide


if __name__ == "__main__":
    filename = "day20.txt"
    if not os.path.exists(filename):
        print("ERROR. Name your input file as:", filename)
    else:
        lines = open(filename).read().split("\n")
        #part_1 = do_stuff(lines)
        part_2 = collisions(lines)
        #print("PART ONE:", part_1)
        print("PART TWO:", part_2)
