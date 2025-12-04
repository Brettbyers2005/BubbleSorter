import gradio as gr

# Cisc 121-Project: Bubble Sort
# Author: Brett Byers
# Description:
# This program will ask the user for a list of numbers, then
# will apply bubble sort and show the swaps happening.

def bubble_sort(numbers):
    n = len(numbers)

    # looping over the entire list
    for i in range(n - 1):
        swapped = False

        # check pairs and swap if needed
        for j in range(n - 1 - i):
            print("Comparing " + str(numbers[j]) + " and " + str(numbers[j+1]) + ".....")

            if numbers[j] > numbers[j+1]:
                print("Swapping " + str(numbers[j]) + " and " + str(numbers[j+1]))

                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
                swapped = True

            print("Current list: " + str(numbers) + "\n")

        # if no swaps end up happening then the list is of course already sorted
        if not swapped:
            break

    return numbers


# This version is for gradio: basically like collecting the steps instead of printing them
def bubble_sort_gradsteps(numbers):
    nums = numbers[:]  # copying here so og list is not changed
    steps = []
    n = len(nums)

    for i in range(n - 1):
        swapped = False

        for j in range(n - 1 - i):
            steps.append("Comparing " + str(nums[j]) + " and " + str(nums[j+1]))

            if nums[j] > nums[j+1]:
                steps.append("Swapping " + str(nums[j]) + " and " + str(nums[j+1]))
                nums[j], nums[j+1] = nums[j+1], nums[j]
                swapped = True

            steps.append("The current list: " + str(nums))

        if not swapped:
            break

    steps.append("The final sorted list: " + str(nums))
    return nums, "\n".join(steps)


# Now this section will be console version (after adding gradio)
# Now below will show the main program (most of what the user will see)
def run_console():
    print("Hello! Welcome to the bubble sort visualizer, you are a welcomed guest!!")
    print("Please, for quality, enter your numbers that will be used to make an unsorted list, seperated by spaces ex. (1 2)")

    input_user = input("Your numbers: ")

    # Convert all the inputed strings into list of integers
    try:
        number_list = [int(num) for num in input_user.split()]
    except ValueError:
        print("This is a error: Please enter only whole numbers, no decimals")
        return

    print("\nYour Numbers are currently being sorted\n")
    numbers_sorted = bubble_sort(number_list)

    print("\nAndddd your numbers are all sorted! Here is your sorted list:")
    print(numbers_sorted)


# Now we write the function that gradio will call:
def bubble_ui_sort(user_text):
    try:
        nums = [int(num) for num in user_text.split()]
    except ValueError:
        return "This is a error, please enter whole numbers no decimals", ""

    sorted_list, steps_text = bubble_sort_gradsteps(nums)

    result_text = "Sorted list: " + str(sorted_list)
    return result_text, steps_text


# This next part is what will actually build the visual app
demo = gr.Interface(
    fn=bubble_ui_sort,
    inputs=gr.Textbox(label="Enter numbers separated by spaces (ex. 5 2 8 1)"),
    outputs=[
        gr.Textbox(label="Sorted list"),
        gr.Textbox(label="Step-by-step process")
    ],
    title="Bubble Sort Visualizer",
    description="Simple CISC 121 project that shows how Bubble Sort works."
)


if __name__ == "__main__":
    

   #this forces Gradio to show url in terminal lol (GPT helped me with that one)
    demo.launch()





