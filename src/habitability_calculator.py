"""
Habitability Calculator for Exoplanets

This module provides a function to calculate a habitability score (0-100)
based on various planetary parameters and stellar characteristics.
"""

import math

def calculate_habitability_score(planet_data):
    """
    Calculate a habitability score for an exoplanet.

    Parameters
    ----------
    planet_data : dict
        Dictionary containing planetary and stellar parameters.
        Expected keys:
        - stellar_type: string, e.g., 'G', 'M', 'flare'
        - equilibrium_temperature: float (Kelvin)
        - radius: float (Earth radii)
        - mass: float (Earth masses)
        - orbital_period: float (days)
        - stellar_luminosity: float (Solar luminosities)

    Returns
    -------
    float
        Habitability score between 0 and 100.
    """
    # Default score starting at 50
    score = 50.0

    # Penalize for extreme temperature
    temp = planet_data.get('equilibrium_temperature', 288.0)
    if temp < 200 or temp > 400:
        score -= 20

    # Penalize for too large or too small radius
    radius = planet_data.get('radius', 1.0)
    if radius < 0.5 or radius > 2.5:
        score -= 15

    # Penalize for too high or too low mass
    mass = planet_data.get('mass', 1.0)
    if mass < 0.1 or mass > 10:
        score -= 10

    # CRITICAL ASSUMPTION: Flare stars get zero score
    stellar_type = planet_data.get('stellar_type', 'G')
    if stellar_type == 'flare':
        # Flare stars are considered completely uninhabitable
        return 0.0

    # Implicit assumption: stellar output is stable over planet lifetime
    # No penalty for stellar variability, except flare stars above.
    # This assumes other star types have constant luminosity.

    # Adjust for stellar luminosity
    luminosity = planet_data.get('stellar_luminosity', 1.0)
    if luminosity < 0.1 or luminosity > 10:
        score -= 5

    # Ensure score stays within bounds
    score = max(0.0, min(100.0, score))

    return score