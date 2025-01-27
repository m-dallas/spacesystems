from astropy import units as u
from astropy import constants as const
import numpy as np
from .eccentricity import eccentricity

def semi_major_axis(apoapsis_radius, periapsis_radius):
    """Returns semi-major axis "a" of an elliptical orbit.

    Parameters
    ----------
    apoapsis_radius : astropy.units.quantity.Quantity
        Distance from center of host body to apoapsis (nominally in meters)

    periapsis_radius : astropy.units.quantity.Quantity
         Distance from center of host body to periapsis (nominally in meters)

    Returns
    -------
    a : semi-major axis
        semi-major axis of elliptical orbit in meters

    Raises
    ------
    AssertionError:
        One or more of the inputs are not in units of length

    """
    
    # Check input are distances
    assert apoapsis_radius.unit.is_equivalent(u.m)
    assert periapsis_radius.unit.is_equivalent(u.m)

    # Convert to meters for consistency
    apoapsis_radius = apoapsis_radius.to(u.m)
    periapsis_radius = periapsis_radius.to(u.m)

    a = (periapsis_radius+apoapsis_radius)/2
    return a

def semi_minor_axis(apoapsis_radius, periapsis_radius):
    """Returns semi-minor axis "b" of an elliptical orbit.

    Parameters
    ----------
    apoapsis_radius : astropy.units.quantity.Quantity
        Distance from center of host body to apoapsis (nominally in meters)

    periapsis_radius : astropy.units.quantity.Quantity
         Distance from center of host body to periapsis (nominally in meters)

    Returns
    -------
    b : semi-minor axis
        semi-minor axis of elliptical orbit in meters

    Raises
    ------
    AssertionError:
        One or more of the inputs are not in units of length

    """

    # Check input are distances
    assert apoapsis_radius.unit.is_equivalent(u.m)
    assert periapsis_radius.unit.is_equivalent(u.m)

    # Convert to meters for consistency
    apoapsis_radius = apoapsis_radius.to(u.m)
    periapsis_radius = periapsis_radius.to(u.m)
    
    a = semi_major_axis(apoapsis_radius, periapsis_radius)
    e = eccentricity(apoapsis_radius, periapsis_radius)

    b = a*(np.sqrt((1-(e**2))))
    return b