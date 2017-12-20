#!/usr/bin/env python3

import re
import copy
import os.path
import itertools

def parse_file(filename):
    """Parse filename to read infos about particles. Return an array of
    particles."""

    particles = []
    with open(filename) as f:
        for line in f:
            p, v, a = re.findall("<(.*?)>", line)
            px, py, pz = list(map(int, p.split(",")))
            vx, vy, vz = list(map(int, v.split(",")))
            ax, ay, az = list(map(int, a.split(",")))

            particles.append({
                "px": px, "py": py, "pz": pz,
                "vx": vx, "vy": vy, "vz": vz,
                "ax": ax, "ay": ay, "az": az,
                })

    return particles

def distance(particle):
    """Return the mahattan distance between (0,0,0) and particle."""

    return abs(particle["px"]) + abs(particle["py"]) + abs(particle["pz"])

def closest_to_origin(particles_, max_steps):
    """Find the particle closest to origin (0, 0, 0) after a certain number of
    steps (long term).
    """

    particles = copy.deepcopy(particles_) # so we don't modify original
    for step in range(max_steps):
        for particle in particles:
            particle["vx"] += particle["ax"]
            particle["vy"] += particle["ay"]
            particle["vz"] += particle["az"]
            particle["px"] += particle["vx"]
            particle["py"] += particle["vy"]
            particle["pz"] += particle["vz"]

    closest  = 0
    min_dist = distance(particles[0])

    for i in range(1, len(particles)):
        d = distance(particles[i])
        if d < min_dist:
            closest  = i
            min_dist = d

    return closest

def n_particles_left(particles_, max_steps):
    """Return the number of particles that have not collide. Collisions occur
    when two particles are at the same position at the same step."""

    particles = copy.deepcopy(particles_) # so we don't modify original
    n = len(particles)

    has_collided  = [False for _ in range(len(particles))]
    n_destroyed   = 0

    for step in range(max_steps):
        # move every non-destroyed particles
        for i in range(n):
            if has_collided[i]:
                continue

            particles[i]["vx"] += particles[i]["ax"]
            particles[i]["vy"] += particles[i]["ay"]
            particles[i]["vz"] += particles[i]["az"]
            particles[i]["px"] += particles[i]["vx"]
            particles[i]["py"] += particles[i]["vy"]
            particles[i]["pz"] += particles[i]["vz"]

        # look for collisions for this step
        collisions = set()
        for i in range(n-1):
            # particle already destroyed, no collision
            if has_collided[i]:
                continue

            for j in range(i+1, n):
                # particles already destroyed, no collision
                if has_collided[j]:
                    continue

                if particles[i]["px"] == particles[j]["px"] and \
                   particles[i]["py"] == particles[j]["py"] and \
                   particles[i]["pz"] == particles[j]["pz"]:
                    collisions.add(i)
                    collisions.add(j)

        # set the collided particles as destroyed
        n_destroyed += len(collisions)
        for p in collisions:
            has_collided[p] = True

    return n - n_destroyed


if __name__ == "__main__":
    filename = "day20_particles.txt"
    if not os.path.exists(filename):
        print("ERROR. Name your input file as:", filename)
    else:
        particles = parse_file(filename)
        part_1 = closest_to_origin(particles, 400)
        print("PART ONE:", part_1)
        part_2 = n_particles_left(particles, 40)
        print("PART TWO:", part_2)
