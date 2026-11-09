"""Generate compact SVG explanations for the shared genetic algorithm and applications."""

from html import escape
from pathlib import Path


ROOT = Path(__file__).parent
BLUE = "#2078ba"
ORANGE = "#c96516"
GRAY = "#737b85"
GREEN = "#198568"
PURPLE = "#7954a8"
INK = "#252b32"


class Diagram:
    def __init__(self, height):
        self.parts = [
            f'<svg xmlns="http://www.w3.org/2000/svg" width="440" '
            f'height="{height}" viewBox="0 0 440 {height}">',
            f'<rect width="440" height="{height}" fill="white"/>',
            '<defs><marker id="arrow" viewBox="0 0 10 10" refX="9" '
            'refY="5" markerWidth="6" markerHeight="6" orient="auto">'
            '<path d="M0 0 L10 5 L0 10" fill="none" '
            'stroke="context-stroke"/></marker></defs>',
        ]

    def text(self, x, y, text, color=INK, anchor="middle"):
        self.parts.append(
            f'<text x="{x}" y="{y}" text-anchor="{anchor}" '
            f'font-family="Arial, Noto Sans CJK KR, sans-serif" '
            f'font-size="16" fill="{color}">{escape(str(text))}</text>'
        )

    def line(self, x1, y1, x2, y2, color=GRAY, arrow=False, dashed=False):
        self.parts.append(
            f'<path d="M{x1} {y1} L{x2} {y2}" fill="none" '
            f'stroke="{color}" stroke-width="2"'
            + (' marker-end="url(#arrow)"' if arrow else "")
            + (' stroke-dasharray="4 4"' if dashed else "")
            + "/>"
        )

    def box(self, x, y, width, height, color=BLUE, fill="white"):
        self.parts.append(
            f'<rect x="{x}" y="{y}" width="{width}" height="{height}" '
            f'rx="5" fill="{fill}" stroke="{color}" stroke-width="1.6"/>'
        )

    def genes(self, values, x, y, step=46, colors=None):
        for index, value in enumerate(values):
            color = colors[index] if colors else BLUE
            self.box(x + step * index, y, 34, 30, color)
            self.text(x + step * index + 17, y + 21, value, color)

    def save(self, filename):
        (ROOT / filename).write_text("".join(self.parts) + "</svg>\n", encoding="utf-8")


def create_figures():
    figure = Diagram(206)
    figure.text(220, 23, "Current candidates", BLUE)
    for i, bits in enumerate(["1000", "0010", "0000", "0100"]):
        x = 14 + 108 * i
        figure.box(x, 35, 87, 34, BLUE)
        figure.text(x + 43, 58, bits, BLUE)
    figure.line(220, 77, 220, 119, ORANGE, arrow=True)
    figure.text(235, 103, "Choose + change", ORANGE, "start")
    for i, bits in enumerate(["1000", "1010", "1011", "0011"]):
        x = 14 + 108 * i
        color = BLUE if i == 0 else ORANGE
        figure.box(x, 128, 87, 34, color)
        figure.text(x + 43, 151, bits, color)
    figure.text(220, 187, "Next candidates: keep the best + add new ones")
    figure.save("genetic_algorithm_overview.svg")

    figure = Diagram(208)
    figure.text(220, 23, "selection_top_k = 2", PURPLE)
    figure.text(85, 51, "Ranked population", BLUE)
    figure.box(12, 64, 145, 128, BLUE)
    for i, label in enumerate(["A: 4", "B: 3", "C: 2", "D: 1"]):
        figure.text(84, 89 + i*29, label, GREEN if i in (0,1) else GRAY)
    figure.line(165, 128, 198, 128, GREEN, arrow=True)
    figure.text(270, 51, "Top 2", GREEN)
    figure.box(206, 64, 128, 90, GREEN)
    figure.text(270, 91, "A: 4", GREEN)
    figure.text(270, 128, "B: 3", GREEN)
    figure.line(342, 100, 366, 100, GREEN, arrow=True)
    figure.text(399, 84, "Pick", GREEN)
    figure.text(399, 113, "B", GREEN)
    figure.text(270, 183, "Random choice from top 2")
    figure.save("selection.svg")

    figure = Diagram(223)
    figure.text(220, 23, "crossover_rate = 1.0", PURPLE)
    figure.text(12, 59, "Binary", BLUE, "start")
    figure.text(269, 59, "[1 | 0] + [0 | 1] → [1 | 1]", ORANGE)
    figure.line(14, 83, 426, 83, GRAY, dashed=True)
    figure.text(12, 113, "Real", BLUE, "start")
    figure.text(267, 113, "blend_weight = 0.5", PURPLE)
    figure.text(220, 145, "[0.2, 0.4]  &  [0.8, 0.6]", BLUE)
    figure.line(220, 153, 220, 177, ORANGE, arrow=True)
    figure.text(220, 204, "Average: [0.5, 0.5]", ORANGE)
    figure.save("crossover.svg")

    figure = Diagram(164)
    figure.text(220, 23, "mutation_rate = 0.3", PURPLE)
    figure.text(12, 60, "Binary", BLUE, "start")
    figure.text(269, 60, "[1, 0] → [1, 1]", ORANGE)
    figure.text(220, 101, "mutation_scale = 0.1", PURPLE)
    figure.text(12, 138, "Real", BLUE, "start")
    figure.text(269, 138, "[0.5, 0.5] → [0.5, 0.56]", ORANGE)
    figure.save("mutation.svg")

    figure = Diagram(218)
    figure.text(220, 23, "elite_count = 1", PURPLE)
    figure.text(99, 54, "Current", BLUE)
    figure.text(339, 54, "Next", BLUE)
    figure.box(12, 65, 175, 140, BLUE)
    figure.box(253, 65, 175, 140, BLUE)
    figure.box(22, 77, 155, 27, BLUE, "#eff7ff")
    figure.text(99, 97, "A: 4 (best)", BLUE)
    for i, label in enumerate(["B: 3", "C: 2", "D: 1"]):
        figure.text(99, 129+i*31, label, GRAY)
    figure.line(193, 90, 247, 90, BLUE, arrow=True)
    figure.box(263, 77, 155, 27, BLUE, "#eff7ff")
    figure.text(340, 97, "A: 4 (copy)", BLUE)
    for i in range(3):
        figure.text(340, 129+i*31, "New child", ORANGE)
    figure.save("elitism.svg")

    figure = Diagram(398)
    figure.box(105, 6, 230, 34, BLUE)
    figure.text(220, 29, "Start with candidates", BLUE)
    figure.line(220, 44, 220, 64, GRAY, arrow=True)
    figure.box(25, 65, 390, 280, GRAY)
    figure.text(220, 89, "Repeat generations times", PURPLE)
    steps = [(103, "Rank by score; keep elites", BLUE),
             (162, "Selection: choose from top k", GREEN),
             (221, "Crossover + mutation → child", ORANGE),
             (300, "Replace the population", BLUE)]
    for y, label, color in steps:
        figure.box(60, y, 320, 32, color)
        figure.text(220, y+22, label, color)
    figure.line(220, 138, 220, 158, GRAY, arrow=True)
    figure.line(220, 197, 220, 217, GRAY, arrow=True)
    figure.text(220, 277, "Repeat until the next population is full")
    figure.line(220, 281, 220, 296, GRAY, arrow=True)
    figure.line(220, 349, 220, 361, GRAY, arrow=True)
    figure.box(105, 364, 230, 32, BLUE)
    figure.text(220, 386, "Return the best", BLUE)
    figure.save("generation_cycle.svg")

    figure = Diagram(152)
    figure.box(20, 10, 170, 58, BLUE)
    figure.text(105, 34, "Light", BLUE)
    figure.text(105, 57, "Medium (1)", BLUE)
    figure.box(250, 10, 170, 58, BLUE)
    figure.text(335, 34, "Nutrient", BLUE)
    figure.text(335, 57, "High (2)", BLUE)
    figure.line(105, 77, 184, 104, GREEN, arrow=True)
    figure.line(335, 77, 256, 104, GREEN, arrow=True)
    figure.box(114, 111, 212, 34, GREEN)
    figure.text(220, 134, "Growth: 7 mm", GREEN)
    figure.save("biology_encoding.svg")

    figure = Diagram(178)
    figure.text(220, 23, "Cost (million KRW)")
    figure.text(265, 53, "Budget: 7", PURPLE)
    figure.line(265, 61, 265, 170, PURPLE, dashed=True)
    for y, label, cost, color, verdict in [(76,"A + C",6,GREEN,"OK"),(130,"A + D",9,GRAY,"Over")]:
        figure.text(12, y+23, label, color, "start")
        figure.box(90, y, cost*25, 32, color, "#f6f8fa")
        figure.text(107, y+23, cost, color)
        figure.text(366, y+23, verdict, color, "start")
    figure.save("budget_feasibility.svg")

    figure = Diagram(172)
    for y, computer, tasks in [(24, 0, [("A",8),("B",7)]), (87, 1, [("C",6),("D",5)])]:
        figure.text(12, y+23, f"CPU {computer}", BLUE, "start")
        x = 87
        for name, duration in tasks:
            width = duration*19
            figure.box(x, y, width, 34, BLUE, "#f4f9fd")
            figure.text(x+width/2, y+23, f"{name}: {duration} s", BLUE)
            x += width
        figure.text(x+9, y+23, f"{sum(t[1] for t in tasks)} s", ORANGE, "start")
    figure.line(87, 10, 87, 129, GRAY, dashed=True)
    figure.text(220, 160, "Start together → finish after 15 s", ORANGE)
    figure.save("task_assignment.svg")


if __name__ == "__main__":
    create_figures()
