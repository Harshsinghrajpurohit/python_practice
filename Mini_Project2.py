'''-----------------------------------------------------"Timed Math Challenge"--------------------------------------------------------'''

import random
import time

# ==================== HIGH SCORE ====================

high_scores = {
    "Easy"   : {"name": None, "score": 0},
    "Medium" : {"name": None, "score": 0},
    "Hard"   : {"name": None, "score": 0},
}

# ==================== PLAYER ====================

class Player:
    def __init__(self):
        self.name = input("Enter Your Name: ").strip()
        print("\n  Welcome, {}! Let's test your math skills!".format(self.name))
        time.sleep(1)

# ==================== QUESTION GENERATOR ====================

class Question:
    def __init__(self, difficulty):
        self.difficulty = difficulty
        self.generate()

    def generate(self):
        if self.difficulty == "Easy":
            # Simple 2-step: a + b - c  or  a - b + c  (small numbers)
            a   = random.randint(1, 15)
            b   = random.randint(1, 10)
            c   = random.randint(1, 10)
            op1 = random.choice(['+', '-'])
            op2 = random.choice(['+', '-'])
            self.text   = "  {} {} {} {} {} = ?".format(a, op1, b, op2, c)
            self.answer = eval("{} {} {} {} {}".format(a, op1, b, op2, c))

        elif self.difficulty == "Medium":
            # 2-step with multiplication: a + b * c  or  a * b - c
            a = random.randint(1, 10)
            b = random.randint(1, 10)
            c = random.randint(1, 10)
            pattern = random.choice([
                "{} + {} * {}".format(a, b, c),
                "{} * {} - {}".format(a, b, c),
                "{} * {} + {}".format(a, b, c),
                "{} - {} * {}".format(a, b, c),
            ])
            self.text   = "  {} = ?  (follow BODMAS)".format(pattern)
            self.answer = eval(pattern)

        else:  # Hard
            # 3-step with mixed ops and brackets
            a = random.randint(2, 15)
            b = random.randint(2, 10)
            c = random.randint(2, 10)
            d = random.randint(1, 10)
            pattern = random.choice([
                "({} + {}) * {} - {}".format(a, b, c, d),
                "{} * ({} + {}) - {}".format(a, b, c, d),
                "({} - {}) * {} + {}".format(a, b, c, d),
                "{} * {} + {} * {}".format(a, b, c, d),
                "({} + {}) * ({} - {})".format(a, b, c, d) if c > d else "({} + {}) * {} + {}".format(a, b, c, d),
                "{} * {} - ({} + {})".format(a, b, c, d),
            ])
            self.text   = "  {} = ?".format(pattern)
            self.answer = eval(pattern)

# ==================== GAME ====================

class Game:
    SETTINGS = {
        "Easy"   : {"questions": 10, "time_per_q": 20, "points": 10},
        "Medium" : {"questions": 10, "time_per_q": 15, "points": 20},
        "Hard"   : {"questions": 10, "time_per_q": 20, "points": 30},
    }

    def __init__(self, player, difficulty):
        self.player     = player
        self.difficulty = difficulty
        self.settings   = self.SETTINGS[difficulty]
        self.score      = 0
        self.correct    = 0
        self.wrong      = 0
        self.skipped    = 0

    def play(self):
        total_q    = self.settings["questions"]
        time_limit = self.settings["time_per_q"]
        points     = self.settings["points"]

        print("\n  Difficulty : {}".format(self.difficulty))
        print("  Questions  : {}".format(total_q))
        print("  Time/Q     : {} seconds".format(time_limit))
        print("  Points/Q   : {}".format(points))
        print("\n  Game starts in...")
        for i in range(3, 0, -1):
            print("  {}...".format(i))
            time.sleep(1)
        print("  GO!\n")

        for q_num in range(1, total_q + 1):
            q = Question(self.difficulty)
            print("  Q{}/{}  |  Score: {}".format(q_num, total_q, self.score))
            print("  {}".format(q.text))
            print("  (You have {} seconds | type 's' to skip)".format(time_limit))

            start = time.time()
            try:
                user_input = input("  Your Answer: ").strip().lower()
            except KeyboardInterrupt:
                print("\n  Game interrupted!")
                break

            elapsed = time.time() - start

            if elapsed > time_limit:
                print("  Time's up! Correct answer was {}\n".format(q.answer))
                self.skipped += 1
            elif user_input == 's':
                print("  Skipped! Correct answer was {}\n".format(q.answer))
                self.skipped += 1
            else:
                try:
                    if int(user_input) == q.answer:
                        time_bonus = max(0, int((time_limit - elapsed) * 2))
                        earned     = points + time_bonus
                        self.score   += earned
                        self.correct += 1
                        print("  Correct! +{} points (includes time bonus: +{})\n".format(earned, time_bonus))
                    else:
                        print("  Wrong! Correct answer was {}\n".format(q.answer))
                        self.wrong += 1
                except ValueError:
                    print("  Invalid input! Correct answer was {}\n".format(q.answer))
                    self.wrong += 1

            time.sleep(0.5)

        self.show_result()

    def show_result(self):
        total_q = self.settings["questions"]
        print("\n" + "=" * 40)
        print("          GAME OVER - RESULTS")
        print("=" * 40)
        print("  Player     : {}".format(self.player.name))
        print("  Difficulty : {}".format(self.difficulty))
        print("-" * 40)
        print("  Correct    : {}/{}".format(self.correct, total_q))
        print("  Wrong      : {}".format(self.wrong))
        print("  Skipped    : {}".format(self.skipped))
        print("  Final Score: {}".format(self.score))
        print("=" * 40)

        # Performance message
        accuracy = (self.correct / total_q) * 100
        if accuracy == 100:
            print("  PERFECT SCORE! Outstanding!")
        elif accuracy >= 80:
            print("  Excellent work! Keep it up!")
        elif accuracy >= 60:
            print("  Good job! Room to improve!")
        elif accuracy >= 40:
            print("  Keep practicing!")
        else:
            print("  Don't give up! Try again!")

        # High score check
        current_best = high_scores[self.difficulty]
        if self.score > current_best["score"]:
            print("\n  NEW HIGH SCORE for {}!".format(self.difficulty))
            high_scores[self.difficulty]["name"]  = self.player.name
            high_scores[self.difficulty]["score"] = self.score
        else:
            if current_best["name"]:
                print("\n  Current High Score ({}): {} by {}".format(
                    self.difficulty, current_best["score"], current_best["name"]))

        print("=" * 40)
        time.sleep(2)

# ==================== HIGH SCORE DISPLAY ====================

def show_leaderboard():
    print("\n" + "=" * 40)
    print("          HIGH SCORES")
    print("=" * 40)
    for level in ["Easy", "Medium", "Hard"]:
        entry = high_scores[level]
        if entry["name"]:
            print("  {:<8}: {:>5} pts  - {}".format(level, entry["score"], entry["name"]))
        else:
            print("  {:<8}: No record yet".format(level))
    print("=" * 40)
    time.sleep(2)

# ==================== DIFFICULTY MENU ====================

def choose_difficulty():
    print("\n  Choose Difficulty:")
    print("  1. Easy   (a+b-c style      | 20 sec/Q | 10 pts)")
    print("  2. Medium (a+b*c BODMAS     | 15 sec/Q | 20 pts)")
    print("  3. Hard   ((a+b)*c-d style  | 20 sec/Q | 30 pts)")
    while True:
        try:
            choice = int(input("  Enter choice (1/2/3): "))
            if choice == 1:
                return "Easy"
            elif choice == 2:
                return "Medium"
            elif choice == 3:
                return "Hard"
            else:
                print("  Please enter 1, 2, or 3.")
        except ValueError:
            print("  Invalid input!")

# ==================== MAIN ====================

print("=" * 40)
print("       TIMED MATH CHALLENGE")
print("=" * 40)
time.sleep(1)

player = Player()

while True:
    print("\n========= MAIN MENU =========")
    print("  1. Start Game")
    print("  2. View High Scores")
    print("  3. Exit")
    print("==============================")

    try:
        choice = int(input("  Enter choice: "))
    except ValueError:
        print("  Invalid input!")
        continue

    if choice == 1:
        difficulty = choose_difficulty()
        game = Game(player, difficulty)
        game.play()
    elif choice == 2:
        show_leaderboard()
    elif choice == 3:
        print("\n  Thanks for playing, {}! Goodbye!".format(player.name))
        time.sleep(2)
        break
    else:
        print("  Invalid choice! Enter 1, 2, or 3.")