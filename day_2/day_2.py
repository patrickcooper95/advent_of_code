# Scoring
score_sheet = {"X": "C", "Y": "A", "Z": "B", "A": "Z", "B": "X", "C": "Y"}
weapon_score = {"X": 1, "Y": 2, "Z": 3, "A": 1, "B": 2, "C": 3}
alias = {"rock": ["A", "X"], "paper": ["B", "Y"], "scissors": ["C", "Z"]}

with open("strategy_guide.txt", "r") as strat_file:
	games = strat_file.readlines()


def part_one():
	points = 0
	for game in games:
		clean_game = game.strip().split(" ")
		print(clean_game)

		# assign points for weapon of choice
		points += weapon_score[clean_game[1]]

		# points for result of the match
		if score_sheet[clean_game[0]] == clean_game[1]:
			winner = ""
			loser = ""
			for k, v in alias.items():
				if clean_game[0] in v:
					winner = k
				if clean_game[1] in v:
					loser = k
			print(f"{winner} beats {loser}")
			continue
		elif score_sheet[clean_game[1]] == clean_game[0]:
			print("You won!")
			points += 6
		else:
			print("It was a draw")
			points += 3
	print(f"Total points: {points}")


def part_two():
	points = 0
	for game in games:
		clean_game = game.strip().split(" ")

		# determine result of the match
		if clean_game[1] == "Y":
			points += (3 + weapon_score[clean_game[0]])
		elif clean_game[1] == "X":
			selection = score_sheet[clean_game[0]]
			points += weapon_score[selection]
		else:
			for k, v in score_sheet.items():
				if clean_game[0] == v:
					selection = k
					break
			points += (6 + weapon_score[selection])
	print(f"Total points: {points}")


part_two()
