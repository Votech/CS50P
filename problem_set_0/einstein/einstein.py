def mass_to_joules(mass_kg):
    c = 3e8
    energy_joules = mass_kg * c**2
    return int(energy_joules)


def main():
    mass = int(input())
    print(mass_to_joules(mass))


main()
