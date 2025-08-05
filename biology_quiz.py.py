import tkinter as tk
from tkinter import messagebox
import time
import pandas as pd
import matplotlib.pyplot as plt
import os

# Questions and answers (ICSE + CBSE mix)
questions = [
    ("What is the functional unit of the kidney?", "nephron"),
    ("Name the hormone secreted by the pancreas that controls blood sugar.", "insulin"),
    ("What is the process by which green plants make their food?", "photosynthesis"),
    ("Which part of the brain controls balance and coordination?", "cerebellum"),
    ("Name the largest gland in the human body.", "liver"),
    ("Which blood cells help in clotting of blood?", "platelets"),
    ("Which is the voice box of human beings?", "larynx"),
    ("What pigment gives colour to the skin?", "melanin"),
    ("Name the organ where fertilization occurs in human females.", "fallopian tube"),
    ("Which vitamin is synthesized in the skin in presence of sunlight?", "vitamin d"),
    ("Which organelle is known as the powerhouse of the cell?", "mitochondria"),
    ("What is the fluid part of blood called?", "plasma"),
    ("What connects muscles to bones?", "tendons"),
    ("Name the enzyme present in saliva.", "ptyalin"),
    ("What type of reproduction involves only one parent?", "asexual")
]

class QuizApp:
    def __init__(self, master):
        self.master = master
        master.title("Class 10 Biology Quiz")
        master.geometry("500x400")

        self.score = 0
        self.qn = 0
        self.start_time = 0

        self.name_label = tk.Label(master, text="Enter your name:")
        self.name_label.pack(pady=10)

        self.name_entry = tk.Entry(master)
        self.name_entry.pack()

        self.rules = tk.Label(master, text="""
Rules:
- Total 15 questions based on ICSE + CBSE Class 10 Biology.
- Each correct answer gives 1 point.
- Type short answers (case-insensitive).
- Score and time will be recorded.
        """, justify="left")
        self.rules.pack(pady=10)

        self.start_button = tk.Button(master, text="Start Quiz", command=self.start_quiz)
        self.start_button.pack()

    def start_quiz(self):
        self.username = self.name_entry.get().strip()
        if not self.username:
            messagebox.showwarning("Input Error", "Please enter your name.")
            return

        self.rules.pack_forget()
        self.name_label.pack_forget()
        self.name_entry.pack_forget()
        self.start_button.pack_forget()

        self.start_time = time.time()
        self.show_question()

    def show_question(self):
        if self.qn < len(questions):
            q, _ = questions[self.qn]
            self.question_label = tk.Label(self.master, text=f"Q{self.qn + 1}. {q}")
            self.question_label.pack(pady=20)

            self.answer_entry = tk.Entry(self.master)
            self.answer_entry.pack()

            self.submit_button = tk.Button(self.master, text="Submit", command=self.check_answer)
            self.submit_button.pack(pady=10)
        else:
            self.end_quiz()

    def check_answer(self):
        user_ans = self.answer_entry.get().strip().lower()
        correct_ans = questions[self.qn][1].lower()

        if user_ans == correct_ans:
            self.score += 1
            messagebox.showinfo("Result", "Correct!")
        else:
            messagebox.showinfo("Result", f"Not correct. Correct answer is: {correct_ans.capitalize()}")

        self.qn += 1
        self.question_label.destroy()
        self.answer_entry.destroy()
        self.submit_button.destroy()
        self.show_question()

    def end_quiz(self):
        end_time = time.time()
        total_time = round(end_time - self.start_time, 2)

        messagebox.showinfo("Quiz Completed", f"Your Score: {self.score}/15\nTime Taken: {total_time} seconds")
        self.save_results(self.username, self.score, total_time)
        self.show_graph_button()

    def save_results(self, name, score, time_taken):
        result_data = pd.DataFrame({"Name": [name], "Score": [score], "Time": [time_taken]})
        file_exists = os.path.isfile("quiz_results.csv")
        result_data.to_csv("quiz_results.csv", mode="a", index=False, header=not file_exists)

    def show_graph_button(self):
        self.graph_button = tk.Button(self.master, text="Show Score Chart", command=self.plot_scores)
        self.graph_button.pack(pady=20)

    def plot_scores(self):
        if os.path.exists("quiz_results.csv"):
            df = pd.read_csv("quiz_results.csv")
            plt.figure(figsize=(10, 5))
            plt.bar(df["Name"], df["Score"], color="skyblue")
            plt.xlabel("Student Name")
            plt.ylabel("Score")
            plt.title("Biology Quiz Scores")
            plt.xticks(rotation=45)
            plt.tight_layout()
            plt.show()
        else:
            messagebox.showinfo("No Data", "No quiz results found to display.")


if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()
