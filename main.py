import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.geometry("600x400")
root.title("Raw Dog Food Calculator")

welcome = tk.Label(root, text ="Welcome to the Raw Dog Food Calculator!", font = ('Arial', 16))
welcome.pack(pady = 20)

inputFrame = tk.Frame(root)
inputFrame.columnconfigure(0, weight = 1)
inputFrame.columnconfigure(1, weight = 1)
inputFrame.columnconfigure(2, weight = 1)
inputFrame.columnconfigure(3, weight = 1)

#user input of dog name
nameLabel = tk.Label(inputFrame, text ="What is your dog's name?", font = ('Arial', 12))
nameInput = tk.Entry(inputFrame, font=('Arial', 12))

#user options for metrics
weight = ["Pounds", "Kilograms"]
weightClick = tk.StringVar()
weightClick.set("Pounds")

#user options for goal
goal = ["Gain Weight", "Maintain Current Weight", "Lose Weight"]
goalClick = tk.StringVar()
goalClick.set("Maintain Current Weight")

#user input of weight
weightLabel = tk.Label(inputFrame, text = "What is the dog's current weight?", font = ('Arial', 12))
weightInput = tk.Entry(inputFrame, font=('Arial', 12))
weightDrop = tk.OptionMenu(inputFrame, weightClick,*weight)

#user input of goal
goalLabel = tk.Label(inputFrame, text = "What is the weight goal?", font = ('Arial', 12))
goalInput = tk.OptionMenu(inputFrame, goalClick, *goal)

nameLabel.grid(row=0, column=0, sticky= tk.W + tk.E, padx=20)
nameInput.grid(row=0, column=1, sticky= tk.W + tk.E, padx=20)
weightLabel.grid(row=1, column=0, sticky= tk.W + tk.E, padx=20)
weightInput.grid(row=1, column=1, sticky= tk.W + tk.E, padx=20)
weightDrop.grid(row=1, column=2, sticky= tk.W + tk.E, padx=20)
goalLabel.grid(row=2, column=0, sticky= tk.W + tk.E, padx=20)
goalInput.grid(row=2, column=1, sticky= tk.W + tk.E, padx=20)

inputFrame.pack()
def validateWeight(wt):
    try:
        int(wt)
        return True
    except (ValueError):

        messagebox.showerror("ERROR", "Please enter a valid number for the weight!", icon = 'error')
        return False

#results function
def results():
    validateWt = validateWeight(weightInput.get())

    if validateWt == True:
        userInput = int(weightInput.get())
        calc = tk.Toplevel(root)
        calc.geometry("400x400")
        calc.columnconfigure(0, weight=1)
        calc.columnconfigure(1, weight=1)
        calc.columnconfigure(2, weight=1)
        calc.columnconfigure(3, weight=1)
#populates dog's name
        getName = nameInput.get()
        name = tk.Label(calc, text=str(getName) +"'s Meal Calculations" + " to " + goalClick.get(), font=('Arial', 12))

#metrics for weight

        metricInput = weightClick.get()
        goalChoice = goalClick.get()
        if metricInput == "Pounds":
            muscleMetric = tk.Label(calc, text="ounces", font=('Arial', 12))
            boneMetric = tk.Label(calc, text="ounces", font=('Arial', 12))
            liverMetric = tk.Label(calc, text="ounces", font=('Arial', 12))
            organMetric = tk.Label(calc, text="ounces", font=('Arial', 12))
        else:
            muscleMetric = tk.Label(calc, text="grams", font=('Arial', 12))
            boneMetric = tk.Label(calc,text="grams", font = ('Arial', 12))
            liverMetric = tk.Label(calc, text="grams", font=('Arial', 12))
            organMetric = tk.Label(calc,text="grams", font = ('Arial', 12))


#goal based on metrics
        if goalChoice == "Gain Weight" and metricInput =="Pounds":
            userInput= (userInput*0.03)*16
        elif goalChoice == "Maintain Current Weight"and metricInput =="Pounds":
            userInput= (userInput*0.025)*16
        elif goalChoice == "Lose Weight" and metricInput =="Pounds":
            userInput = (userInput*0.02)*16
        elif goalChoice == "Gain Weight" and metricInput == "Kilograms":
                userInput = (userInput * 0.03) * 1000
        elif goalChoice == "Maintain Current Weight" and metricInput == "Kilograms":
                userInput = (userInput * 0.025) * 1000
        elif goalChoice == "Lose Weight" and metricInput == "Kilograms":
                userInput = (userInput * 0.02) * 1000

#labels for each component
        muscleLabel = tk.Label(calc, text="Muscle Meat: ", font=('Arial', 12))
        boneLabel = tk.Label(calc, text="Bone: ", font=('Arial', 12))
        liverLabel = tk.Label(calc, text="Liver: ", font=('Arial', 12))
        organLabel = tk.Label(calc, text="2nd Secreting Organ*: ", font=('Arial', 12))

        muscleOutput = tk.Label(calc, font=('Arial', 12))
        boneOutput = tk.Label(calc, font=('Arial', 12))
        liverOutput = tk.Label(calc, font=('Arial', 12))
        organOutput = tk.Label(calc, font=('Arial', 12))

#calculations for each component
        musc = "{:.2f}".format(userInput * 0.8)
        bone = "{:.2f}".format(userInput * 0.1)
        liver = "{:.2f}".format(userInput * 0.05)
        organ = "{:.2f}".format(userInput * 0.05)

        muscleOutput.config(text=musc)
        boneOutput.config(text=bone)
        liverOutput.config(text=liver)
        organOutput.config(text=organ)

#grid
        name.grid(row=0, column=0, columnspan=50, sticky=tk.W + tk.E, pady=50)
        muscleLabel.grid(row=1, column=0, sticky=tk.W + tk.E, padx=10)
        muscleOutput.grid(row=1, column=1, sticky=tk.W + tk.E, padx=10)
        muscleMetric.grid(row=1, column=2, sticky=tk.W + tk.E, padx=10)

        boneLabel.grid(row=2, column=0, sticky=tk.W + tk.E, padx=10)
        boneOutput.grid(row=2, column=1, sticky=tk.W + tk.E, padx=10)
        boneMetric.grid(row=2, column=2, sticky=tk.W + tk.E, padx=10)

        liverLabel.grid(row=3, column=0, sticky=tk.W + tk.E, padx=10)
        liverOutput.grid(row=3, column=1, sticky=tk.W + tk.E, padx=10)
        liverMetric.grid(row=3, column=2, sticky=tk.W + tk.E, padx=10)

        organLabel.grid(row=4, column=0, sticky=tk.W + tk.E, padx=10)
        organOutput.grid(row=4, column=1, sticky=tk.W + tk.E, padx=10)
        organMetric.grid(row=4, column=2, sticky=tk.W + tk.E, padx=10)

        attn = tk.Label(calc, text="*Some secreting examples include: \n brain, kidney, spleen, pancreas, and testicles. ",
                        font=('Arial', 12))
        attn.grid(row=5, column=0, columnspan=50, sticky = tk.W + tk.E, pady=50)
    else:
        return

calculateButton = tk.Button(root, text="Calculate!", font =('Arial', 12), command=results)
calculateButton.pack(pady=20)

calcInfo = tk.Label(root, text ="These calculations are daily recommendations.", font=('Arial', 12), fg = 'red')
calcInfo.pack(pady=20)

root.mainloop()


"""label = tk.Label(root, text ="Welcome!", font = ('Arial', 18))
label.pack(pady = 20)

textbox = tk.Text(root, height = 2, font=('Arial', 16))
textbox.pack()

myentry = tk.Entry(root)
myentry.pack()
"""