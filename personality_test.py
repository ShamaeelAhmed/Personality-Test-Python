import tkinter as tk
from tkinter import font as tkfont
import math

QUESTIONS = [
    ("I have a rich vocabulary and enjoy playing with words.", "O", 1),
    ("I have a vivid imagination.", "O", 1),
    ("I am not interested in abstract ideas.", "O", -1),
    ("I enjoy thinking about complex problems.", "O", 1),
    ("I prefer routine over new experiences.", "O", -1),
    ("I am always prepared before starting a task.", "C", 1),
    ("I pay attention to details.", "C", 1),
    ("I often leave a mess in my room.", "C", -1),
    ("I follow a schedule and stick to it.", "C", 1),
    ("I find it difficult to get down to work.", "C", -1),
    ("I am the life of the party.", "E", 1),
    ("I feel comfortable around people.", "E", 1),
    ("I don't talk a lot in group settings.", "E", -1),
    ("I enjoy meeting new people.", "E", 1),
    ("I prefer spending evenings alone rather than at social events.", "E", -1),
    ("I sympathize with others' feelings.", "A", 1),
    ("I am interested in people's problems and try to help.", "A", 1),
    ("I sometimes insult or belittle others.", "A", -1),
    ("I make people feel at ease.", "A", 1),
    ("I am not really interested in others' feelings.", "A", -1),
    ("I get stressed out easily.", "N", 1),
    ("I worry about things a lot.", "N", 1),
    ("I am relaxed most of the time.", "N", -1),
    ("I get upset easily.", "N", 1),
    ("I rarely feel sad or depressed.", "N", -1),
]

TRAIT_NAMES = {
    "O": "Openness",
    "C": "Conscientiousness",
    "E": "Extraversion",
    "A": "Agreeableness",
    "N": "Neuroticism",
}

TRAIT_COLORS = {
    "O": "#7C6EFA",
    "C": "#3ABFBF",
    "E": "#F4A338",
    "A": "#5DBE7E",
    "N": "#E8607A",
}

PROFILES = {
    "O": {
        "high": {
            "label": "Creative & Curious",
            "desc": "You are imaginative, intellectually curious, and open to new experiences. You love art, philosophy, and exploring unconventional ideas.",
            "strengths": ["Creative thinking", "Adaptability", "Love of learning", "Appreciation for novelty"],
            "weaknesses": ["Easily distracted by too many ideas", "Can seem impractical", "Struggles with repetition"],
        },
        "low": {
            "label": "Practical & Traditional",
            "desc": "You are grounded and prefer the familiar. You value convention and find comfort in established routines.",
            "strengths": ["Reliability", "Pragmatism", "Strong practical skills", "Consistency"],
            "weaknesses": ["Resistance to change", "May miss creative solutions", "Less comfortable with ambiguity"],
        },
    },
    "C": {
        "high": {
            "label": "Organized & Disciplined",
            "desc": "You are self-disciplined, goal-oriented, and dependable. You plan ahead, meet deadlines, and take your responsibilities seriously.",
            "strengths": ["Strong work ethic", "Time management", "Reliability", "Attention to detail"],
            "weaknesses": ["Can be overly rigid", "May struggle with spontaneity", "Risk of workaholism"],
        },
        "low": {
            "label": "Flexible & Spontaneous",
            "desc": "You are easygoing and live in the moment. You adapt quickly but may find it hard to stick to long-term plans.",
            "strengths": ["Flexibility", "Creativity under pressure", "Present-moment awareness"],
            "weaknesses": ["Procrastination", "Disorganization", "Difficulty meeting deadlines"],
        },
    },
    "E": {
        "high": {
            "label": "Outgoing & Energetic",
            "desc": "You draw energy from social interactions. You are talkative, assertive, and enthusiastic — a natural in group settings.",
            "strengths": ["Strong social skills", "Leadership potential", "Positive energy", "Networking ability"],
            "weaknesses": ["Can dominate conversations", "Needs external stimulation", "Can be impulsive"],
        },
        "low": {
            "label": "Reflective & Reserved",
            "desc": "You are introverted and prefer depth over breadth in relationships. You recharge through solitude and careful thought.",
            "strengths": ["Deep focus", "Thoughtful communication", "Strong one-on-one bonds", "Independence"],
            "weaknesses": ["May seem aloof", "Social fatigue in large groups", "Can miss networking opportunities"],
        },
    },
    "A": {
        "high": {
            "label": "Warm & Cooperative",
            "desc": "You are compassionate and eager to help others. You value harmony and are often the peacemaker in conflicts.",
            "strengths": ["Empathy", "Teamwork", "Conflict resolution", "Trustworthiness"],
            "weaknesses": ["Difficulty saying no", "May neglect own needs", "Can be taken advantage of"],
        },
        "low": {
            "label": "Independent & Direct",
            "desc": "You are straightforward and prioritize logic over feelings. You're not afraid to challenge others when you disagree.",
            "strengths": ["Directness", "Competitive drive", "Critical thinking", "Self-reliance"],
            "weaknesses": ["Can come across as cold or blunt", "May clash in team settings", "Risk of conflict"],
        },
    },
    "N": {
        "high": {
            "label": "Sensitive & Emotionally Aware",
            "desc": "You experience emotions intensely and are highly aware of your inner world. You may be prone to stress or mood swings.",
            "strengths": ["Emotional depth", "Empathy", "Self-awareness", "Motivating sensitivity"],
            "weaknesses": ["Prone to anxiety", "Mood fluctuations", "Difficulty under pressure"],
        },
        "low": {
            "label": "Calm & Emotionally Stable",
            "desc": "You are emotionally resilient and remain steady under pressure. Setbacks rarely throw you off course.",
            "strengths": ["Stress tolerance", "Consistency", "Clear thinking under pressure", "Emotional stability"],
            "weaknesses": ["May underestimate emotional situations", "Can seem unsympathetic"],
        },
    },
}

ARCHETYPES = [
    {
        "name": "The Visionary Leader",
        "conditions": {"O": "high", "C": "high", "E": "high", "A": "mid", "N": "low"},
        "desc": "You combine creativity with discipline and social confidence. Built to inspire and execute big ideas.",
        "icon": "🔭",
    },
    {
        "name": "The Empathetic Helper",
        "conditions": {"O": "mid", "C": "mid", "E": "mid", "A": "high", "N": "high"},
        "desc": "Deeply attuned to the feelings of others, driven by a genuine desire to support and nurture the people around you.",
        "icon": "🤝",
    },
    {
        "name": "The Quiet Achiever",
        "conditions": {"O": "mid", "C": "high", "E": "low", "A": "mid", "N": "low"},
        "desc": "You work steadily and independently behind the scenes, delivering results without needing the spotlight.",
        "icon": "🎯",
    },
    {
        "name": "The Creative Explorer",
        "conditions": {"O": "high", "C": "low", "E": "mid", "A": "mid", "N": "mid"},
        "desc": "Drawn to new ideas and experiences, you thrive wherever imagination is valued over routine.",
        "icon": "🧭",
    },
    {
        "name": "The Analytical Thinker",
        "conditions": {"O": "high", "C": "high", "E": "low", "A": "low", "N": "low"},
        "desc": "Driven by logic and precision, you prefer facts over feelings and genuinely love solving complex problems.",
        "icon": "🔬",
    },
    {
        "name": "The Social Connector",
        "conditions": {"O": "mid", "C": "mid", "E": "high", "A": "high", "N": "mid"},
        "desc": "You are the glue in any group — warm, engaging, and genuinely interested in bringing people together.",
        "icon": "🌐",
    },
]

BG = "#0F0F13"
CARD = "#1A1A24"
BORDER = "#2A2A38"
TEXT = "#E8E8F0"
SUBTEXT = "#888899"
ACCENT = "#7C6EFA"

SCALE_LABELS = ["Strongly\nDisagree", "Disagree", "Neutral", "Agree", "Strongly\nAgree"]


def get_bracket(pct):
    if pct >= 60:
        return "high"
    elif pct <= 40:
        return "low"
    return "mid"


def match_archetype(brackets):
    best, top = None, -1
    for arch in ARCHETYPES:
        score = sum(1 for t, lvl in arch["conditions"].items() if brackets.get(t) == lvl)
        if score > top:
            top, best = score, arch
    return best


def compute_results(answers):
    raw = {"O": [], "C": [], "E": [], "A": [], "N": []}
    for i, (_, trait, direction) in enumerate(QUESTIONS):
        val = answers[i]
        raw[trait].append((6 - val) if direction == -1 else val)

    pcts, brackets = {}, {}
    for trait, scores in raw.items():
        pct = (sum(scores) - 5) / 20 * 100
        pcts[trait] = pct
        brackets[trait] = get_bracket(pct)

    return pcts, brackets


class PersonalityApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Personality Test")
        self.configure(bg=BG)
        self.resizable(True, True)
        self.geometry("720x600")
        self.minsize(600, 500)

        self.answers = [None] * len(QUESTIONS)
        self.current = 0

        self.header_font = tkfont.Font(family="Helvetica", size=22, weight="bold")
        self.sub_font = tkfont.Font(family="Helvetica", size=13)
        self.body_font = tkfont.Font(family="Helvetica", size=11)
        self.small_font = tkfont.Font(family="Helvetica", size=10)
        self.tiny_font = tkfont.Font(family="Helvetica", size=9)
        self.label_font = tkfont.Font(family="Helvetica", size=10, weight="bold")

        self.container = tk.Frame(self, bg=BG)
        self.container.pack(fill="both", expand=True)

        self.show_welcome()

    def clear(self):
        for w in self.container.winfo_children():
            w.destroy()

    def show_welcome(self):
        self.clear()

        outer = tk.Frame(self.container, bg=BG)
        outer.place(relx=0.5, rely=0.5, anchor="center")

        tk.Label(outer, text="Personality Test", font=self.header_font,
                 bg=BG, fg=TEXT).pack(pady=(0, 6))

        tk.Label(outer, text="Big Five — OCEAN Model  ·  IPIP & NEO-PI-R validated",
                 font=self.small_font, bg=BG, fg=SUBTEXT).pack()

        tk.Frame(outer, height=1, bg=BORDER, width=420).pack(pady=20)

        desc = ("This test measures five core personality dimensions used in\n"
                "psychological research worldwide. Answer each question honestly —\n"
                "there are no right or wrong answers. It takes about 5 minutes.")
        tk.Label(outer, text=desc, font=self.body_font, bg=BG, fg=SUBTEXT,
                 justify="center", wraplength=420).pack()

        tk.Frame(outer, height=1, bg=BORDER, width=420).pack(pady=20)

        traits_frame = tk.Frame(outer, bg=BG)
        traits_frame.pack(pady=(0, 28))
        for key, name in TRAIT_NAMES.items():
            row = tk.Frame(traits_frame, bg=BG)
            row.pack(pady=2)
            dot = tk.Canvas(row, width=10, height=10, bg=BG, highlightthickness=0)
            dot.pack(side="left", padx=(0, 8))
            dot.create_oval(1, 1, 9, 9, fill=TRAIT_COLORS[key], outline="")
            tk.Label(row, text=name, font=self.body_font, bg=BG, fg=TEXT).pack(side="left")

        start_btn = tk.Button(outer, text="Begin Test →", font=self.label_font,
                              bg=ACCENT, fg="white", relief="flat", cursor="hand2",
                              padx=32, pady=10, bd=0,
                              activebackground="#6A5DE8", activeforeground="white",
                              command=self.show_question)
        start_btn.pack()

    def show_question(self):
        self.clear()

        q_text, trait, _ = QUESTIONS[self.current]
        total = len(QUESTIONS)
        progress = (self.current + 1) / total

        top = tk.Frame(self.container, bg=BG)
        top.pack(fill="x", padx=40, pady=(28, 0))

        progress_bar_bg = tk.Canvas(top, height=4, bg=BORDER, highlightthickness=0)
        progress_bar_bg.pack(fill="x", pady=(0, 10))

        def draw_progress(event=None):
            w = progress_bar_bg.winfo_width()
            progress_bar_bg.delete("all")
            progress_bar_bg.create_rectangle(0, 0, w * progress, 4,
                                             fill=TRAIT_COLORS[trait], outline="")

        progress_bar_bg.bind("<Configure>", draw_progress)
        self.after(10, draw_progress)

        counter_row = tk.Frame(top, bg=BG)
        counter_row.pack(fill="x")
        tk.Label(counter_row, text=f"Question {self.current + 1} of {total}",
                 font=self.small_font, bg=BG, fg=SUBTEXT).pack(side="left")

        trait_pill = tk.Label(counter_row, text=TRAIT_NAMES[trait],
                              font=self.tiny_font, bg=TRAIT_COLORS[trait],
                              fg="white", padx=8, pady=3)
        trait_pill.pack(side="right")

        mid = tk.Frame(self.container, bg=BG)
        mid.pack(fill="both", expand=True, padx=60)

        tk.Frame(mid, height=30, bg=BG).pack()

        tk.Label(mid, text=q_text, font=self.sub_font, bg=BG, fg=TEXT,
                 wraplength=580, justify="center").pack()

        tk.Frame(mid, height=40, bg=BG).pack()

        self.selected_val = tk.IntVar(value=self.answers[self.current] or 0)

        btn_row = tk.Frame(mid, bg=BG)
        btn_row.pack()

        self.option_buttons = []
        for i, label in enumerate(SCALE_LABELS, 1):
            col = tk.Frame(btn_row, bg=BG)
            col.pack(side="left", padx=10)

            btn = tk.Canvas(col, width=52, height=52, bg=BG, highlightthickness=0,
                            cursor="hand2")
            btn.pack()
            self.option_buttons.append((btn, i))

            def on_click(event, val=i):
                self.selected_val.set(val)
                self.refresh_buttons(trait)

            btn.bind("<Button-1>", on_click)

            tk.Label(col, text=label, font=self.tiny_font, bg=BG, fg=SUBTEXT,
                     justify="center").pack(pady=(4, 0))

        self.refresh_buttons(trait)

        bottom = tk.Frame(self.container, bg=BG)
        bottom.pack(fill="x", padx=40, pady=24)

        if self.current > 0:
            back_btn = tk.Button(bottom, text="← Back", font=self.small_font,
                                 bg=CARD, fg=SUBTEXT, relief="flat", cursor="hand2",
                                 padx=18, pady=8, bd=0,
                                 activebackground=BORDER, activeforeground=TEXT,
                                 command=self.go_back)
            back_btn.pack(side="left")

        self.next_btn = tk.Button(bottom, text="Next →", font=self.label_font,
                                  bg=ACCENT, fg="white", relief="flat", cursor="hand2",
                                  padx=24, pady=8, bd=0,
                                  activebackground="#6A5DE8", activeforeground="white",
                                  state="disabled" if not self.answers[self.current] else "normal",
                                  command=self.go_next)
        self.next_btn.pack(side="right")

        self.selected_val.trace_add("write", lambda *_: self.toggle_next())

    def refresh_buttons(self, trait):
        val = self.selected_val.get()
        color = TRAIT_COLORS[trait]
        for btn, i in self.option_buttons:
            btn.delete("all")
            if i == val:
                btn.create_oval(4, 4, 48, 48, fill=color, outline="")
                btn.create_text(26, 26, text=str(i), fill="white",
                                font=tkfont.Font(family="Helvetica", size=16, weight="bold"))
            else:
                btn.create_oval(4, 4, 48, 48, fill=CARD, outline=BORDER, width=2)
                btn.create_text(26, 26, text=str(i), fill=SUBTEXT,
                                font=tkfont.Font(family="Helvetica", size=14))

    def toggle_next(self):
        state = "normal" if self.selected_val.get() > 0 else "disabled"
        self.next_btn.config(state=state)

    def go_next(self):
        self.answers[self.current] = self.selected_val.get()
        if self.current < len(QUESTIONS) - 1:
            self.current += 1
            self.show_question()
        else:
            self.show_results()

    def go_back(self):
        if self.current > 0:
            self.answers[self.current] = self.selected_val.get()
            self.current -= 1
            self.show_question()

    def show_results(self):
        self.clear()

        pcts, brackets = compute_results(self.answers)
        archetype = match_archetype(brackets)

        canvas = tk.Canvas(self.container, bg=BG, highlightthickness=0)
        scrollbar = tk.Scrollbar(self.container, orient="vertical", command=canvas.yview)
        canvas.configure(yscrollcommand=scrollbar.set)

        scrollbar.pack(side="right", fill="y")
        canvas.pack(side="left", fill="both", expand=True)

        frame = tk.Frame(canvas, bg=BG)
        frame_id = canvas.create_window((0, 0), window=frame, anchor="nw")

        def on_resize(event):
            canvas.itemconfig(frame_id, width=event.width)

        canvas.bind("<Configure>", on_resize)
        frame.bind("<Configure>", lambda e: canvas.configure(
            scrollregion=canvas.bbox("all")))

        def on_mouse_wheel(event):
            canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

        canvas.bind_all("<MouseWheel>", on_mouse_wheel)

        pad = tk.Frame(frame, bg=BG)
        pad.pack(fill="both", padx=40, pady=30)

        tk.Label(pad, text="Your Results", font=self.header_font,
                 bg=BG, fg=TEXT).pack(anchor="w")
        tk.Label(pad, text="Based on the Big Five personality model",
                 font=self.small_font, bg=BG, fg=SUBTEXT).pack(anchor="w", pady=(2, 20))

        arch_card = tk.Frame(pad, bg=CARD, padx=20, pady=18)
        arch_card.pack(fill="x", pady=(0, 20))

        tk.Label(arch_card, text=archetype["icon"] + "  " + archetype["name"],
                 font=tkfont.Font(family="Helvetica", size=16, weight="bold"),
                 bg=CARD, fg=TEXT).pack(anchor="w")
        tk.Label(arch_card, text=archetype["desc"],
                 font=self.body_font, bg=CARD, fg=SUBTEXT,
                 wraplength=580, justify="left").pack(anchor="w", pady=(6, 0))

        tk.Label(pad, text="Trait Scores", font=self.label_font,
                 bg=BG, fg=SUBTEXT).pack(anchor="w", pady=(0, 10))

        bars_frame = tk.Frame(pad, bg=BG)
        bars_frame.pack(fill="x", pady=(0, 20))

        for trait, name in TRAIT_NAMES.items():
            pct = pcts[trait]
            color = TRAIT_COLORS[trait]

            row = tk.Frame(bars_frame, bg=BG)
            row.pack(fill="x", pady=5)

            name_label = tk.Label(row, text=name, font=self.body_font,
                                  bg=BG, fg=TEXT, width=18, anchor="w")
            name_label.pack(side="left")

            bar_bg = tk.Canvas(row, height=16, bg=BORDER, highlightthickness=0)
            bar_bg.pack(side="left", fill="x", expand=True, padx=(8, 10))

            pct_label = tk.Label(row, text=f"{pct:.0f}%", font=self.small_font,
                                 bg=BG, fg=SUBTEXT, width=4, anchor="e")
            pct_label.pack(side="right")

            def draw_bar(event=None, b=bar_bg, p=pct, c=color):
                w = b.winfo_width()
                b.delete("all")
                b.create_rectangle(0, 0, w, 16, fill=BORDER, outline="")
                filled_w = max(int(w * p / 100), 1)
                b.create_rectangle(0, 0, filled_w, 16, fill=c, outline="")

            bar_bg.bind("<Configure>", draw_bar)
            self.after(50, lambda b=bar_bg, p=pct, c=color: draw_bar(b=b, p=p, c=c))

        tk.Frame(pad, height=1, bg=BORDER).pack(fill="x", pady=(0, 20))

        tk.Label(pad, text="Detailed Breakdown", font=self.label_font,
                 bg=BG, fg=SUBTEXT).pack(anchor="w", pady=(0, 12))

        for trait, name in TRAIT_NAMES.items():
            bracket = brackets[trait]
            color = TRAIT_COLORS[trait]

            card = tk.Frame(pad, bg=CARD, padx=18, pady=14)
            card.pack(fill="x", pady=(0, 10))

            header_row = tk.Frame(card, bg=CARD)
            header_row.pack(fill="x")

            accent_bar = tk.Canvas(header_row, width=4, height=20, bg=CARD,
                                   highlightthickness=0)
            accent_bar.pack(side="left", padx=(0, 10))
            accent_bar.create_rectangle(0, 0, 4, 20, fill=color, outline="")

            if bracket == "mid":
                label_text = name + " — Balanced"
            else:
                label_text = name + " — " + PROFILES[trait][bracket]["label"]

            tk.Label(header_row, text=label_text,
                     font=tkfont.Font(family="Helvetica", size=12, weight="bold"),
                     bg=CARD, fg=TEXT).pack(side="left")

            pct_tag = tk.Label(header_row, text=f"{pcts[trait]:.0f}%",
                               font=self.tiny_font, bg=color, fg="white",
                               padx=6, pady=2)
            pct_tag.pack(side="right")

            if bracket == "mid":
                hp = PROFILES[trait]["high"]["label"].lower()
                lp = PROFILES[trait]["low"]["label"].lower()
                desc_text = (f"You sit in the middle on this dimension, naturally blending "
                             f"{hp} and {lp} tendencies depending on the situation.")
                tk.Label(card, text=desc_text, font=self.body_font, bg=CARD, fg=SUBTEXT,
                         wraplength=560, justify="left").pack(anchor="w", pady=(8, 0))
            else:
                profile = PROFILES[trait][bracket]
                tk.Label(card, text=profile["desc"], font=self.body_font, bg=CARD,
                         fg=SUBTEXT, wraplength=560, justify="left").pack(anchor="w", pady=(8, 6))

                sw_frame = tk.Frame(card, bg=CARD)
                sw_frame.pack(fill="x")

                s_col = tk.Frame(sw_frame, bg=CARD)
                s_col.pack(side="left", fill="both", expand=True, padx=(0, 10))

                tk.Label(s_col, text="Strengths", font=self.tiny_font,
                         bg=CARD, fg=color).pack(anchor="w")
                for s in profile["strengths"]:
                    tk.Label(s_col, text="+ " + s, font=self.tiny_font,
                             bg=CARD, fg=TEXT).pack(anchor="w")

                w_col = tk.Frame(sw_frame, bg=CARD)
                w_col.pack(side="left", fill="both", expand=True)

                tk.Label(w_col, text="Weaknesses", font=self.tiny_font,
                         bg=CARD, fg="#888899").pack(anchor="w")
                for w in profile["weaknesses"]:
                    tk.Label(w_col, text="− " + w, font=self.tiny_font,
                             bg=CARD, fg=SUBTEXT).pack(anchor="w")

        sorted_traits = sorted(pcts, key=lambda t: pcts[t], reverse=True)
        top_two = sorted_traits[:2]
        bottom_one = sorted_traits[-1]

        summary_card = tk.Frame(pad, bg="#1C1C2E", padx=20, pady=16)
        summary_card.pack(fill="x", pady=(10, 4))

        tk.Label(summary_card, text="Summary", font=self.label_font,
                 bg="#1C1C2E", fg=SUBTEXT).pack(anchor="w", pady=(0, 6))

        summary_text = (
            f"Your strongest dimensions are {TRAIT_NAMES[top_two[0]]} and "
            f"{TRAIT_NAMES[top_two[1]]}, which shape how you engage with the world. "
            f"The area with the most room for growth is {TRAIT_NAMES[bottom_one]}."
        )
        tk.Label(summary_card, text=summary_text, font=self.body_font,
                 bg="#1C1C2E", fg=TEXT, wraplength=560, justify="left").pack(anchor="w")

        tk.Label(pad, text="Sources: IPIP (Goldberg, 1999)  ·  NEO-PI-R (Costa & McCrae, 1992)",
                 font=self.tiny_font, bg=BG, fg=BORDER).pack(pady=(16, 0))

        retry_btn = tk.Button(pad, text="Take Test Again", font=self.small_font,
                              bg=CARD, fg=SUBTEXT, relief="flat", cursor="hand2",
                              padx=18, pady=8, bd=0,
                              activebackground=BORDER, activeforeground=TEXT,
                              command=self.restart)
        retry_btn.pack(pady=(10, 0))

    def restart(self):
        self.answers = [None] * len(QUESTIONS)
        self.current = 0
        self.show_welcome()


if __name__ == "__main__":
    app = PersonalityApp()
    app.mainloop()