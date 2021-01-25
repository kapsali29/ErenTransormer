# EREN dataset translation scripts

This is a series of scripts for translating categorical values from spanish to english
This repository contains the following files:

1. **DATA/**: In this folder all the source files sould be placed
2. **requirements.txt**: This file contains all the library requirements for running the translation
3. **settings.py**: Contains all the value mappings from spanish to english
4. **transformer.py**: This is the execution script of the EREN dataset translation

### Steps for using the script

1. Create **DATA** repository and download the following files
  + [Regional Administration Consumer centers](https://analisis.datosabiertos.jcyl.es/explore/dataset/centros-de-consumo-energetico-de-la-administracion-autonoma-de-castilla-y-leon/export/?disjunctive.organismo_consejeria&disjunctive.centro_gestor&disjunctive.tipo_de_centro_de_consumo)
1. Put the EREN datasets to **DATA/** directory
2. Execute this command for installing python requirements: `pip install -r requirements.txt`
3. Execute this script: `python transformer.py`

The translated datasets will be generated to the **OUTPUT/** folder
