from astropy import units as u
from astropy import constants as const
import numpy as np

def eccentricity(apoapsis_radius, periapsis_radius):
    """Returns eccentricity "e" of an elliptical orbit.

    Parameters
    ----------
    apoapsis_radius : astropy.units.quantity.Quantity
        Distance from center of host body to apoapsis (nominally in meters)

    periapsis_radius : astropy.units.quantity.Quantity
         Distance from center of host body to periapsis (nominally in meters)

    Returns
    -------
    e : eccentricity
        Dimensionless eccentricity parameter e.

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
    
    e = 1-(2/((apoapsis_radius/periapsis_radius)+1))
    return e