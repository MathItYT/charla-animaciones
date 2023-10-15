from manim import *
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import cmasher


def challenge1():
    plt.rc('text', usetex=True)
    px = 1/plt.rcParams['figure.dpi']
    fig, ax = plt.subplots(figsize=(1920*px, 1080*px))
    ax: plt.Axes
    fig.set_facecolor("black")
    ax.set_facecolor("black")
    ax.spines['bottom'].set_color("white")
    ax.spines['top'].set_color("white")
    ax.spines['left'].set_color("white")
    ax.spines['right'].set_color("white")
    ax.xaxis.label.set_color("white")
    ax.yaxis.label.set_color("white")
    ax.tick_params(axis='x', colors="white")
    ax.tick_params(axis='y', colors="white")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_title(r"$$y = x^2$$")
    x = np.linspace(-2, 2, 10000)
    rate_func = smooth

    fps = 60
    duration = 5
    frames = fps * duration

    def update_line(n):
        ax.clear()
        interpolated_x = x[round(interpolate(5000, 0, rate_func(
            n/frames))):round(interpolate(5000, 10000, rate_func(n/frames)))]
        interpolated_y = interpolated_x**2
        ax.plot(interpolated_x, interpolated_y, color="red", linewidth=3)
        ax.set_xlim(-2, 2)
        ax.set_ylim(0, 4)
        return ax,

    anim = FuncAnimation(fig, update_line, frames=frames,
                         interval=1000/fps)
    anim.save("challenge1.mp4", fps=fps)


class Challenge2(Scene):
    def construct(self):
        import random

        EVENTS = [0, 1]
        PROBABILITY = 0.5
        N_EVENTS = 100
        COLOR_0 = BLUE
        COLOR_1 = RED

        def get_random_event():
            return random.choice(EVENTS)

        def get_random_events(n):
            return np.array([get_random_event() for _ in range(n)])

        def count_event_occurrences_until_n(events, n):
            # Events are zeros and ones, so we can just sum them
            return np.cumsum(events)[:n]

        ax = Axes(
            x_range=[0, N_EVENTS, 10],
            y_range=[0, 1, 0.1],
            x_length=5,
            y_length=5
        ).to_edge(RIGHT)
        ax.set_stroke(width=4)
        ax.add_coordinates()
        y_label = ax.get_y_axis_label(MathTex("{n\\over N}"))
        x_label = ax.get_x_axis_label(MathTex("N"))
        self.add(ax, x_label, y_label)
        prob_graph = ax.plot(lambda x: PROBABILITY, color=RED)
        self.add(prob_graph)
        line_graph = VMobject()
        x = np.arange(
            1, N_EVENTS + 1)
        events = get_random_events(N_EVENTS)
        y = count_event_occurrences_until_n(
            events, N_EVENTS) / x

        def update_line_graph(line_graph, n):
            line_graph.become(ax.plot_line_graph(
                x[:n+1], y[:n+1], line_color=YELLOW,
                stroke_width=1, vertex_dot_radius=0.03))

        def get_event_mobject(n):
            dot = Dot(color=COLOR_1 if events[n] == 1 else COLOR_0)
            dot.move_to(final_slots[n])
            return dot

        self.add(line_graph)
        final_slots = VGroup(*[Square() for _ in range(N_EVENTS)])
        final_slots.arrange_in_grid(rows=10, buff=0)
        final_slots.scale_to_fit_height(5)
        final_slots.to_edge(LEFT)
        self.add(final_slots)

        for i in range(N_EVENTS):
            update_line_graph(line_graph, i)
            self.add(get_event_mobject(i))
            self.wait()


def challenge3_displacement_map():
    x = np.linspace(-1, 1, 2000)
    y = np.linspace(-1, 1, 2000)
    xx, yy = np.meshgrid(x, y)
    z = np.sin(5*xx)*np.cos(5*yy)/5
    plt.imsave("challenge3.png", z, cmap="gray")


def challenge3_color_map():
    x = np.linspace(-1, 1, 2000)
    y = np.linspace(-1, 1, 2000)
    xx, yy = np.meshgrid(x, y)
    z = np.sin(5*xx)*np.cos(5*yy)/5
    plt.imsave("challenge3-color.png", z, cmap=cmasher.guppy)


if __name__ == "__main__":
    # challenge1()
    # Challenge2().render(preview=True)
    # challenge3_displacement_map()
    challenge3_color_map()
