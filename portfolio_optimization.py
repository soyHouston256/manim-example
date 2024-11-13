from manim import *
import numpy as np

class OptimizationComparison(Scene):
    def construct(self):
        # Datos de los resultados
        assets = [3, 5, 10, 20, 30, 40, 50, 100, 200, 300, 500]
        hc_fitness = [3.4, 4.0, 3.8, 3.95, 3.85, 3.83, 3.85, 3.87, 3.9, 3.91, 3.9]
        sa_fitness = [3.3, 3.7, 4.2, 4.0, 4.0, 4.0, 4.0, 4.45, 4.47, 4.52, 4.51]
        hc_time = [0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5, 0.55, 0.6]
        sa_time = [5, 6, 6.5, 7, 7.2, 7.5, 8, 12, 16, 20, 38]

        # Configuración del plano para el gráfico de Fitness
        fitness_axes = Axes(
            x_range=[0, 550, 100],
            y_range=[3, 5, 0.5],
            axis_config={"include_tip": False},
            x_axis_config={"numbers_to_include": [0, 100, 200, 300, 400, 500]},
            y_axis_config={"numbers_to_include": np.arange(3, 5.1, 0.5)},
        ).scale(0.7)

        # Títulos y etiquetas para el gráfico de Fitness
        fitness_title = Text("Fitness Comparison").scale(0.8)
        fitness_title.to_edge(UP)
        x_label = Text("Number of Assets (n)", font_size=20)
        x_label.next_to(fitness_axes.x_axis, DOWN)
        y_label = Text("Fitness", font_size=20).rotate(90 * DEGREES)
        y_label.next_to(fitness_axes.y_axis, LEFT)

        # Crear las líneas de datos
        hc_points = [fitness_axes.coords_to_point(x, y) for x, y in zip(assets, hc_fitness)]
        sa_points = [fitness_axes.coords_to_point(x, y) for x, y in zip(assets, sa_fitness)]
        
        hc_line = VMobject()
        hc_line.set_points_smoothly(hc_points)
        hc_line.set_color(BLUE)
        
        sa_line = VMobject()
        sa_line.set_points_smoothly(sa_points)
        sa_line.set_color(GREEN)

        # Leyenda
        legend = VGroup(
            VGroup(
                Dot(color=BLUE),
                Text("Hill Climbing", font_size=20)
            ).arrange(RIGHT),
            VGroup(
                Dot(color=GREEN),
                Text("Simulated Annealing", font_size=20)
            ).arrange(RIGHT)
        ).arrange(DOWN, aligned_edge=LEFT)
        #legend.to_corner(UR)
        legend.move_to(RIGHT * 5 + UP * 1)
        #legend.move_to(RIGHT * 5 + UP * 1)

        # Animación del primer gráfico
        self.play(Write(fitness_title), run_time=1)  # 2 segundos
        self.play(Create(fitness_axes), Write(x_label), Write(y_label), run_time=5)  # 3 segundos
        self.play(Create(hc_line), Create(sa_line), run_time=5)  # 3 segundos
        self.play(FadeIn(legend), run_time=2)  # 2 segundos
        self.wait(2)

        # Transition to time comparison
        self.play(
            *[FadeOut(mob) for mob in self.mobjects]
        )

        # Configuración del plano para el gráfico de Tiempo
        time_axes = Axes(
            x_range=[0, 550, 100],
            y_range=[0, 40, 10],
            axis_config={"include_tip": False},
            x_axis_config={"numbers_to_include": [0, 100, 200, 300, 400, 500]},
            y_axis_config={"numbers_to_include": np.arange(0, 41, 10)},
        ).scale(0.7)

        # Títulos y etiquetas para el gráfico de Tiempo
        time_title = Text("Execution Time Comparison").scale(0.8)
        time_title.to_edge(UP)
        time_x_label = Text("Number of Assets (n)", font_size=20)
        time_x_label.next_to(time_axes.x_axis, DOWN)
        time_y_label = Text("Time (s)", font_size=20).rotate(90 * DEGREES)
        time_y_label.next_to(time_axes.y_axis, LEFT)

        # Crear las líneas de datos para tiempo
        hc_time_points = [time_axes.coords_to_point(x, y) for x, y in zip(assets, hc_time)]
        sa_time_points = [time_axes.coords_to_point(x, y) for x, y in zip(assets, sa_time)]
        
        hc_time_line = VMobject()
        hc_time_line.set_points_smoothly(hc_time_points)
        hc_time_line.set_color(BLUE)
        
        sa_time_line = VMobject()
        sa_time_line.set_points_smoothly(sa_time_points)
        sa_time_line.set_color(GREEN)

        # Animación del segundo gráfico
        self.play(Write(time_title), run_time=1)  # 2 segundos
        self.play(Create(time_axes), Write(time_x_label), Write(time_y_label), run_time=5)  # 3 segundos
        self.play(Create(hc_time_line), Create(sa_time_line), run_time=5)  # 3 segundos
        self.play(FadeIn(legend), run_time=2)  # 2 segundos
        self.wait(2)

        # Conclusiones
        conclusion = VGroup(
            Text("Hill Climbing:", color=BLUE, font_size=24),
            Text("Faster but lower fitness", font_size=20),
            Text("Simulated Annealing:", color=GREEN, font_size=24),
            Text("Better fitness but slower", font_size=20)
        ).arrange(DOWN, aligned_edge=LEFT)
        conclusion.to_edge(LEFT)
        
        self.play(
            *[FadeOut(mob) for mob in self.mobjects],
            FadeIn(conclusion)
        )
        self.wait(2)

# Para ejecutar:
# manim -pql portfolio_optimization.py OptimizationComparison