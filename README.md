# 🧠 Class 10 Biology Quiz App (CBSE + ICSE)

This is an interactive **Biology Quiz Application** developed using **Python Tkinter GUI**. It includes a timer, performance-based feedback, and stores scores in a CSV file with visualization support.

---

## 🚀 Features

- ✅ 15 Multiple Choice Short Answer Questions from Class 10 Biology (CBSE + ICSE)
- ⏱️ Timer starts when quiz begins and ends on submission
- 📈 Score and Time taken are recorded in a `.csv` file (`quiz_results.csv`)
- 🎯 Personalized feedback after the quiz based on your performance
- 📊 Plot bar graph of all past results using Matplotlib
- 💾 Automatically saves quiz results for review or analysis

---

## 🧰 Technologies Used

- `tkinter` – for GUI
- `pandas` – for handling results and saving to CSV
- `matplotlib` – for plotting the quiz score chart
- `time` – for measuring time taken for the quiz
- `os` – for file path checks

---

## 📦 Installation

Make sure you have **Python 3.x** installed.

### Install required libraries:

```bash
pip install pandas matplotlib




🧪 Quiz Rules
Total of 15 questions.

Based on ICSE and CBSE Biology syllabus.

Type short answers (case-insensitive).

Score = Total correct answers out of 15.

Time taken is recorded.

On completion, you get:

Your score

Time taken

A performance compliment!

Option to plot a graph of all scores so far



 Output Files
quiz_results.csv — stores all quiz attempts with:

Name

Score

Time Taken (in seconds)



Sample Graph Output
After completing the quiz, click "Show Score Chart" to view:

A bar graph with each student’s name and their respective scores.

💡 Performance Compliments (Example)
Score	Feedback
13 - 15	🏆 Excellent! Future Biologist!
10 - 12	💪 Good Job! Keep Practicing!
6 - 9	🙂 Nice Try! Improve further.
0 - 5	📘 Revise again. You can do it!


📁 Folder Structure
cpp
Copy code
project-folder/
├── quiz_app.py
├── quiz_results.csv (auto-generated)
├── README.md
