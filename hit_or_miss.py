score = 100
action = 0
while action < 4:
	shot = input("shot 1:")
	if  shot == "hit":
		score+=10
	elif shot == "miss":
		score-=20
	action+=1
print(score)
