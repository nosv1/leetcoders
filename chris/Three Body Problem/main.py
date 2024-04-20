from __future__ import annotations
from itertools import combinations
import numpy as np
import math as m
import matplotlib.pyplot as plt

# https://youtu.be/6GfIDwwxfsM?si=45eUr7oIbdcRxskT&t=439

# Three Body Problem ... point mass simulation with n masses


class Vector(np.ndarray):
    def __new__(cls, x: float, y: float, z: float):
        obj = np.array([x, y, z], dtype=float).view(cls)
        return obj

    @property
    def x(self) -> float:
        return self[0]

    @property
    def y(self) -> float:
        return self[1]

    @property
    def z(self) -> float:
        return self[2]

    def distance(self, other: Vector) -> float:
        return np.linalg.norm(self - other)

    def to_other(self, other: Vector) -> Vector:
        return other - self

    def normalize(self) -> Vector:
        return self / np.linalg.norm(self)


class PointMass:
    def __init__(
        self,
        name: str,
        mass: float,
        position: Vector,
        velocity: Vector,
        acceleration: Vector,
    ):
        self.name = name
        self.mass = mass  # in kg
        self.position = position  # in m
        self.velocity = velocity  # in m/s
        self.acceleration = acceleration  # in m/s^2

        self.forces_to_apply: list[Vector] = []
        self.color = np.random.uniform(0.1, 0.3, size=3)
        self.positions: np.ndarray = np.array([self.position])

    def calculate_force_to_apply(self, other: PointMass, dt: float) -> Vector:
        # F = G * m1 * m2 / r^2
        G = 6.67430e-11  # in
        r = self.position.distance(other.position)
        force = G * self.mass * other.mass / r**2  # in N
        direction = self.position.to_other(other.position).normalize()
        return force * direction

    def apply_force(self, force: Vector, dt: float) -> Vector:
        # F = ma
        acceleration = force / self.mass
        self.acceleration += acceleration
        self.velocity += self.acceleration * dt
        self.position += self.velocity * dt
        return self.position


class Simulation:
    def __init__(self, point_masses: list[PointMass], dt: float = 1.0):
        self.point_masses = point_masses
        self.dt = dt

        self.time = 0
        self.point_mass_combinations = list(combinations(self.point_masses, 2))
        self.fig = plt.figure()
        self.ax: plt.Axes = self.fig.add_subplot(111, projection="3d")
        # self.ax.set_xlim(-1e5, 1e5)
        # self.ax.set_ylim(-1e5, 1e5)

        for point_mass in self.point_masses:
            self.plot_point_mass(point_mass)
        self.ax.set_title("Time: 0")
        self.ax.set_xlim(1000)
        self.ax.set_ylim(1000)
        plt.pause(0.01)

    def plot_point_mass(self, point_mass: PointMass):
        self.ax.text(
            point_mass.position.x,
            point_mass.position.y,
            point_mass.position.z,
            f"{point_mass.name} ({point_mass.mass} kg)\n"
            f"Position: ({point_mass.position.x:0.2f}, {point_mass.position.y:0.2f}, {point_mass.position.z:0.2f})\n"
            f"Velocity: ({point_mass.velocity.x:0.2f}, {point_mass.velocity.y:0.2f}, {point_mass.velocity.z:0.2f})\n",
            va="center",
            ha="center",
        )
        self.ax.scatter(
            point_mass.position.x,
            point_mass.position.y,
            point_mass.position.z,
            color=point_mass.color,
        )

    def plot_trajectory(self, point_mass: PointMass):
        self.ax.plot(
            point_mass.positions[:, 0],
            point_mass.positions[:, 1],
            point_mass.positions[:, 2],
            color=point_mass.color,
        )

    def run(self):
        while True:
            for point_mass1, point_mass2 in self.point_mass_combinations:
                force = point_mass1.calculate_force_to_apply(point_mass2, self.dt)
                point_mass1.forces_to_apply.append(force)
                point_mass2.forces_to_apply.append(-force)

            for point_mass in self.point_masses:
                for force in point_mass.forces_to_apply:
                    point_mass.apply_force(force, self.dt)
                point_mass.positions = np.append(
                    point_mass.positions, [point_mass.position], axis=0
                )
                point_mass.forces_to_apply = []
                if (self.time % 50000) == 0:
                    self.plot_point_mass(point_mass)
                    self.plot_trajectory(point_mass)

            self.time += self.dt
            if (self.time % 50000) == 0:
                self.ax.set_title(f"Time: {self.time}")
                plt.pause(0.01)
                self.ax.clear()


if __name__ == "__main__":
    point_masses: list[PointMass] = [
        PointMass(
            name="big",
            mass=10000000000,
            position=Vector(0.0, 0.0, 0.0),
            velocity=Vector(0.0, 0.0, 0.0),
            acceleration=Vector(0.0, 0.0, 0.0),
        ),
        PointMass(
            name="small",
            mass=1000,
            position=Vector(700000, 0.0, 0.0),
            velocity=Vector(0.0, -0.1, 0.0),
            acceleration=Vector(0.0, 0.0, 0.0),
        ),
        # PointMass(
        #     name="small2",
        #     mass=1000,
        #     position=Vector(0.0, 1000, 0.0),
        #     velocity=Vector(5.5, 0.0, 0.0),
        #     acceleration=Vector(0.0, 0.0, 0.0),
        # ),
    ]

    sim = Simulation(
        point_masses=point_masses,
        # dt=1,  # 1 second
        # dt=10,  # 10 seconds
        dt=100,  # 100 seconds
        # dt=1000,  # 1000 seconsds
        # dt=10000,  # 10000 seconds
        # dt=31449600,  # 1 year
    )
    sim.run()
