

with open("input.txt", mode="r", encoding="utf-8-sig") as input_file:
	elf_calories_raw = input_file.read().split("\n\n")

loaded_elf = 0
all_elves_list = []
for cal_str in elf_calories_raw:
	cal_list = cal_str.strip().split("\n")

	total_cal = 0
	for elf_cal in [int(c) for c in cal_list]:
		total_cal += elf_cal
	all_elves_list.append(total_cal)

	if total_cal > loaded_elf:
		loaded_elf = total_cal
		print(f"New calorie max with: {total_cal}")


print(f"Location of max: {all_elves_list.index(max(all_elves_list))}")
print(f"Max carried by an elf: {max(all_elves_list)}")
