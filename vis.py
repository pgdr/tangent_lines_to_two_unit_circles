from manim import *
import numpy as np

config.frame_width = 12
config.frame_height = 8


class Tangent(MovingCameraScene):
    def construct(self):
        self.camera.frame.move_to(np.array([1.75, 1.25, 0.0]))
        d = 5

        c1 = np.array([0, 0, 0])
        c2 = np.array([d, 0, 0])
        mid = np.array([d / 2, 0, 0])

        theta = np.arccos(2 / d)
        tp = np.array([np.cos(theta), np.sin(theta), 0])
        tp_other = np.array([d - np.cos(theta), -np.sin(theta), 0])

        circle1 = Circle(radius=1).move_to(c1)
        circle2 = Circle(radius=1).move_to(c2)
        center_line = Line(c1, c2)

        dot1 = Dot(c1, color=YELLOW)
        dot2 = Dot(c2, color=YELLOW)

        hyp = Line(c1, mid, color=YELLOW)
        radius_to_tangent = Line(c1, tp, color=YELLOW)
        tangent_to_mid = Line(tp, mid, color=BLUE)
        tangent_to_mid_yellow = Line(tp, mid, color=YELLOW)

        full_tangent = Line(tp, tp_other, color=BLUE)

        midpoint_dot = Dot(mid, color=RED)
        tangent_dot = Dot(tp, color=YELLOW)
        tangent_point = (
            MathTex(r"p", color=BLUE)
            .scale(0.5)
            .move_to(tp + np.array([0.2, 0.2, 0]))
        )

        angle = Angle(
            center_line, radius_to_tangent, radius=0.4, color=GREEN
        )

        text = MathTex(r"\theta").scale(0.5)
        theta_label = text.move_to((0.5, 0.25, 0))

        right_angle = RightAngle(
            radius_to_tangent,
            tangent_to_mid,
            length=0.15,
            quadrant=(-1, 1),
        )

        a_label = (
            MathTex(r"a=1")
            .scale(0.5)
            .next_to(radius_to_tangent.get_center(), LEFT, buff=0.15)
        )

        d_label = (
            MathTex(r"d").scale(0.5).move_to(np.array([d / 2, -2, 0]))
        )

        h_brace = BraceBetweenPoints(
            np.array([0, -1, 0]),
            np.array([d, -1, 0]),
            direction=DOWN,
        )
        h_label = (
            MathTex(r"h=d/2")
            .scale(0.5)
            .next_to(hyp.get_center(), DOWN, buff=0.15)
        )

        text_soh = (
            MathTex(
                r"\text{soc-\textbf{cah}-toa}: \quad\quad"
                + r"\cos \theta =\frac{a}{h}=\frac{1}{d/2}=\frac{2}{d}"
            )
            .scale(0.5)
            .move_to(np.array([0, 4, 0]))
        )
        text_eq_2 = (
            MathTex(r"\sin^2 \theta = 1 - \cos^2 \theta = 1 - 4/d^2")
            .scale(0.5)
            .move_to(np.array([1.35, 3.5, 0]))
        )
        text_eq_3 = (
            MathTex(r"\sin \theta = \sqrt{d^2-4}/d")
            .scale(0.5)
            .move_to(np.array([0.87, 3, 0]))
        )
        text_p = (
            MathTex(
                r"p = (\cos \theta, \sin \theta) = \left(\frac 2d, \frac{\sqrt{d^2 - 4}}{d}\right)"
            )
            .scale(0.5)
            .next_to(tangent_point, RIGHT + UP)
        )

        self.play(
            Create(dot1),
            Create(dot2),
            FadeIn(h_brace),
            Write(d_label),
        )
        self.play(Create(circle1), Create(circle2))
        self.play(Create(full_tangent))

        self.play(Create(center_line))

        self.play(FadeIn(midpoint_dot))

        self.play(Create(radius_to_tangent), Create(tangent_dot))
        self.play(Write(tangent_point))

        self.play(Create(tangent_to_mid_yellow), Create(hyp))

        self.play(
            Create(angle), Write(theta_label), Create(right_angle)
        )
        self.play(Write(a_label))

        self.play(Write(h_label))

        self.play(Write(text_soh))
        self.play(Write(text_eq_2))
        self.play(Write(text_eq_3))
        self.play(Write(text_p))
        self.wait(5.0)
        self.play(FadeOut(*self.mobjects), run_time=2)
        self.wait()
