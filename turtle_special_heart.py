import turtle
import math
import random


# -----------------------------
# SCREEN SETUP
# -----------------------------

def setup_environment():
    screen = turtle.Screen()
    screen.bgcolor("#000000")
    screen.title("Ultimate Love ❤️")
    screen.setup(width=900, height=700)
    screen.tracer(0)
    return screen


# -----------------------------
# PARTICLE CLASS
# -----------------------------

class VortexParticle:

    def __init__(self):
        self.reset()
        self.history = [(self.x, self.y)] * 5

    def reset(self):

        self.x = random.uniform(-400, 400)
        self.y = random.uniform(-300, 300)

        self.vx = random.uniform(-2, 2)
        self.vy = random.uniform(-2, 2)

        self.color_base = random.uniform(0, 1)

        self.target_angle = random.uniform(
            0,
            2 * math.pi
        )

    def update(self, t, mouse_x, mouse_y):

        # Save particle history
        self.history.append((self.x, self.y))
        self.history.pop(0)

        # Heart size animation
        scale = 15 + 3 * math.sin(t * 0.03)

        # Heart equation
        heart_x = (
            16
            * math.sin(self.target_angle) ** 3
            * scale
        )

        heart_y = (
            13 * math.cos(self.target_angle)
            - 5 * math.cos(2 * self.target_angle)
            - 2 * math.cos(3 * self.target_angle)
            - math.cos(4 * self.target_angle)
        ) * scale

        # Direction toward heart
        dx = heart_x - self.x
        dy = heart_y - self.y

        dist = math.sqrt(dx ** 2 + dy ** 2)

        # Pull particle toward heart
        self.vx += dx * 0.002
        self.vy += dy * 0.002

        # Vortex movement
        self.vx += -dy * 0.001
        self.vy += dx * 0.001

        # Mouse interaction
        mouse_dx = mouse_x - self.x
        mouse_dy = mouse_y - self.y

        mouse_dist = math.sqrt(
            mouse_dx ** 2 + mouse_dy ** 2
        )

        if mouse_dist < 120 and mouse_dist > 0:

            force = (120 - mouse_dist) / 120

            self.vx -= mouse_dx * force * 0.01
            self.vy -= mouse_dy * force * 0.01

        # Limit speed
        speed = math.sqrt(
            self.vx ** 2 + self.vy ** 2
        )

        if speed > 8:

            self.vx = self.vx / speed * 8
            self.vy = self.vy / speed * 8

        # Move particle
        self.x += self.vx
        self.y += self.vy

        # Damping
        self.vx *= 0.98
        self.vy *= 0.98

        # Reset if particle goes too far
        if (
            abs(self.x) > 500
            or abs(self.y) > 400
        ):
            self.reset()


# -----------------------------
# DRAW PARTICLES
# -----------------------------

def draw_particle(particle, pen):

    pen.penup()

    pen.goto(
        particle.x,
        particle.y
    )

    pen.dot(
        4,
        "#ff1744"
    )


# -----------------------------
# MAIN PROGRAM
# -----------------------------

screen = setup_environment()

pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)

# Create particles
particles = []

for _ in range(250):

    particles.append(
        VortexParticle()
    )


# Mouse position
mouse_x = 0
mouse_y = 0


def mouse_move(x, y):

    global mouse_x
    global mouse_y

    mouse_x = x
    mouse_y = y


screen.getcanvas().bind(
    "<Motion>",
    lambda event: mouse_move(
        event.x - 450,
        350 - event.y
    )
)


# -----------------------------
# ANIMATION LOOP
# -----------------------------

def animate():

    pen.clear()

    current_time = 0

    for particle in particles:

        particle.update(
            current_time,
            mouse_x,
            mouse_y
        )

        draw_particle(
            particle,
            pen
        )

    screen.update()

    screen.ontimer(
        animate,
        16
    )


# Start animation
animate()

turtle.done()

