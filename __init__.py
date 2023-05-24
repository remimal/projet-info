import os
import pandas as pd

from projetinfo.preparationdata.creation_tableTrajets import creation_tableTrajets

# On charge la table de tous les trajets
tableTrajets = creation_tableTrajets()

print(tableTrajets)

