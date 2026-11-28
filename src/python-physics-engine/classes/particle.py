import numpy as np
import numpy.typing as npt

Scalar = float | np.float64
Vector = list[float | np.float64] | npt.NDArray[np.float64]

class Particle:
  def __init__(
    self,
    pos: Vector | None = None,
    vel: Vector | None = None,
    accel: Vector | None = None,
    mass: Scalar | None = None
  ):
    self.pos = np.zeros(2) if pos is None else np.array(pos, dtype=np.float64)
    self.vel = np.zeros(2) if vel is None else np.array(vel, dtype=np.float64)
    self.accel = np.zeros(2) if accel is None else np.array(accel, dtype=np.float64)
    self.mass = np.float64(0) if mass is None else np.float64(mass)

    self.app_force = np.zeros(2)

  @property
  def inv_mass(self) -> np.float64:
    return self.mass if self.mass == 0 else 1/self.mass

  def tick(self):
    self.pos += self.vel
    self.vel += self.accel
    self.accel = self.app_force * self.inv_mass

if __name__ == "__main__":
  p = Particle(mass=2)
  print(p.inv_mass)