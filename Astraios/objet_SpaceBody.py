class SpaceBody():

    """Define a body enrolled in an orbit,
    it can be a planet, a star, a satellite or any kind of artificial or natural element
    """
    def __init__(self, mass=0):
        self.mass = mass


class Planet(SpaceBody):

    def __init__(self,mass, radius=0,color='b'):
        super().__init__(mass)
        self.radius = radius    # [m]
        self.color = color


class Satellite(SpaceBody):
    def __init__(self, mass, cross_surface, cx=2):
        super().__init__(mass)
        self.cx = cx                # [sans dimension]
        self.surface = cross_surface      # [m²]
