

with open("input.txt", "r") as input_file:
    raw_games = input_file.readlines()


def assign_color(input: str):
    if "red" in input:
        return "red"
    elif "green" in input:
        return "green"
    else:
        return "blue"


games = []

for idx, game in enumerate(raw_games):
    remove_game_number = game.split(":")[1].strip()
    all_pulls = remove_game_number.split(";")
    cube_sets = [pull.strip().split(",") for pull in all_pulls]
    game_sets = []
    for cubes in cube_sets:
        set = {}
        for cube in cubes:
            color = assign_color(cube)
            number = int(cube.replace(f"{color}", "").strip())
            set[color] = number
        game_sets.append(set)
    game = {
        "game": idx+1,
        "game_sets": game_sets
    }
    games.append(game)


def part_one(games):
    valid_games = 0
    for game in games:
        for game_set in game["game_sets"]:
            invalid = False
            if game_set.get("red", 0) > 12:
                invalid = True
                break
            if game_set.get("blue", 0) > 14:
                invalid = True
                break
            if game_set.get("green", 0) > 13:
                invalid = True
                break
        if not invalid:
            valid_games += game["game"]
    print(valid_games)


def part_two(games):
    total_power = 0
    for game in games:
        max_red = max([set.get("red", 0) for set in game["game_sets"]])
        max_blue = max([set.get("blue", 0) for set in game["game_sets"]])
        max_green = max([set.get("green", 0) for set in game["game_sets"]])
        color_power = max_red * max_blue * max_green
        print(color_power)
        total_power += color_power
    print(total_power)


part_two(games)
