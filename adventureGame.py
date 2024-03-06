name = input("Enter your name: ")
print("Welcome", name, "to the adventure game!")

print("You find yourself on a dirt road that forks ahead. You can see a forest to the left and a mountain to the right.")

answer = input("Which path do you choose? Forest or mountain? ").lower()

if answer == "forest":
    print("You venture into the forest. After walking for a while, you encounter a clearing with a small cottage.")
    cottage_choice = input("Do you explore the cottage or continue deeper into the forest? (explore/continue) ").lower()
    if cottage_choice == "explore":
        print("You enter the cottage and find an old book with a map inside. The map leads you to a hidden treasure.")
    elif cottage_choice == "continue":
        print("You decide to continue deeper into the forest. You stumble upon a magical pond.")
        pond_choice = input("Do you drink from the pond or keep moving? (drink/move) ").lower()
        if pond_choice == "drink":
            print("The water grants you enhanced strength. You continue your journey feeling invigorated.")
        elif pond_choice == "move":
            print("You decide not to risk it and keep moving. You find a hidden path that leads to a mysterious cave.")
            cave_choice = input("Do you enter the cave or return to the fork in the road? (enter/return) ").lower()
            if cave_choice == "enter":
                print("You enter the cave and find a sleeping dragon. You manage to sneak past it and find a treasure.")
            elif cave_choice == "return":
                print("You return to the fork in the road and choose another path.")
            else:
                print("Not a valid option. You lose.")
        else:
            print("Not a valid option. You lose.")
    else:
        print("Not a valid option. You lose.")
elif answer == "mountain":
    print("You decide to climb the mountain. As you ascend, the air becomes thinner and the climb more treacherous.")
    mountain_choice = input("Do you continue climbing or turn back? (continue/back) ").lower()
    if mountain_choice == "continue":
        print("You press on, determined to reach the summit. At the top, you find a nest with a dragon egg.")
        egg_choice = input("Do you take the egg or leave it? (take/leave) ").lower()
        if egg_choice == "take":
            print("You carefully take the egg and make your way down the mountain. The dragon mother finds you and rewards you for your bravery.")
        elif egg_choice == "leave":
            print("You decide to leave the egg undisturbed. As you descend the mountain, you encounter a group of adventurers who offer to join forces.")
        else:
            print("Not a valid option. You lose.")
    elif mountain_choice == "back":
        print("You decide to turn back, realizing the climb is too dangerous. You return to the fork in the road.")
    else:
        print("Not a valid option. You lose.")
else:
    print("Not a valid option. You lose.")
