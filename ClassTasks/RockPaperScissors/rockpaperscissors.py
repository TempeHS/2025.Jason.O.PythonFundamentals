def main():
	player_choice = input("Rock, Paper or Scissors").lower()
	computer_choice = FUNCTION generateRandom
	match player_choice:
		case rock:
			match computer_choice:
		 		case rock:
				    print("draw")
			    case paper:
				    print("lose")
				case scissors:
				    print("win")
		case paper:
			match computer_choice:
		 		case rock:
					print("win")
				case paper:
					print("draw")
				case scissors:
					print("lose")
		case scissors:
			match computer_choice:
		 		case rock:
					print("lose")
				case paper:
					print("lose")
				case scissors:
					print("lose")
			
		DEFAULT	

main()