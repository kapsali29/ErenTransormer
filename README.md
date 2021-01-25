# EREN dataset translation scripts

This is a series of scripts for translating categorical values from spanish to english
This repository contains the following files:


1. **DATA/**: In this folder all the source files sould be placed
2. **requirements.txt**: This file contains all the library requirements for running the translation
3. **settings.py**: Contains all the value mappings from spanish to english
4. **transformer.py**: This is the execution script of the EREN dataset translation

### Prerequisites

1. Have Python 3.7 installed
2. Install python requirements `pip install -r requirements.txt`

### Steps for using the script

1. Create **DATA** repository and download the following files and put them in DATA folder:
   + [Regional Administration Consumer centers](https://analisis.datosabiertos.jcyl.es/explore/dataset/centros-de-consumo-energetico-de-la-administracion-autonoma-de-castilla-y-leon/export/?disjunctive.organismo_consejeria&disjunctive.centro_gestor&disjunctive.tipo_de_centro_de_consumo) name this file as `centros-de-consumo-energetico-de-la-administracion-autonoma-de-castilla-y-leon.csv`
   + [Electricity consumption of the Regional Administration buildings](https://analisis.datosabiertos.jcyl.es/explore/dataset/consumo-de-electricidad-en-centros-de-la-administracion-autonomica-de-castilla-y/export/?disjunctive.tipo_de_punto_de_medida) name this file as `consumo-de-electricidad-en-centros-de-la-administracion-autonomica-de-castilla-y.csv`
   + [Natural gas consumption of the Regional Administration buildings](https://analisis.datosabiertos.jcyl.es/explore/dataset/consumo-de-gas-en-centros-de-la-administracion-autonomica-de-castilla-y-leon/export/) name this file as `consumo-de-gas-en-centros-de-la-administracion-autonomica-de-castilla-y-leon.csv`
   + [Diesel consumption in education, health and culture centres of the Regional Administration of Castilla y León](https://analisis.datosabiertos.jcyl.es/explore/dataset/consumo-de-gasoil-en-centros-de-educacion-y-sanidad-de-la-administracion-autonom/export/) name this file as `consumo-de-gasoil-en-centros-de-educacion-y-sanidad-de-la-administracion-autonom.csv`
   + [Energy efficiency certificates](https://analisis.datosabiertos.jcyl.es/explore/dataset/certificados-de-eficiencia-energetica/export/?location=10,41.15005,-2.43043&basemap=jawg.streets) name this file as `certificados-de-eficiencia-energetica.csv`
   + [Hourly electricity consumption in hospitals](https://analisis.datosabiertos.jcyl.es/explore/dataset/consumos-horarios-en-hospitales/export/?disjunctive.ano) name this file as `consumos-horarios-en-hospitales.csv`
1. Put the EREN datasets to **DATA/** directory
2. Execute this command for installing python requirements: `pip install -r requirements.txt`
3. Execute this script: `python transformer.py`

The translated datasets will be generated to the **OUTPUT/** folder
