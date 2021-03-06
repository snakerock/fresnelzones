import fresnel_spiral
import matplotlib.pyplot as plot
from numpy import arange

lowest = 0.0001
highest = 0.05
default = 0.01
step = 0.001


def show(model):
    hole_radiuses = arange(lowest, highest, step)
    current_hole_radius = model.hole_radius
    intensities = []
    for radius in hole_radiuses:
        model.hole_radius = radius
        intensities.append(model.calculate_intensity())
        print(highest - radius)

    zone_radiuses = []
    zone_radius = 0
    n = 0
    while zone_radius < highest:
        zone_radiuses.append(zone_radius)
        zone_radius = model.get_zone_outer_radius(n)
        n += 1

    model.hole_radius = current_hole_radius
    figure = plot.figure(1)
    plot.subplots_adjust(left=0.15, bottom=0.3)
    plot.subplot2grid((1, 3), (0, 0), colspan=2)

    plot.title('Зависимость интенсивности от радиуса отверстия')
    plot.xlabel('Радиус отверстия (мм)')
    plot.ylabel('Интенсивность (Вт/м2)')
    plot.grid(True)

    print(len(zone_radiuses))
    for zone_radius in zone_radiuses:
        plot.axvline(zone_radius, 0, model.initial_intensity, color='r')

    plot.plot(hole_radiuses, intensities, linewidth=2)

    intensities = []
    for radius in hole_radiuses:
        model.hole_radius = radius
        intensities.append(model.calculate_intensity(False))
        print(highest - radius)

    plot.plot(hole_radiuses, intensities, linewidth=2, color='g')
    fresnel_spiral.show(model)

    model.draw(figure)