import tkinter as tk
from tkinter import messagebox
import time
from datetime import datetime
import random


class TypingSpeedApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Typing Speed Assessor")
        self.root.geometry("1000x800")
        self.root.config(bg="#f0f0f0")

        # Comprehensive word list for random generation
        self.word_list = [
            "about", "after", "again", "all", "also", "an", "and", "another", "any", "are",
            "as", "at", "be", "because", "been", "before", "being", "both", "but", "by",
            "came", "can", "come", "could", "did", "do", "does", "done", "down", "each",
            "early", "end", "even", "ever", "every", "fact", "feel", "few", "find", "first",
            "for", "found", "from", "full", "gave", "get", "give", "go", "good", "got",
            "great", "group", "had", "has", "have", "having", "he", "head", "help", "her",
            "here", "herself", "high", "him", "himself", "his", "how", "if", "in", "into",
            "is", "it", "its", "itself", "just", "keep", "kind", "know", "large", "last",
            "later", "left", "less", "life", "like", "line", "little", "live", "long", "look",
            "made", "make", "man", "many", "me", "mean", "might", "more", "most", "much",
            "must", "my", "myself", "name", "never", "new", "next", "no", "not", "now",
            "number", "of", "off", "often", "on", "once", "only", "or", "other", "our",
            "out", "over", "own", "part", "people", "place", "play", "point", "put", "read",
            "right", "said", "same", "say", "see", "seem", "seen", "set", "several", "shall",
            "she", "should", "show", "side", "since", "so", "some", "something", "soon", "sort",
            "such", "take", "tell", "than", "thank", "that", "the", "their", "them", "then",
            "there", "these", "they", "thing", "think", "this", "those", "thought", "three", "through",
            "time", "to", "told", "took", "tried", "tries", "true", "two", "under", "understand",
            "up", "us", "use", "used", "very", "want", "was", "way", "we", "well",
            "went", "were", "what", "when", "where", "which", "while", "who", "whom", "why",
            "will", "with", "without", "work", "would", "year", "years", "you", "young", "your",
            "ability", "able", "absence", "absolute", "accept", "access", "accident", "account", "achieve", "acid",
            "acquire", "action", "active", "activity", "actual", "adapt", "add", "addition", "address", "adequate",
            "adjust", "admit", "adopt", "advance", "advent", "advice", "advise", "affair", "affect", "afford",
            "afraid", "afternoon", "agent", "ago", "agree", "agreement", "agriculture", "ahead", "aid", "aim",
            "aircraft", "airline", "airport", "aisle", "alarm", "album", "alcohol", "alert", "alien", "align",
            "alike", "alive", "allow", "allowance", "almost", "alone", "along", "alongside", "aloud", "already",
            "alter", "alternative", "although", "altitude", "altogether", "always", "amateur", "amazing", "ambassador",
            "amber",
            "ambition", "ambulance", "amend", "amendment", "america", "american", "among", "amongst", "amount", "ample",
            "amuse", "amusement", "ancient", "angel", "anger", "angle", "angry", "animal", "ankle", "announce",
            "annoy", "annual", "annul", "anode", "anomaly", "anonymous", "answer", "ant", "anticipate", "antique",
            "anxiety", "anxious", "anybody", "anyone", "anything", "anyway", "anywhere", "apart", "apartment",
            "apology",
            "apostle", "appall", "apparatus", "apparel", "apparent", "appeal", "appear", "appearance", "appease",
            "append",
            "appendix", "appetite", "applaud", "applause", "apple", "appliance", "applicable", "applicant",
            "application", "apply",
            "appoint", "appointment", "appraisal", "appraise", "appreciate", "appreciation", "apprehend",
            "apprehension", "apprentice", "approach",
            "appropriate", "approval", "approve", "approximate", "apricot", "april", "apron", "apt", "aptitude",
            "aquatic",
            "aqueduct", "arab", "arabic", "arbitrary", "arbor", "arcade", "arch", "archaic", "archbishop", "archer",
            "archive", "arctic", "ardent", "ardor", "arduous", "area", "arena", "argentina", "argentinian", "argue",
            "argument", "arise", "aristocrat", "arithmetic", "arizona", "ark", "arkansas", "arm", "armada", "armor",
            "armory", "arms", "army", "aroma", "around", "arouse", "arrange", "arrangement", "array", "arrest",
            "arrival", "arrive", "arrogance", "arrogant", "arrow", "arsenal", "art", "artery", "artful", "article",
            "artifice", "artificial", "artillery", "artist", "artistic", "artless", "arts", "artwork", "ash", "ashamed",
            "ashen", "ashes", "asia", "asian", "aside", "ask", "asleep", "aspect", "aspiration", "aspire",
            "aspiring", "ass", "assail", "assassin", "assassinate", "assassination", "assault", "assay", "assemble",
            "assembly",
            "assent", "assert", "assertion", "assess", "assessment", "asset", "assets", "assiduous", "assign",
            "assignment",
            "assimilate", "assimilation", "assist", "assistance", "assistant", "associate", "association", "assort",
            "assorted", "assortment",
            "assuage", "assume", "assumption", "assurance", "assure", "astonish", "astonishment", "astound", "astray",
            "astride",
            "astrology", "astronaut", "astronomer", "astronomy", "astute", "asylum", "at", "ate", "atheism", "atheist",
            "athlete", "athletic", "athletics", "atlantic", "atlas", "atmosphere", "atom", "atomic", "atone",
            "atonement",
            "atrocious", "atrocity", "attach", "attachment", "attack", "attain", "attainment", "attempt", "attend",
            "attendance",
            "attendant", "attention", "attentive", "attest", "attic", "attire", "attitude", "attorney", "attract",
            "attraction",
            "attractive", "attributable", "attribute", "attribution", "attrition", "attune", "auburn", "auction",
            "audacious", "audacity",
            "audible", "audience", "audio", "audit", "audition", "auditor", "auditorium", "auditory", "august", "aunt",
            "auspices", "auspicious", "austere", "austerity", "australia", "australian", "austria", "austrian",
            "authentic", "authenticate",
            "authentication", "authenticity", "author", "authorisation", "authorise", "authorised", "authorities",
            "authority", "authorization", "authorize",
            "authorized", "authorship", "autism", "autistic", "auto", "autobiography", "autocracy", "autocrat",
            "autocratic", "autograph",
            "automate", "automated", "automatic", "automatically", "automation", "automaton", "automobile",
            "autonomous", "autonomy", "autopsy",
            "autumn", "auxiliary", "avail", "availability", "available", "avalanche", "avarice", "avaricious", "avast",
            "avenue",
            "aver", "average", "averse", "aversion", "avert", "aviary", "aviation", "aviator", "avid", "avidly",
            "avocado", "avocation", "avoid", "avoidable", "avoidance", "avouch", "avow", "avowal", "avowed", "await",
            "awake", "awaken", "awakening", "award", "aware", "awareness", "awash", "away", "awe", "awed",
            "awesome", "awestricken", "awestruck", "awful", "awfully", "awfulness", "awhile", "awkward", "awkwardness",
            "awl",
            "awning", "awoke", "awoken", "awry", "axe", "axiom", "axiomatic", "axis", "axle", "axman",
            "axon", "aye", "azure", "baby", "back", "bacon", "bad", "bag", "ball", "band"
        ]

        self.current_text = ""
        self.word_list_full = []
        self.start_time = None
        self.test_active = False
        self.words_typed = 0
        self.current_word_index = 0
        self.time_remaining = 60
        self.test_duration = 60

        self.setup_ui()

    def generate_random_text(self, num_words=1000):
        """Generate random text from word list"""
        self.word_list_full = [random.choice(self.word_list) for _ in range(num_words)]
        return " ".join(self.word_list_full)

    def setup_ui(self):
        # Top result display frame
        result_frame = tk.Frame(self.root, bg="white", relief="solid", borderwidth=2)
        result_frame.pack(padx=20, pady=15, fill="x")

        self.wpm_result_display = tk.Label(result_frame, text="WPM: 0.00",
                                           font=("Arial", 32, "bold"), bg="white", fg="#0066cc")
        self.wpm_result_display.pack(pady=15)

        # Title
        title = tk.Label(self.root, text="Typing Speed Assessor",
                         font=("Arial", 24, "bold"), bg="#f0f0f0", fg="#333")
        title.pack(pady=15)

        # Instructions
        instructions = tk.Label(self.root,
                                text="Type the words shown. The current word is highlighted in large text. Green = correct, Red = incorrect. You have 60 seconds!",
                                font=("Arial", 11), bg="#f0f0f0", fg="#666")
        instructions.pack(pady=10)

        # Current word display with 5 words visible
        current_label = tk.Label(self.root, text="Words to Type:",
                                 font=("Arial", 12, "bold"), bg="#f0f0f0")
        current_label.pack(anchor="w", padx=20, pady=(15, 5))

        self.current_word_frame = tk.Frame(self.root, bg="white", relief="solid", borderwidth=2, height=180)
        self.current_word_frame.pack(padx=20, pady=(0, 15), fill="both", expand=False)
        self.current_word_frame.pack_propagate(False)

        # Container for word labels
        self.words_container = tk.Frame(self.current_word_frame, bg="white")
        self.words_container.pack(pady=20, padx=20, fill="both", expand=True)

        # Create 5 word label slots
        self.word_labels = []
        for i in range(5):
            word_label = tk.Label(self.words_container,
                                  text="",
                                  font=("Arial", 28, "bold"), bg="white", fg="#333")
            word_label.pack(side="left", expand=True, fill="both", padx=5)
            self.word_labels.append(word_label)

        # Progress and Timer display
        progress_frame = tk.Frame(self.root, bg="#f0f0f0")
        progress_frame.pack(pady=10, fill="x")

        self.progress_display = tk.Label(progress_frame, text="Words: 0/1000",
                                         font=("Arial", 11), bg="#f0f0f0", fg="#666")
        self.progress_display.pack(side="left", padx=20)

        self.timer_label = tk.Label(progress_frame, text="Time: 60s",
                                    font=("Arial", 12, "bold"), bg="#f0f0f0", fg="#DC143C")
        self.timer_label.pack(side="right", padx=20)

        # Input text area
        input_label = tk.Label(self.root, text="Type Here:",
                               font=("Arial", 12, "bold"), bg="#f0f0f0")
        input_label.pack(anchor="w", padx=20, pady=(10, 5))

        self.input_text = tk.Text(self.root, height=2, width=100,
                                  font=("Arial", 12), relief="solid", borderwidth=1)
        self.input_text.pack(padx=20, pady=(0, 15), fill="x")
        self.input_text.config(state="disabled")

        # Buttons
        button_frame = tk.Frame(self.root, bg="#f0f0f0")
        button_frame.pack(pady=15)

        self.start_btn = tk.Button(button_frame, text="Start", command=self.start_test,
                                   font=("Arial", 12, "bold"), bg="#4CAF50", fg="white",
                                   padx=20, pady=10, relief="raised")
        self.start_btn.pack(side="left", padx=10)

        self.reset_btn = tk.Button(button_frame, text="Reset", command=self.reset_test,
                                   font=("Arial", 12, "bold"), bg="#ff9800", fg="white",
                                   padx=20, pady=10, relief="raised")
        self.reset_btn.pack(side="left", padx=10)

    def update_words_display(self):
        """Update the 5 words display"""
        if self.current_word_index < len(self.word_list_full):
            # Get current word and next 4 words
            for i in range(5):
                label = self.word_labels[i]
                if self.current_word_index + i < len(self.word_list_full):
                    word = self.word_list_full[self.current_word_index + i]

                    # Current word (index 0) is larger and highlighted in blue
                    if i == 0:
                        label.config(text=word, font=("Arial", 40, "bold"), fg="#0066cc")
                    else:
                        label.config(text=word, font=("Arial", 20), fg="#999")
                else:
                    label.config(text="")

    def start_test(self):
        if self.test_active:
            messagebox.showwarning("Active Test", "A test is already in progress. Reset first.")
            return

        # Generate random 1000-word text
        self.generate_random_text(1000)
        self.current_word_index = 0
        self.time_remaining = self.test_duration

        # Display first 5 words
        self.update_words_display()

        # Enable input
        self.input_text.config(state="normal")
        self.input_text.delete(1.0, "end")
        self.input_text.focus()
        self.input_text.bind("<KeyRelease>", self.on_key_release)

        # Start timer
        self.start_time = time.time()
        self.test_active = True
        self.start_btn.config(state="disabled")

        # Start updating timer and WPM
        self.update_timer()

    def on_key_release(self, event):
        """Handle input and validate words"""
        user_input = self.input_text.get(1.0, "end-1c").strip()

        # Check if user completed a word (space pressed)
        if event.keysym == "space":
            if self.current_word_index < len(self.word_list_full) and self.test_active:
                current_word = self.word_list_full[self.current_word_index]

                # Check if typed word matches (case-insensitive)
                if user_input.lower() == current_word.lower():
                    # Correct word - show in green
                    self.word_labels[0].config(fg="#228B22")
                else:
                    # Incorrect word - show in red
                    self.word_labels[0].config(fg="#DC143C")

                # Move to next word after a short delay
                self.root.after(400, self.move_to_next_word)

    def move_to_next_word(self):
        """Move to the next word in the list"""
        if self.test_active:
            self.current_word_index += 1
            self.input_text.delete(1.0, "end")
            self.progress_display.config(text=f"Words: {self.current_word_index}/{len(self.word_list_full)}")
            self.update_words_display()

    def update_timer(self):
        if self.test_active:
            elapsed_time = time.time() - self.start_time
            self.time_remaining = self.test_duration - int(elapsed_time)

            # Update timer display
            if self.time_remaining >= 0:
                self.timer_label.config(text=f"Time: {self.time_remaining}s")

                # Calculate and update live WPM
                if elapsed_time > 0:
                    wpm = (self.current_word_index / elapsed_time) * 60
                    self.wpm_result_display.config(text=f"WPM: {wpm:.2f}")

                self.root.after(1000, self.update_timer)
            else:
                # Time's up
                self.test_active = False
                self.submit_test()

    def submit_test(self):
        if not self.test_active:
            self.test_active = False
            self.input_text.config(state="disabled")
            try:
                self.input_text.unbind("<KeyRelease>")
            except:
                pass

            elapsed_time = self.test_duration
            words_completed = self.current_word_index
            wpm = (words_completed / elapsed_time) * 60

            # Update final WPM display
            self.wpm_result_display.config(text=f"WPM: {wpm:.2f}", fg="#228B22")

            # Show results
            result_message = f"""
Typing Test Complete!

Time: {elapsed_time} seconds
Words Completed: {words_completed}/{len(self.word_list_full)}
Words Per Minute (WPM): {wpm:.2f}

{'Excellent! Outstanding performance!' if wpm > 60 else 'Great job! Keep practicing!' if wpm > 40 else 'Good effort! Practice makes perfect!' if wpm > 20 else 'Keep practicing to increase your speed!'}
            """

            messagebox.showinfo("Test Results", result_message)

            # Reset for next test
            self.reset_test()

    def reset_test(self):
        self.test_active = False
        self.current_word_index = 0
        self.start_time = None
        self.time_remaining = self.test_duration

        self.input_text.config(state="disabled")
        self.input_text.delete(1.0, "end")
        try:
            self.input_text.unbind("<KeyRelease>")
        except:
            pass

        self.start_btn.config(state="normal")

        self.timer_label.config(text="Time: 60s", fg="#DC143C")
        self.wpm_result_display.config(text="WPM: 0.00", fg="#0066cc")

        for label in self.word_labels:
            label.config(text="")

        self.progress_display.config(text="Words: 0/1000")


if __name__ == "__main__":
    root = tk.Tk()
    app = TypingSpeedApp(root)
    root.mainloop()