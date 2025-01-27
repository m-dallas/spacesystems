from astropy import units as u
from astropy import constants as const
import numpy as np

def period(M, a):
    """Returns orbital period in seconds.

    Parameters
    ----------
    M : astropy.units.quantity.Quantity
        Mass of host body (nominally in kg)

    a : astropy.units.quantity.Quantity
         semi-major axis of orbit (nominally in meters)

    Returns
    -------
    period : astropy.units.quantity.Quantity
        Orbital period in s

    Raises
    ------
    AssertionError:
        One or more of the inputs are not in the correct units

    """

    # Check inputs are in the correct units
    assert M.unit.is_equivalent(u.kg)
    assert a.unit.is_equivalent(u.m)

    # Convert to SI for consistency
    M = M.to(u.kg)
    a = a.to(u.m)
    
    period = (2*np.pi) * np.sqrt((a**3)/(const.G*M))
    return period