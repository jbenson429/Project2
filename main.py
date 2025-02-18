import functions
from functions import main_menu, bubble_menu, merge_menu, quick_menu, tbd_menu, get_choice

if __name__ == '__main__':
    nums100 = functions.generate_nums(100)
    nums1_000 = functions.generate_nums(1000)
    nums10_000 = functions.generate_nums(10_000)
    nums100_000 = functions.generate_nums(100_000)

    print("Welcome to the test suite of selected sorting algorithms!")
    while True:
        main_menu()
        choice = get_choice("Select a sorting algorithm (1-5): ")

        if choice == 1:
            while True:
                bubble_menu()
                bubble_choice = get_choice("Select the case (1-4): ")

                if bubble_choice == 1:
                    while True:
                        # TODO
                        break
                if bubble_choice == 2:
                    while True:
                        # TODO
                        break
                if bubble_choice == 3:
                    while True:
                        # TODO
                        break
                if bubble_choice == 4:
                    break
        elif choice == 2:
            while True:
                merge_menu()
                merge_choice = get_choice("Select the case (1-4): ")

                if merge_choice == 1:
                    while True:
                        # TODO
                        break
                if merge_choice == 2:
                    while True:
                        # TODO
                        break
                if merge_choice == 3:
                    while True:
                        # TODO
                        break
                if merge_choice == 4:
                    break
        elif choice == 3:
            while True:
                quick_menu()
                quick_choice = get_choice("Select the case (1-4): ")

                if quick_choice == 1:
                    while True:
                        # TODO
                        break
                if quick_choice == 2:
                    while True:
                        # TODO
                        break
                if quick_choice == 3:
                    while True:
                        # TODO
                        break
                if quick_choice == 4:
                    break
        elif choice == 4:
            while True:
                tbd_menu()
                tbd_choice = get_choice("Select the case (1-4): ")

                if tbd_choice == 1:
                    while True:
                        # TODO
                        break
                if tbd_choice == 2:
                    while True:
                        # TODO
                        break
                if tbd_choice == 3:
                    while True:
                        # TODO
                        break
                if tbd_choice == 4:
                    break
        elif choice == 5:
            print("Bye!")
            exit()