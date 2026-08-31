"""Visual demonstrations used by concept.ipynb.

Keep implementation details here so the lecture notebook can focus on concepts.
The notebook loads this file from the local folder or JSPCV's uploads folder.
"""

DEMO_VERSION = "2026-09-01-controlled-comparison-v2"


def show_system_behavior():
    # Controlled comparison: hold external inputs constant and change only the decision.
    import numpy as np
    import matplotlib.pyplot as plt

    outside_temperature = np.full(12, 31.0)
    occupants = np.full(12, 20.0)
    candidates = (
        ("Low cooling", np.full(12, 1.0), "tab:red"),
        ("Moderate cooling", np.full(12, 3.0), "tab:blue"),
        ("Strong cooling", np.full(12, 4.0), "tab:purple"),
    )

    temperature_paths = {}
    for label, cooling_schedule, _ in candidates:
        temperatures = [27.0]
        for outdoor, people, cooling in zip(
            outside_temperature, occupants, cooling_schedule
        ):
            current = temperatures[-1]
            temperatures.append(
                current
                + 0.12 * (outdoor - current)
                + 0.012 * people
                - 0.45 * cooling
            )
        temperature_paths[label] = np.array(temperatures)

    decision_steps = np.arange(1, len(outside_temperature) + 1)
    state_steps = np.arange(len(outside_temperature) + 1)
    figure, axes = plt.subplots(1, 2, figsize=(10.8, 3.8))

    for label, cooling_schedule, color in candidates:
        axes[0].step(
            decision_steps, cooling_schedule, where="mid",
            linewidth=2, color=color, label=label,
        )
    axes[0].set(
        xlabel="Time step", ylabel="Cooling level",
        title="Candidate decisions",
        xlim=(1, 12), ylim=(0, 5),
    )
    axes[0].legend(fontsize=8)

    axes[1].axhspan(22, 24, color="tab:green", alpha=0.15, label="Comfort range")
    axes[1].plot(
        state_steps, np.full_like(state_steps, 31.0, dtype=float),
        linestyle="--", color="black", linewidth=1.5,
        label="Outdoor temperature: fixed at 31 °C",
    )
    for label, _, color in candidates:
        axes[1].plot(
            state_steps, temperature_paths[label],
            marker="o", linewidth=2, color=color, label=label,
        )
    axes[1].set(
        xlabel="Time step", ylabel="Indoor temperature (°C)",
        title="Different decisions produce different behavior",
        xlim=(0, 12), ylim=(18, 32),
    )
    axes[1].legend(fontsize=8)

    for axis in axes:
        axis.grid(alpha=0.25)
    figure.suptitle(
        "Controlled comparison · same outdoor temperature and occupancy",
        fontsize=11,
    )
    figure.tight_layout(rect=(0, 0, 1, 0.94))
    plt.show()
    plt.close(figure)


def show_interactive_explorer():
    # Interactive running example: explore candidate decisions and one hyperparameter.
    import sys
    import numpy as np
    import matplotlib

    # Use ipympl in VS Code/Jupyter; JSPCV Playground supplies its own browser bridge.
    if sys.platform != "emscripten":
        try:
            matplotlib.use("widget", force=True)
        except (RuntimeError, ValueError):
            # A kernel started before ipympl was installed may cache the old backend list.
            from matplotlib.backends import backend_registry
            backend_registry._clear()
            matplotlib.use("widget", force=True)

    import matplotlib.pyplot as plt
    from matplotlib.widgets import Slider

    # Start the interactive example with its own figure manager.
    plt.close("all")

    # Fixed parameters: given during this analysis, so they are not sliders.
    WEATHER_EXCHANGE = 0.12
    OCCUPANT_HEAT = 0.012
    COOLING_EFFECT = 0.45

    # External inputs: held constant across candidates for a controlled comparison.
    outside_temperature = np.full(12, 31.0)
    occupants = np.full(12, 20.0)

    # Requirements: these define feasibility rather than preference.
    MIN_TEMPERATURE = 20.0
    MAX_TEMPERATURE = 30.0
    MAX_ENERGY = 60.0

    def simulate(early_decision, late_decision):
        cooling_schedule = np.r_[np.full(6, early_decision), np.full(6, late_decision)]
        temperatures = [27.0]
        for outdoor, people, cooling in zip(outside_temperature, occupants, cooling_schedule):
            current = temperatures[-1]
            temperatures.append(
                current
                + WEATHER_EXCHANGE * (outdoor - current)
                + OCCUPANT_HEAT * people
                - COOLING_EFFECT * cooling
            )
        temperatures = np.array(temperatures)
        discomfort = np.sum(
            np.maximum(temperatures[1:] - 24, 0) ** 2
            + np.maximum(22 - temperatures[1:], 0) ** 2
        )
        energy = 0.5 * np.sum(cooling_schedule ** 2)
        feasible = (
            temperatures[1:].min() >= MIN_TEMPERATURE
            and temperatures[1:].max() <= MAX_TEMPERATURE
            and energy <= MAX_ENERGY
        )
        return temperatures, discomfort, energy, feasible

    candidate_levels = np.arange(0.0, 5.01, 0.5)
    grid_shape = (len(candidate_levels), len(candidate_levels))
    discomfort_grid = np.zeros(grid_shape)
    energy_grid = np.zeros(grid_shape)
    feasible_grid = np.zeros(grid_shape, dtype=bool)
    records = []
    for early_index, early in enumerate(candidate_levels):
        for late_index, late in enumerate(candidate_levels):
            _, discomfort, energy, feasible = simulate(early, late)
            discomfort_grid[early_index, late_index] = discomfort
            energy_grid[early_index, late_index] = energy
            feasible_grid[early_index, late_index] = feasible
            records.append((early, late, discomfort, energy, feasible))

    def evaluate_landscape(energy_weight):
        objective_grid = discomfort_grid + energy_weight * energy_grid
        objective_grid = np.where(feasible_grid, objective_grid, np.nan)
        best_index = np.unravel_index(np.nanargmin(objective_grid), objective_grid.shape)
        early = candidate_levels[best_index[0]]
        late = candidate_levels[best_index[1]]
        return objective_grid, (
            objective_grid[best_index], early, late,
            discomfort_grid[best_index], energy_grid[best_index],
        )

    # One Matplotlib figure stays interactive in both VS Code/Jupyter and JSPCV Playground.
    figure, axes = plt.subplots(1, 3, figsize=(12, 8))
    figure.subplots_adjust(left=0.07, right=0.98, bottom=0.35, top=0.80, wspace=0.34)

    initial_early, initial_late, initial_weight = 3.5, 1.5, 1.0
    initial_temperatures, initial_discomfort, initial_energy, initial_feasible = simulate(
        initial_early, initial_late
    )
    initial_objective_grid, initial_best = evaluate_landscape(initial_weight)

    # Panel 1: a decision changes the physical system trajectory.
    axes[0].axhspan(MIN_TEMPERATURE, MAX_TEMPERATURE,
                    color="tab:blue", alpha=0.08, label="Feasible range")
    axes[0].axhspan(22, 24, color="tab:green", alpha=0.18, label="Comfort range")
    temperature_line, = axes[0].plot(
        np.arange(len(initial_temperatures)), initial_temperatures,
        marker="o", linewidth=2, color="tab:blue",
    )
    axes[0].set(xlabel="Time step", ylabel="Indoor temperature (°C)", ylim=(15, 34))
    axes[0].grid(alpha=0.25)
    axes[0].legend(fontsize=8)

    # Panel 2: every candidate becomes raw discomfort and energy performance.
    feasible_points = np.array([(r[3], r[2]) for r in records if r[4]])
    infeasible_points = np.array([(r[3], r[2]) for r in records if not r[4]])
    axes[1].scatter(infeasible_points[:, 0], infeasible_points[:, 1],
                    marker="x", color="lightgray", label="Infeasible grid candidate")
    axes[1].scatter(feasible_points[:, 0], feasible_points[:, 1],
                    color="teal", alpha=0.55, label="Feasible grid candidate")
    current_performance = axes[1].scatter(
        initial_energy, initial_discomfort, marker="s", s=90,
        color="tab:orange", edgecolor="black", label="Current candidate",
    )
    best_performance = axes[1].scatter(
        initial_best[4], initial_best[3], marker="*", s=190,
        color="gold", edgecolor="black", label="Best grid candidate",
    )
    axes[1].set(xlabel="Raw energy performance $E$",
                ylabel="Raw discomfort performance $D$", xlim=(0, 155), ylim=(0, 500),
                title="Physical performance of candidate decisions")
    axes[1].grid(alpha=0.25)
    axes[1].legend(loc="upper right", fontsize=7)

    # Panel 3: the hyperparameter changes evaluation and the preferred candidate.
    cmap = plt.colormaps["viridis_r"].copy()
    cmap.set_bad("#e6e6e6")
    objective_image = axes[2].imshow(
        initial_objective_grid, origin="lower", cmap=cmap,
        extent=(-0.25, 5.25, -0.25, 5.25), aspect="equal",
    )
    current_decision = axes[2].scatter(
        initial_late, initial_early, marker="s", s=90,
        color="tab:orange", edgecolor="black", label="Current",
    )
    best_decision = axes[2].scatter(
        initial_best[2], initial_best[1], marker="*", s=190,
        color="gold", edgecolor="black", label="Best grid candidate",
    )
    axes[2].set(xticks=np.arange(0, 5.1, 1), yticks=np.arange(0, 5.1, 1),
                xlabel="Late cooling decision", ylabel="Early cooling decision")
    axes[2].legend(fontsize=8)

    status_text = figure.text(0.5, 0.955, "", ha="center", va="top",
                              fontsize=12, fontweight="bold")
    metrics_text = figure.text(0.5, 0.915, "", ha="center", va="top", fontsize=10)
    figure.text(
        0.5, 0.255,
        f"Fixed parameters — not adjustable: a={WEATHER_EXCHANGE} (weather exchange), "
        f"b={OCCUPANT_HEAT} (occupant heat), c={COOLING_EFFECT} (cooling effect)",
        ha="center", va="center", fontsize=9,
        bbox=dict(boxstyle="round,pad=0.35", facecolor="#f1f3f5", edgecolor="#adb5bd"),
    )

    early_axis = figure.add_axes([0.35, 0.175, 0.55, 0.025])
    late_axis = figure.add_axes([0.35, 0.115, 0.55, 0.025])
    weight_axis = figure.add_axes([0.35, 0.055, 0.55, 0.025])
    early_slider = Slider(early_axis, "Decision · early cooling", 0.0, 5.0,
                          valinit=initial_early, valstep=0.25, valfmt="%1.2f")
    late_slider = Slider(late_axis, "Decision · late cooling", 0.0, 5.0,
                         valinit=initial_late, valstep=0.25, valfmt="%1.2f")
    energy_weight_slider = Slider(
        weight_axis, "Hyperparameter · energy weight", 0.0, 3.0,
        valinit=initial_weight, valstep=0.1, valfmt="%1.1f", color="tab:purple",
    )

    # This state dictionary also makes the conceptual distinction easy to verify.
    systems_thinking_state = {}

    def refresh(_=None):
        early = early_slider.val
        late = late_slider.val
        energy_weight = energy_weight_slider.val
        temperatures, discomfort, energy, feasible = simulate(early, late)
        objective = discomfort + energy_weight * energy
        objective_grid, best = evaluate_landscape(energy_weight)
        status = "FEASIBLE" if feasible else "INFEASIBLE"

        temperature_line.set_ydata(temperatures)
        current_performance.set_offsets([[energy, discomfort]])
        best_performance.set_offsets([[best[4], best[3]]])
        objective_image.set_data(objective_grid)
        objective_image.set_clim(np.nanmin(objective_grid), np.nanmax(objective_grid))
        current_decision.set_offsets([[late, early]])
        best_decision.set_offsets([[best[2], best[1]]])

        axes[0].set_title(f"Candidate system behavior: {status.lower()}")
        axes[2].set_title(f"Evaluation landscape\nenergy weight = {energy_weight:.1f}")
        status_text.set_text(
            f"Current candidate: early={early:.2f}, late={late:.2f}  ·  {status}"
        )
        status_text.set_color("#087f5b" if feasible else "#c92a2a")
        metrics_text.set_text(
            f"Raw performance: D={discomfort:.2f}, E={energy:.2f}  |  "
            f"J=D+{energy_weight:.1f}E={objective:.2f}  |  "
            f"best grid: early={best[1]:.2f}, late={best[2]:.2f}, J={best[0]:.2f}"
        )

        systems_thinking_state.clear()
        systems_thinking_state.update(
            early=early, late=late, energy_weight=energy_weight,
            temperatures=temperatures.copy(), discomfort=discomfort, energy=energy,
            feasible=feasible, objective=objective, best=best,
        )
        figure.canvas.draw_idle()

    for slider in (early_slider, late_slider, energy_weight_slider):
        slider.on_changed(refresh)

    # Keep references alive after cell execution so browser pointer events remain connected.
    figure._systems_thinking_sliders = (early_slider, late_slider, energy_weight_slider)
    refresh()
    plt.show()
    from types import SimpleNamespace

    return SimpleNamespace(
        figure=figure,
        state=systems_thinking_state,
        refresh=refresh,
        simulate=simulate,
        evaluate_landscape=evaluate_landscape,
        early_slider=early_slider,
        late_slider=late_slider,
        energy_weight_slider=energy_weight_slider,
    )
