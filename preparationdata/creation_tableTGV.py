import pandas as pd
import os

def creation_tableTGV():
    """Création de la table des trajets TGV.
    A faire en deux étapes ?

    Returns
    -------
    dataframe
        Avec les colonnes Gare Origine, Gare origine - code UIC, Destination,
        Gare destination - code UIC, Prix
    """
    # os.path.join("preparationdata/data","tarifs-tgv-inoui-ouigo.csv")
    tableTGV = pd.read_csv(os.path.join("preparationdata/data","tarifs-tgv-inoui-ouigo.csv"),sep=";",
                             dtype={'Gare origine - code UIC': str,'Gare destination - code UIC': str,
                                    'Classe': str})
    tableTGV.columns = [c.replace(' ','_') for c in tableTGV.columns]
    
    tableTGV = tableTGV.rename(columns = {"Transporteur" : "transporteur",
                                          "Gare_origine" : "origine",
                                          "Gare_origine_-_code_UIC" : "code_origine",
                                          "Destination" : "destination",
                                          "Gare_destination_-_code_UIC" : "code_destination",
                                          "Classe" : "classe",
                                          "Profil_tarifaire" : "tarif_profil",
                                          })
        
        # df = df [["origine","code_origine","destination","code_destination","prix"]]
        
    tableTGV['type'] = 'TGV'
    
    # par défaut on prned le prix min
    tableTGV['prix']=tableTGV['Prix_minimum']

    
    return(tableTGV)