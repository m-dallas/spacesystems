from astropy import units as u
from astropy import constants as const
import numpy as np

def apoapsis_velocity(M, e, a):
    """Returns orbital velocity at apoapsis of an elliptical orbit.

    Parameters
    ----------
    M : astropy.units.quantity.Quantity
        Mass of host body (nominally in kg)

    e : float
         eccentricity of elliptical orbit

    a : astropy.units.quantity.Quantity
         semi-major axis of elliptical orbit (nominally in meters)

    Returns
    -------
    v_ap : astropy.units.quantity.Quantity
        Orbital velocity at apoapsis in m/s

    Raises
    ------
    AssertionError:
        One or more of the inputs are not in the correct units

    """

    # Check inputs are in the correct units
    assert M.unit.is_equivalent(u.kg)
    assert e.unit.is_equivalent(u.dimensionless_unscaled) or e.unit is None
    assert a.unit.is_equivalent(u.m)

    # Convert to SI for consistency
    M = M.to(u.kg)
    a = a.to(u.m)
    
    v_ap = np.sqrt(((const.G*M)/(a)) * ((1-e)/(1+e)))
    return v_ap

def periapsis_velocity(M, e, a):
    """Returns orbital velocity at periapsis of an elliptical orbit.

    Parameters
    ----------
    M : astropy.units.quantity.Quantity
        Mass of host body (nominally in kg)

    e : float
         eccentricity of elliptical orbit

    a : astropy.units.quantity.Quantity
         semi-major axis of elliptical orbit (nominally in meters)

    Returns
    -------
    v_per : astropy.units.quantity.Quantity
        Orbital velocity at periapsis in m/s

    Raises
    ------
    AssertionError:
        One or more of the inputs are not in the correct units

    """

    # Check inputs are in the correct units
    assert M.unit.is_equivalent(u.kg)
    assert e.unit.is_equivalent(u.dimensionless_unscaled) or e.unit is None
    assert a.unit.is_equivalent(u.m)

    # Convert to SI for consistency
    M = M.to(u.kg)
    a = a.to(u.m)
    
    v_per = np.sqrt(((const.G*M)/(a)) * ((1+e)/(1-e)))
    return v_per