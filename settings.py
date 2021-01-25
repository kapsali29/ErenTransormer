##########################################
# Diesel consumption in education, health and culture centres of the Regional Administration
# of Castilla y LeónDiesel consumption in education,
# health and culture centres of the Regional Administration of Castilla y León
##########################################
DIESEL_CONSUMPTION_DATASET_COLUMNS = {
    'ORGANISMO / CONSEJERÍA': 'ORGANISM / COUNSIL',
    'CENTRO GESTOR': 'MANAGEMENT CENTER',
    'ID OPTE CENTRO DE GASTO': 'SPENDING CENTER ID',
    'CENTRO DE GASTO': 'SPENDING CENTER',
    'TIPO DE CENTRO DE CONSUMO': 'TYPE OF CONSUMER CENTER',
    'ID OPTE CENTRO DE CONSUMO': 'CONSUMER CENTER ID',
    'CENTRO DE CONSUMO': 'CONSUMER CENTER',
    'TIPO DE ENERGÍA': 'TYPE OF ENERGY',
    'AÑO': 'YEAR',
    'MES': 'MONTH',
    'CONSUMO MENSUAL TOTAL GSL (M3) Gasóleo A': 'TOTAL MONTHLY CONSUMPTION GSL (M3) Diesel A',
    'CONSUMO MENSUAL TOTAL GSL (M3) Gasóleo B': 'TOTAL MONTHLY CONSUMPTION GSL (M3) Diesel B',
    'CONSUMO MENSUAL TOTAL GSL (M3) Gasóleo C': 'TOTAL MONTHLY CONSUMPTION GSL (M3) Diesel C',
    'G.D. en Base 20': 'G.D. in Base 20',
    'G.D. en Base 26': 'G.D. in Base 26',
    'TIPO DE CENTRO A NIVEL DE ADMINISTRACIÓN AUTONÓMICA': 'TYPE OF CENTER AT THE REGIONAL ADMINISTRATION LEVEL',
    'CÓDIGO MUNICIPIO DIRECCIÓN': 'MUNICIPAL CODE ADDRESS',
    'MUNICIPIO DIRECCIÓN': 'MUNICIPALITY ADDRESS',
    'COORDENADA X LONGITUD': 'COORDINATE X LENGTH',
    'COORDENADA Y LATITUD': 'COORDINATE Y LATITUDE',
    'POSICIÓN': 'POSITION',
    'FECHA': 'DATE'
}

DIESEL_CONSUMPTION_DATASET_COLUMN_VALUES = {
    'ORGANISMO / CONSEJERÍA': {
        '05 - SANIDAD': '05 - HEALTH',
        '07 - EDUCACIÓN': '07 - EDUCATION',
        '08 - EMPLEO E INDUSTRIA': '08 - EMPLOYMENT AND INDUSTRY',
        '10 - CULTURA Y TURISMO': '10 - CULTURE AND TOURISM'
    },
    'CENTRO GESTOR': {
        '0702 - D.G. CENTROS, PLANI, ORD EDUCA': '0702 - DG CENTROS, PLANI, ORD EDUCA',
        '0524 - GRS (GAP)': '0524 - GRS (GAP)',
        '1003 - CULTURA Y TURISMO': '1003 - CULTURE AND TOURISM',
        '0522 - GRS(GAE)': '0522 - GRS (GAE)',
        '0523 - GRS (GSA)': '0523 - GRS (GSA)',
        '0701 - S. G. EDUCACION': '0701 - SG EDUCATION',
        '0801 - SG EMPLEO': '0801 - SG EMPLOYMENT'
    },
    'TIPO DE CENTRO A NIVEL DE ADMINISTRACIÓN AUTONÓMICA': {
        'C. EDUCATIVOS': 'C. EDUCATIONAL',
        'CENTROS DE SALUD': 'HEALTH CENTERS',
        'MUSEO': 'MUSEUM',
        'HOSPITALES': 'HOSPITALS',
        'C. ADMINISTRATIVOS': 'C. ADMINISTRATIVE',
        'OTROS': 'OTHERS',
        'BIBLIOTECA': 'LIBRARY',
        'RESIDENCIA': 'HOME'
    },
    'TIPO DE ENERGÍA': {
        'GASÓLEO': 'DIESEL OIL'
    },
    'TIPO DE CENTRO DE CONSUMO': {
        'ADMINISTRATIVO': 'ADMINISTRATIVE',
        'CENTRO DE SALUD CON URGENCIAS': 'EMERGENCY HEALTH CENTER',
        'HOSPITAL CON MAS DE 300 CAMAS': 'HOSPITAL WITH MORE THAN 300 BEDS',
        'HOSPITAL CON MENOS DE 300 CAMAS': 'HOSPITAL WITH LESS THAN 300 BEDS',
        'CENTRO DE SALUD SIN URGENCIAS': 'HEALTH CENTER WITHOUT EMERGENCIES',
        'ALMACÉN, LOCAL, RESTO': 'WAREHOUSE, LOCAL, REST',
        'OTRO TIPO DE CENTRO': 'ANOTHER KIND OF CENTER',
        'EDIFICIO ADMINISTRATIVO': 'ADMINISTRATIVE BUILDING',
        'INSTITUTO DE EDUCACION SECUNDARIA': 'INSTITUTE OF SECONDARY EDUCATION',
        'ESCUELA DE ARTE': 'ART SCHOOL',
        'INSTITUTO DE EDUCACION SECUNDARIA OBLIGATORIA': 'INSTITUTE OF COMPULSORY SECONDARY EDUCATION',
        'CIFP': 'CIFP',
        'CONSERVATORIO DE MÚSICA': 'CONSERVATORY OF MUSIC',
        'ESCUELA OFICIAL DE IDIOMAS': 'OFFICIAL SCHOOL OF LANGUAGES',
        'CENTRO DE FORMACIÓN DEL PROFESORADO E INNOVACIÓN EDUCATIVA': 'TEACHER TRAINING AND EDUCATIONAL INNOVATION CENTER',
        'ESCUELA HOGAR': 'HOME SCHOOL',
        'CENTRO RURAL DE INNOVACION EDUCATIVA': 'RURAL CENTER OF EDUCATIONAL INNOVATION',
        'COLEGIO DE EDUCACIÓN ESPECIAL': 'COLLEGE OF SPECIAL EDUCATION',
        'RESIDENCIA': 'HOME',
        'OFICINA': 'OFFICE',
        'ARCHIVO': 'ARCHIVE',
        'BIBLOTECA/FILMOTECA': 'LIBRARY / FILM LIBRARY',
        'MUSEO': 'MUSEUM',
        'FILIAL MUSEO': 'FILIAL MUSEUM',
        'DEPORTIVO': 'SPORTS'
    }
}

## - Electricity consumption of the Regional Administration buildings:

ELECTRICITY_CONSUMPTION_DATASET_COLUMNS = {
    'ORGANISMO / CONSEJERÍA': 'ORGANISM / COUNSIL',
    'CENTRO GESTOR': 'MANAGEMENT CENTER',
    'ID OPTE CENTRO DE GASTO': 'SPENDING CENTER ID',
    'CENTRO DE GASTO': 'SPENDING CENTER',
    'TIPO DE CENTRO DE CONSUMO': 'TYPE OF CONSUMER CENTER',
    'ID OPTE CENTRO DE CONSUMO': 'CONSUMER CENTER ID',
    'CENTRO DE CONSUMO': 'CONSUMER CENTER',
    'CUPS ELECTRICIDAD': 'ELECTRICITY CUPS',
    'DISTRIBUIDORA ELÉCTRICA': 'ELECTRIC DISTRIBUTOR',
    'TIPO DE ENERGÍA': 'TYPE OF ENERGY',
    'TIPO SUMINISTRO ELÉCTRICO': 'TYPE OF ELECTRICAL SUPPLY',
    'TARIFA ELÉCTRICA': 'ELECTRICITY TARIFF',
    'P1 (kW) POTENCIA CONTRATADA': 'P1 (kW) CONTRACTED POWER',
    'P2 (kW) POTENCIA CONTRATADA': 'P2 (kW) CONTRACTED POWER',
    'P3 (kW) POTENCIA CONTRATADA': 'P3 (kW) CONTRACTED POWER',
    'P4 (kW) POTENCIA CONTRATADA': 'P4 (kW) CONTRACTED POWER',
    'P5 (kW) POTENCIA CONTRATADA': 'P5 (kW) CONTRACTED POWER',
    'P6 (kW) POTENCIA CONTRATADA': 'P6 (kW) CONTRACTED POWER',
    'AÑO': 'YEAR',
    'MES': 'MONTH',
    'CONSUMO MENSUAL ENERGÍA ACTIVA TOTAL (kWh)': 'MONTHLY CONSUMPTION OF TOTAL ACTIVE ENERGY (kWh)',
    'G.D. en Base 20': 'G.D. in Base 20',
    'G.D. en Base 26': 'G.D. in Base 26',
    'TIPO DE CENTRO A NIVEL DE ADMINISTRACIÓN AUTONÓMICA': 'TYPE OF CENTER AT THE REGIONAL ADMINISTRATION LEVEL',
    'CÓDIGO MUNICIPIO DIRECCIÓN': 'MUNICIPAL CODE ADDRESS',
    'MUNICIPIO DIRECCIÓN': 'MUNICIPALITY ADDRESS',
    'COORDENADA X LONGITUD': 'COORDINATE X LENGTH',
    'COORDENADA Y LATITUD': 'COORDINATE Y LATITUDE',
    'POSICIÓN': 'POSITION',
    'FECHA': 'DATE',
    'TIPO DE PUNTO DE MEDIDA': 'TYPE OF MEASURING POINT'
}

ELECTRICITY_CONSUMPTION_DATASET_VALUES = {
    'ORGANISMO / CONSEJERÍA': {
        '07 - EDUCACIÓN': '07 - EDUCATION',
        '05 - SANIDAD': '05 - HEALTH',
        '04 - FOMENTO Y M. AMBIENTE': '04 - DEVELOPMENT AND ENVIRONMENT',
        '03 - AGRIC. Y G.': '03 - AGRIC. And G.',
        '09 - FAMILIA E IO (BIS)': '09 - FAMILY AND IO (BIS)',
        '10 - CULTURA Y TURISMO': '10 - CULTURE AND TOURISM',
        '08 - EMPLEO E INDUSTRIA': '08 - EMPLOYMENT AND INDUSTRY',
        '02 - ECONOMIA Y HACIENDA': '02 - ECONOMY AND FINANCE',
        '00 - FAMILIA E IGUAL.OPOR': '00 - FAMILY AND EQUAL.',
        '14 - PRESIDENCIA DE LAS CORTES CYL': '14 - PRESIDENCY OF THE COURTS CYL',
        '01 - DE LA PRESIDENCIA': '01 - FROM THE PRESIDENCY'
    },
    'CENTRO GESTOR': {
        '0702 - D.G. CENTROS, PLANI, ORD EDUCA': '0702 - D.G. CENTERS, PLANI, ORD EDUCA',
        '0401 - SG FOMENTO Y MEDIO AMBIENTE': '0401 - SG DEVELOPMENT AND ENVIRONMENT',
        '0524 - GRS (GAP)': '0524 - GRS (GAP)',
        '0301 - SG AGRICULTURA Y GANADERIA': '0301 - SG AGRICULTURE AND LIVESTOCK',
        '0921 - GERENCIA SERV.SOC.': '0921 - SERV.SOC MANAGEMENT.',
        '1003 - CULTURA Y TURISMO': '1003 - CULTURE AND TOURISM',
        '0823 - SERVIC.PÚBL.EMPLEO': '0823 - EMPLOYMENT PUBLIC SERVICE',
        '0410 - FUND PATRIMONIO NATURAL CYL': '0410 - NATURAL HERITAGE CYL FUND',
        '0522 - GRS(GAE)': '0522 - GRS (GAE)',
        '0821 - ICE': '0821 - ICE',
        '0201 - SG ECONOMIA Y HACIENDA': '0201 - SG ECONOMY AND FINANCE',
        '0501 - SG SANIDAD': '0501 - SG HEALTH',
        '0922 - INSTITUTO JUVENTUD': '0922 - YOUTH INSTITUTE',
        '0021 - GSS': '0021 - GSS',
        '0801 - SG EMPLEO': '0801 - SG EMPLOYMENT',
        '0701 - S. G. EDUCACION': '0701 - S. G. EDUCATION',
        '0523 - GRS (GSA)': '0523 - GRS (GSA)',
        '0321 - ITACYL': '0321 - ITACYL',
        '0302 - DG DE COMP IND AGR EMPR AGRAR': '0302 - DG DE COMP IND AGR EMPR AGRAR',
        '0525 - G.E. SANITARIAS': '0525 - G.E. SANITARY',
        '1400 - PRESIDENCIA DE LAS CORTES CYL': '1400 - PRESIDENCY OF THE CORTES CYL',
        '0103 - SG PRESIDENCIA': '0103 - SG PRESIDENCY',
        '0822 - ENTE REG.ENERGIA': '0822 - ENERGY REGISTRATION ENTITY',
        '0901 - SG FAMILIA': '0901 - SG FAMILY',
        '0022 - INSTI. JUVENTUD': '0022 - INSTI. YOUTH',
        '0304 - D G DE DESARROLLO RURAL': '0304 - D G OF RURAL DEVELOPMENT'
    },
    'TIPO DE PUNTO DE MEDIDA': {
        'PUNTO DE MEDIDA TIPO 2': 'TYPE 2 MEASUREMENT POINT',
        'PUNTO DE MEDIDA TIPO 3': 'TYPE 3 MEASUREMENT POINT',
        'PUNTO DE MEDIDA TIPO 4': 'TYPE 4 MEASUREMENT POINT',
        'PUNTO DE MEDIDA TIPO 5': 'TYPE 5 MEASUREMENT POINT'
    },
    'TIPO DE CENTRO A NIVEL DE ADMINISTRACIÓN AUTONÓMICA': {
        'C. EDUCATIVOS': 'C. EDUCATIONAL',
        'CENTROS DE SALUD': 'HEALTH CENTERS',
        'MUSEO': 'MUSEUM',
        'HOSPITALES': 'HOSPITALS',
        'C. ADMINISTRATIVOS': 'C. ADMINISTRATIVE',
        'OTROS': 'OTHERS',
        'BIBLIOTECA': 'LIBRARY',
        'RESIDENCIA': 'HOME',
        'C. ATENCIÓN SS': 'C. ATTENTION SS',
        'LABORATORIO': 'LABORATORY',
        'C. EDUCACIÓN INFANCIA': 'C. CHILDHOOD EDUCATION',
        'ALBERGUE': 'HOSTEL',
        'C. FORMACIÓN JCyL': 'C. JCyL TRAINING'
    },
    'TIPO DE ENERGÍA': {
        'ELECTRICIDAD': 'ELECTRICITY'
    },
    'TIPO SUMINISTRO ELÉCTRICO': {
        'Principal': 'Principal',
        'Duplicado': 'Duplicate',
        'Reserva': 'Reservation',
        'Socorro': 'Help'
    },
    'TIPO DE CENTRO DE CONSUMO': {
        'ADMINISTRATIVO': 'ADMINISTRATIVE',
        'EDIF. SERVICIOS': 'EDIF. SERVICES',
        'EDIFICIO ADMINISTRATIVO': 'ADMINISTRATIVE BUILDING',
        'SUMINISTRO INDUSTRIAL': 'INDUSTRIAL SUPPLY',
        'LABORATORIO': 'LABORATORY',
        'EDIFICIO ADMINISTRATIVO Y LABORATORIO': 'ADMINISTRATIVE AND LABORATORY BUILDING',
        'ALMACÉN Y VIVIENDAS': 'WAREHOUSE AND HOUSING',
        'CENTRO DE FORMACIÓN': 'TRAINING CENTER',
        'GARAJE': 'GARAGE',
        'GARAJE-ARCHIVO': 'GARAGE-FILE',
        'SILO': 'SILO',
        'UNIDAD DE ALMACENAMIENTO Y ADMINISTRACIÓN': 'STORAGE AND ADMINISTRATION UNIT',
        'VIVIENDA': 'HOUSING',
        'EDIFICIO PRÁCTICAS EDUCATIVAS': 'EDUCATIONAL PRACTICES BUILDING',
        'CASA DEL PARQUE': 'HOUSE OF THE PARK',
        'CENTRO DE RECEPCION DE AVES': 'CENTER FOR THE RECEPTION OF BIRDS',
        'ADMINISTRATIVO - EDUCACIÓN AMBIENTAL': 'ADMINISTRATIVE - ENVIRONMENTAL EDUCATION',
        'HOSPITAL CON MAS DE 300 CAMAS': 'HOSPITAL WITH MORE THAN 300 BEDS',
        'HOSPITAL CON MENOS DE 300 CAMAS': 'HOSPITAL WITH LESS THAN 300 BEDS',
        'CENTRO DE SALUD CON URGENCIAS': 'EMERGENCY HEALTH CENTER',
        'OTRO TIPO DE CENTRO': 'ANOTHER TYPE OF CENTER',
        'CENTRO DE SALUD SIN URGENCIAS': 'HEALTH CENTER WITHOUT EMERGENCIES',
        'PISO': 'FLAT',
        'ALMACÉN, LOCAL, RESTO' 'ESCUELA': 'WAREHOUSE, LOCAL, REST, SCHOOL',
        'INSTITUTO DE EDUCACION SECUNDARIA': 'INSTITUTE OF SECONDARY EDUCATION',
        'INSTITUTO DE EDUCACION SECUNDARIA OBLIGATORIA': 'INSTITUTE OF COMPULSORY SECONDARY EDUCATION',
        'COLEGIO DE EDUCACIÓN ESPECIAL': 'COLLEGE OF SPECIAL EDUCATION',
        'CENTRO DE FORMACIÓN DEL PROFESORADO E INNOVACIÓN EDUCATIVA': 'TEACHER TRAINING AND EDUCATIONAL INNOVATION CENTER',
        'CENTRO RURAL DE INNOVACION EDUCATIVA': 'RURAL CENTER OF EDUCATIONAL INNOVATION',
        'CIFP': 'CIFP',
        'CONSERVATORIO DE MÚSICA': 'CONSERVATORY OF MUSIC',
        'ESCUELA DE ARTE': 'SCHOOL OF ART',
        'ESCUELA OFICIAL DE IDIOMAS': 'OFFICIAL LANGUAGE SCHOOL',
        'FORMACIÓN': 'TRAINING',
        'EDIF. ADMINISTRATIVO': 'EDIF. ADMINISTRATIVE',
        'UNIDAD DE INTERVENCIÓN EDUCATIVA': 'EDUCATIONAL INTERVENTION UNIT',
        'CENTRO DE DÍA PARA LA ATENCIÓN DE PERSONAS MAYORES': 'DAY CENTER FOR THE CARE OF ELDERLY PEOPLE',
        'CENTRO DE ATENCIÓN A LA INFANCIA': 'CHILD CARE CENTER',
        'CENTRO DE ATENCIÓN A MINUSVÁLIDOS PSÍQUICOS': 'CENTER OF ATTENTION TO THE PSYCHIC DISABLED',
        'CENTRO DE ATENCIÓN A MINUSVÁLIDOS PSÍQUICOS Y CENTRO OCUPACIONAL': 'CENTER OF ATTENTION TO THE PSYCHIC DISABLED AND OCCUPATIONAL CENTER',
        'SERVICIOS ADMINISTRATIVOS': 'ADMINISTRATIVE SERVICES',
        'CENTRO BASE DE ATENCIÓN A  PERSONAS CON DISCAPACIDAD': 'BASE CENTER OF ATTENTION TO PEOPLE WITH DISABILITIES',
        'COMEDOR SOCIAL': 'SOCIAL DINING ROOM',
        'CENTRO OCUPACIONAL': 'OCCUPATIONAL CENTER',
        'CENTRO DE EDUCACIÓN INFANTIL': 'CHILDREN EDUCATION CENTER',
        'VIVIENDA TUTELADA PARA PERSONAS CON DISCAPACIDAD': 'TUTELED HOUSING FOR PEOPLE WITH DISABILITIES',
        'RESIDENCIA DE PROTECCIÓN A LA INFANCIA': 'RESIDENCE FOR THE PROTECTION OF CHILDREN',
        'RESIDENCIA DE PERSONAS MAYORES': 'RESIDENCE FOR THE ELDERLY PEOPLE',
        'ALBERGUE JUVENIL': 'YOUTH HOSTEL',
        'CAMPAMENTO JUVENIL': 'YOUTH CAMP',
        'RESIDENCIA JUVENIL': 'YOUTH RESIDENCE',
        'ALMACÉN': 'WAREHOUSE',
        'RESIDENCIA': 'RESIDENCE',
        'OFICINA': 'OFFICE',
        'ARCHIVO': 'ARCHIVE',
        'MUSEO': 'MUSEUM',
        'BIBLOTECA/FILMOTECA': 'LIBRARY / FILM LIBRARY',
        'FILIAL MUSEO': 'FILIAL MUSEUM',
        'CENTRO PÚBLICO DE EDUCACIÓN DE PERSONAS ADULTAS': 'PUBLIC CENTER FOR EDUCATION OF ADULTS',
        'ESCUELA HOGAR': 'HOME SCHOOL',
        'CENTRO DE EDUACIÓN INFANTIL': 'CHILDREN EDUCATION CENTER',
        'BASE DE EMERGENCIAS': 'EMERGENCY BASE',
        'COCHERA': 'GARAGE',
        'INCENDIOS, RIEGOS, CENTRO CINEGÉTICO, EMISORA, TORRE VIGILANCIA': 'INCENDIOS, RIEGOS, CENTRO CINEGÉTICO, EMISORA, TORRE VIGILANCIA',
        'ESPACIO DIGITAL': 'DIGITAL SPACE',
        'ALUMBRADO PÚBLICO': 'PUBLIC LIGHTING',
        'NAVE': 'WAREHOUSE',
        'PARQUE MAQUINARIA': 'MACHINERY PARK',
        'OFICINAS': 'OFFICES',
        'REPETIDOR': 'REPEATER',
        'CASA FORESTAL': 'FOREST HOUSE',
        'HELIPUERTO': 'HELIPORT',
        'REFUGIO': 'REFUGE',
        'EDIFICIO CALEFACTADO': 'HEATED BUILDING',
        'PISCIFACTORIA': 'FISH FARM',
        'VIVERO': 'NURSERY',
        'ANTENA': 'ANTENNA',
        'BÁSCULA': 'SCALE',
        'CENTRO FORESTAL': 'FOREST CENTER',
        'DEPORTIVO': 'SPORTS',
        'LOCAL': 'LOCAL',
        'OTROS': 'OTHERS',
        'DELEGACION TERRITORIAL': 'TERRITORIAL DELEGATION',
        'EDF. ADMINISTRATIVO': 'EDF. ADMINISTRATIVE',
        'LABORATORIOS DE METROLOGIA': 'METROLOGY LABORATORIES',
        'ALUMBRADO PUBLICO VAPOR SODIO ALTA PRESION + HALOGENURO METALICO': 'PUBLIC LIGHTING HIGH PRESSURE SODIUM VAPOR + METALLIC HALOGENIDE',
        'ALUMBRADO PUBLICO VAPOR SODIO ALTA PRESION + VAPOR MERCURIO': 'PUBLIC LIGHTING HIGH PRESSURE SODIUM VAPOR + MERCURY VAPOR',
        'ALUMBRADO PUBLICO VAPOR SODIO ALTA PRESION': 'PUBLIC LIGHTING HIGH PRESSURE SODIUM VAPOR',
        'ARCHIVO CENTRAL, ARCHIVO ALMACEN': 'CENTRAL FILE, WAREHOUSE FILE',
        'ALUMBRADO EXTERIOR': 'EXTERIOR LIGHTING',
        'LABORATORIO Y CENTRO DE FORMACIÓN': 'LABORATORY AND TRAINING CENTER',
        'CENTRO DE FORMACIÓN / LABORATORIOS': 'TRAINING CENTER / LABORATORIES',
        'PRESA': 'DAM',
        'LABORATORIO/PLANTA INDUSTRIAL': 'LABORATORY / INDUSTRIAL PLANT',
        'OFICINAS/LABORATORIO/NAVES': 'OFFICES / LABORATORY / WAREHOUSES',
        'RIEGOS': 'IRRIGATIONS'
    }
}

# - Hourly hospitals electricity consumption:

HOURLY_HOSPITAL_ENERGY_CONSUMPTION_COLUMNS = {
    'ORGANISMO / CONSEJERÍA': 'ORGANISM / COUNSIL',
    'CENTRO GESTOR': 'MANAGEMENT CENTER',
    'ID OPTE CENTRO DE GASTO': 'SPENDING CENTER ID',
    'CENTRO DE GASTO': 'SPENDING CENTER',
    'TIPO DE CENTRO DE CONSUMO': 'TYPE OF CONSUMER CENTER',
    'ID OPTE CENTRO DE CONSUMO': 'CONSUMER CENTER ID',
    'CENTRO DE CONSUMO': 'CONSUMER CENTER',
    'CUPS ELECTRICIDAD': 'ELECTRICITY CUPS',
    'FECHA DE LECTURA': 'READING DATE',
    'AÑO': 'YEAR',
    'MES': 'MONTH',
    'DIA': 'DAY',
    'HORA': 'HOUR',
    'DÍA DE LA SEMANA': 'WEEKDAY',
    'TIPO DE DÍA': 'TYPE OF DAY',
    'ESTACIÓN': 'STATION',
    'TARIFA': 'RATE',
    'PERIODO': 'PERIOD',
    'CONSUMO HORARIO ENERGÍA ACTIVA (kWh)': 'HOURLY ACTIVE ENERGY CONSUMPTION (kWh)',
    'PRECIO ENERGÍA ACTIVA': 'ACTIVE ENERGY PRICE',
    'GRADO 20 DIARIOS': 'GRADE 20 DAILY',
    'GRADO 26 DIARIOS': 'GRADE 26 DAILY',
    'TIPO DE CENTRO A NIVEL DE ADMINISTRACIÓN AUTONÓMICA': 'TYPE OF CENTER AT THE REGIONAL ADMINISTRATION LEVEL',
    'CÓDIGO MUNICIPIO DIRECCIÓN': 'MUNICIPAL CODE ADDRESS',
    'MUNICIPIO DIRECCIÓN': 'MUNICIPALITY ADDRESS',
    'COORDENADA X LONGITUD': 'COORDINATE X LENGTH',
    'COORDENADA Y LATITUD': 'COORDINATE Y LATITUDE',
    'POSICIÓN': 'POSITION',
    'FECHA': 'DATE',
    'Gasto_Lectura': 'Expense_Read',
    'n_dia_semana': 'n_day_week'
}

HOURLY_HOSPITAL_ENERGY_CONSUMPTION_VALUES = {
    'ORGANISMO / CONSEJERÍA': {
        '05 - SANIDAD': '05 - HEALTH',
    },
    'TIPO DE CENTRO DE CONSUMO': {
        'HOSPITAL CON MAS DE 300 CAMAS': 'HOSPITAL WITH MORE THAN 300 BEDS',
        'HOSPITAL CON MENOS DE 300 CAMAS': 'HOSPITAL WITH LESS THAN 300 BEDS',
    },
    'DÍA DE LA SEMANA': {
        'DOMINGO': 'SUNDAY',
        'LUNES': 'MONDAY',
        'MARTES': 'TUESDAY',
        'MIÉRCOLES': 'WEDNESDAY',
        'SÁBADO': 'SATURDAY',
        'VIERNES': 'FRIDAY',
        'JUEVES': 'THURSDAY'
    },
    'TIPO DE CENTRO A NIVEL DE ADMINISTRACIÓN AUTONÓMICA': {
        'HOSPITALES': 'HOSPITAL'
    },
    'TIPO DE DÍA': {
        'Laboral': 'Labor',
        'No laboral (sábados y domingos)': 'Non-working (Saturdays and Sundays)',
        'Festivo nacional': 'National festive'
    }
}

# - Regional Administration energy consumption centres:

ADMINISTRATION_ENERGY_CONSUMPTION_CENTERS_COLUMNS = {
    'ORGANISMO / CONSEJERÍA': 'ORGANISM / COUNSIL',
    'CENTRO GESTOR': 'MANAGEMENT CENTER',
    'ID OPTE CENTRO DE GASTO': 'SPENDING CENTER ID',
    'CENTRO DE GASTO': 'SPENDING CENTER',
    'CÓDIGO INTERNO': 'INTERNAL CODE',
    'TIPO DE CENTRO DE CONSUMO': 'TYPE OF CONSUMER CENTER',
    'ID OPTE CENTRO DE CONSUMO': 'CONSUMER CENTER ID',
    'CENTRO DE CONSUMO': 'CONSUMER CENTER',
    'C.I.F': 'C.I.F',
    'DIRECCIÓN': 'DIRECTION',
    'SUPERFICIE CONSTRUIDA': 'BUILDED SURFACE',
    'OCUPACIÓN': 'OCCUPATION',
    'CUPs E': 'CUPs E',
    'CUPs GN': 'CUPs GN',
    'GSL': 'GSL',
    'TIPO DE CENTRO A NIVEL DE ADMINISTRACIÓN AUTONÓMICA': 'TYPE OF CENTER AT THE REGIONAL ADMINISTRATION LEVEL',
    'CÓDIGO MUNICIPIO DIRECCIÓN': 'MUNICIPAL CODE ADDRESS',
    'MUNICIPIO DIRECCIÓN': 'MUNICIPALITY ADDRESS',
    'COORDENADA X LONGITUD': 'COORDINATE X LENGTH',
    'COORDENADA Y LATITUD': 'COORDINATE Y LATITUDE',
    'POSICIÓN': 'POSITION',
    'REFERENCIA CATASTRAL 1': 'CATASTRAL REFERENCE 1',
    'REFERENCIA CATASTRAL 2': 'CATASTRAL REFERENCE 2',
    'REFERENCIA CATASTRAL 3': 'CATASTRAL REFERENCE 3',
    'REFERENCIA CATASTRAL 4': 'CATASTRAL REFERENCE 4',
    'REFERENCIA CATASTRAL 5': 'CATASTRAL REFERENCE 5',
    'REFERENCIA CATASTRAL 6': 'CATASTRAL REFERENCE 6',
    'REFERENCIA CATASTRAL 7': 'CATASTRAL REFERENCE 7',
}

ADMINISTRATION_ENERGY_CONSUMPTION_CENTERS_VALUES = {
    'ORGANISMO / CONSEJERÍA': {
        '07 - EDUCACIÓN': '07 - EDUCATION',
        '05 - SANIDAD': '05 - HEALTH',
        '04 - FOMENTO Y M. AMBIENTE': '04 - DEVELOPMENT AND ENVIRONMENT',
        '03 - AGRIC. Y G.': '03 - AGRIC. And G.',
        '09 - FAMILIA E IO (BIS)': '09 - FAMILY AND IO (BIS)',
        '10 - CULTURA Y TURISMO': '10 - CULTURE AND TOURISM',
        '08 - EMPLEO E INDUSTRIA': '08 - EMPLOYMENT AND INDUSTRY',
        '02 - ECONOMIA Y HACIENDA': '02 - ECONOMY AND FINANCE',
        '00 - FAMILIA E IGUAL.OPOR': '00 - FAMILY AND EQUAL.',
        '14 - PRESIDENCIA DE LAS CORTES CYL': '14 - PRESIDENCY OF THE COURTS CYL',
        '01 - DE LA PRESIDENCIA': '01 - FROM THE PRESIDENCY'
    },
    'CENTRO GESTOR': {
        '0702 - D.G. CENTROS, PLANI, ORD EDUCA': '0702 - D.G. CENTERS, PLANI, ORD EDUCA',
        '0401 - SG FOMENTO Y MEDIO AMBIENTE': '0401 - SG DEVELOPMENT AND ENVIRONMENT',
        '0524 - GRS (GAP)': '0524 - GRS (GAP)',
        '0301 - SG AGRICULTURA Y GANADERIA': '0301 - SG AGRICULTURE AND LIVESTOCK',
        '0921 - GERENCIA SERV.SOC.': '0921 - SERV.SOC MANAGEMENT.',
        '1003 - CULTURA Y TURISMO': '1003 - CULTURE AND TOURISM',
        '0823 - SERVIC.PÚBL.EMPLEO': '0823 - EMPLOYMENT PUBLIC SERVICE',
        '0410 - FUND PATRIMONIO NATURAL CYL': '0410 - NATURAL HERITAGE CYL FUND',
        '0522 - GRS(GAE)': '0522 - GRS (GAE)',
        '0821 - ICE': '0821 - ICE',
        '0201 - SG ECONOMIA Y HACIENDA': '0201 - SG ECONOMY AND FINANCE',
        '0501 - SG SANIDAD': '0501 - SG HEALTH',
        '0922 - INSTITUTO JUVENTUD': '0922 - YOUTH INSTITUTE',
        '0021 - GSS': '0021 - GSS',
        '0801 - SG EMPLEO': '0801 - SG EMPLOYMENT',
        '0701 - S. G. EDUCACION': '0701 - S. G. EDUCATION',
        '0523 - GRS (GSA)': '0523 - GRS (GSA)',
        '0321 - ITACYL': '0321 - ITACYL',
        '0302 - DG DE COMP IND AGR EMPR AGRAR': '0302 - DG DE COMP IND AGR EMPR AGRAR',
        '0525 - G.E. SANITARIAS': '0525 - G.E. SANITARY',
        '1400 - PRESIDENCIA DE LAS CORTES CYL': '1400 - PRESIDENCY OF THE CORTES CYL',
        '0103 - SG PRESIDENCIA': '0103 - SG PRESIDENCY',
        '0822 - ENTE REG.ENERGIA': '0822 - ENERGY REGISTRATION ENTITY',
        '0901 - SG FAMILIA': '0901 - SG FAMILY',
        '0022 - INSTI. JUVENTUD': '0022 - INSTI. YOUTH',
        '0304 - D G DE DESARROLLO RURAL': '0304 - D G OF RURAL DEVELOPMENT'
    },
    'TIPO DE CENTRO A NIVEL DE ADMINISTRACIÓN AUTONÓMICA': {
        'C. EDUCATIVOS': 'C. EDUCATIONAL',
        'CENTROS DE SALUD': 'HEALTH CENTERS',
        'MUSEO': 'MUSEUM',
        'HOSPITALES': 'HOSPITALS',
        'C. ADMINISTRATIVOS': 'C. ADMINISTRATIVE',
        'OTROS': 'OTHERS',
        'BIBLIOTECA': 'LIBRARY',
        'RESIDENCIA': 'HOME',
        'C. ATENCIÓN SS': 'C. ATTENTION SS',
        'LABORATORIO': 'LABORATORY',
        'C. EDUCACIÓN INFANCIA': 'C. CHILDHOOD EDUCATION',
        'ALBERGUE': 'HOSTEL',
        'C. FORMACIÓN JCyL': 'C. JCyL TRAINING'
    },
    'TIPO DE CENTRO DE CONSUMO': {
        'ADMINISTRATIVO': 'ADMINISTRATIVE',
        'EDIF. SERVICIOS': 'EDIF. SERVICES',
        'EDIFICIO ADMINISTRATIVO': 'ADMINISTRATIVE BUILDING',
        'SUMINISTRO INDUSTRIAL': 'INDUSTRIAL SUPPLY',
        'LABORATORIO': 'LABORATORY',
        'EDIFICIO ADMINISTRATIVO Y LABORATORIO': 'ADMINISTRATIVE AND LABORATORY BUILDING',
        'ALMACÉN Y VIVIENDAS': 'WAREHOUSE AND HOUSING',
        'CENTRO DE FORMACIÓN': 'TRAINING CENTER',
        'GARAJE': 'GARAGE',
        'GARAJE-ARCHIVO': 'GARAGE-FILE',
        'SILO': 'SILO',
        'UNIDAD DE ALMACENAMIENTO Y ADMINISTRACIÓN': 'STORAGE AND ADMINISTRATION UNIT',
        'VIVIENDA': 'HOUSING',
        'EDIFICIO PRÁCTICAS EDUCATIVAS': 'EDUCATIONAL PRACTICES BUILDING',
        'CASA DEL PARQUE': 'HOUSE OF THE PARK',
        'CENTRO DE RECEPCION DE AVES': 'CENTER FOR THE RECEPTION OF BIRDS',
        'ADMINISTRATIVO - EDUCACIÓN AMBIENTAL': 'ADMINISTRATIVE - ENVIRONMENTAL EDUCATION',
        'HOSPITAL CON MAS DE 300 CAMAS': 'HOSPITAL WITH MORE THAN 300 BEDS',
        'HOSPITAL CON MENOS DE 300 CAMAS': 'HOSPITAL WITH LESS THAN 300 BEDS',
        'CENTRO DE SALUD CON URGENCIAS': 'EMERGENCY HEALTH CENTER',
        'OTRO TIPO DE CENTRO': 'ANOTHER TYPE OF CENTER',
        'CENTRO DE SALUD SIN URGENCIAS': 'HEALTH CENTER WITHOUT EMERGENCIES',
        'PISO': 'FLAT',
        'ALMACÉN, LOCAL, RESTO' 'ESCUELA': 'WAREHOUSE, LOCAL, REST, SCHOOL',
        'INSTITUTO DE EDUCACION SECUNDARIA': 'INSTITUTE OF SECONDARY EDUCATION',
        'INSTITUTO DE EDUCACION SECUNDARIA OBLIGATORIA': 'INSTITUTE OF COMPULSORY SECONDARY EDUCATION',
        'COLEGIO DE EDUCACIÓN ESPECIAL': 'COLLEGE OF SPECIAL EDUCATION',
        'CENTRO DE FORMACIÓN DEL PROFESORADO E INNOVACIÓN EDUCATIVA': 'TEACHER TRAINING AND EDUCATIONAL INNOVATION CENTER',
        'CENTRO RURAL DE INNOVACION EDUCATIVA': 'RURAL CENTER OF EDUCATIONAL INNOVATION',
        'CIFP': 'CIFP',
        'CONSERVATORIO DE MÚSICA': 'CONSERVATORY OF MUSIC',
        'ESCUELA DE ARTE': 'SCHOOL OF ART',
        'ESCUELA OFICIAL DE IDIOMAS': 'OFFICIAL LANGUAGE SCHOOL',
        'FORMACIÓN': 'TRAINING',
        'EDIF. ADMINISTRATIVO': 'EDIF. ADMINISTRATIVE',
        'UNIDAD DE INTERVENCIÓN EDUCATIVA': 'EDUCATIONAL INTERVENTION UNIT',
        'CENTRO DE DÍA PARA LA ATENCIÓN DE PERSONAS MAYORES': 'DAY CENTER FOR THE CARE OF ELDERLY PEOPLE',
        'CENTRO DE ATENCIÓN A LA INFANCIA': 'CHILD CARE CENTER',
        'CENTRO DE ATENCIÓN A MINUSVÁLIDOS PSÍQUICOS': 'CENTER OF ATTENTION TO THE PSYCHIC DISABLED',
        'CENTRO DE ATENCIÓN A MINUSVÁLIDOS PSÍQUICOS Y CENTRO OCUPACIONAL': 'CENTER OF ATTENTION TO THE PSYCHIC DISABLED AND OCCUPATIONAL CENTER',
        'SERVICIOS ADMINISTRATIVOS': 'ADMINISTRATIVE SERVICES',
        'CENTRO BASE DE ATENCIÓN A  PERSONAS CON DISCAPACIDAD': 'BASE CENTER OF ATTENTION TO PEOPLE WITH DISABILITIES',
        'COMEDOR SOCIAL': 'SOCIAL DINING ROOM',
        'CENTRO OCUPACIONAL': 'OCCUPATIONAL CENTER',
        'CENTRO DE EDUCACIÓN INFANTIL': 'CHILDREN EDUCATION CENTER',
        'VIVIENDA TUTELADA PARA PERSONAS CON DISCAPACIDAD': 'TUTELED HOUSING FOR PEOPLE WITH DISABILITIES',
        'RESIDENCIA DE PROTECCIÓN A LA INFANCIA': 'RESIDENCE FOR THE PROTECTION OF CHILDREN',
        'RESIDENCIA DE PERSONAS MAYORES': 'RESIDENCE FOR THE ELDERLY PEOPLE',
        'ALBERGUE JUVENIL': 'YOUTH HOSTEL',
        'CAMPAMENTO JUVENIL': 'YOUTH CAMP',
        'RESIDENCIA JUVENIL': 'YOUTH RESIDENCE',
        'ALMACÉN': 'WAREHOUSE',
        'RESIDENCIA': 'RESIDENCE',
        'OFICINA': 'OFFICE',
        'ARCHIVO': 'ARCHIVE',
        'MUSEO': 'MUSEUM',
        'BIBLOTECA/FILMOTECA': 'LIBRARY / FILM LIBRARY',
        'FILIAL MUSEO': 'FILIAL MUSEUM',
        'CENTRO PÚBLICO DE EDUCACIÓN DE PERSONAS ADULTAS': 'PUBLIC CENTER FOR EDUCATION OF ADULTS',
        'ESCUELA HOGAR': 'HOME SCHOOL',
        'CENTRO DE EDUACIÓN INFANTIL': 'CHILDREN EDUCATION CENTER',
        'BASE DE EMERGENCIAS': 'EMERGENCY BASE',
        'COCHERA': 'GARAGE',
        'INCENDIOS, RIEGOS, CENTRO CINEGÉTICO, EMISORA, TORRE VIGILANCIA': 'INCENDIOS, RIEGOS, CENTRO CINEGÉTICO, EMISORA, TORRE VIGILANCIA',
        'ESPACIO DIGITAL': 'DIGITAL SPACE',
        'ALUMBRADO PÚBLICO': 'PUBLIC LIGHTING',
        'NAVE': 'WAREHOUSE',
        'PARQUE MAQUINARIA': 'MACHINERY PARK',
        'OFICINAS': 'OFFICES',
        'REPETIDOR': 'REPEATER',
        'CASA FORESTAL': 'FOREST HOUSE',
        'HELIPUERTO': 'HELIPORT',
        'REFUGIO': 'REFUGE',
        'EDIFICIO CALEFACTADO': 'HEATED BUILDING',
        'PISCIFACTORIA': 'FISH FARM',
        'VIVERO': 'NURSERY',
        'ANTENA': 'ANTENNA',
        'BÁSCULA': 'SCALE',
        'CENTRO FORESTAL': 'FOREST CENTER',
        'DEPORTIVO': 'SPORTS',
        'LOCAL': 'LOCAL',
        'OTROS': 'OTHERS',
        'DELEGACION TERRITORIAL': 'TERRITORIAL DELEGATION',
        'EDF. ADMINISTRATIVO': 'EDF. ADMINISTRATIVE',
        'LABORATORIOS DE METROLOGIA': 'METROLOGY LABORATORIES',
        'ALUMBRADO PUBLICO VAPOR SODIO ALTA PRESION + HALOGENURO METALICO': 'PUBLIC LIGHTING HIGH PRESSURE SODIUM VAPOR + METALLIC HALOGENIDE',
        'ALUMBRADO PUBLICO VAPOR SODIO ALTA PRESION + VAPOR MERCURIO': 'PUBLIC LIGHTING HIGH PRESSURE SODIUM VAPOR + MERCURY VAPOR',
        'ALUMBRADO PUBLICO VAPOR SODIO ALTA PRESION': 'PUBLIC LIGHTING HIGH PRESSURE SODIUM VAPOR',
        'ARCHIVO CENTRAL, ARCHIVO ALMACEN': 'CENTRAL FILE, WAREHOUSE FILE',
        'ALUMBRADO EXTERIOR': 'EXTERIOR LIGHTING',
        'LABORATORIO Y CENTRO DE FORMACIÓN': 'LABORATORY AND TRAINING CENTER',
        'CENTRO DE FORMACIÓN / LABORATORIOS': 'TRAINING CENTER / LABORATORIES',
        'PRESA': 'DAM',
        'LABORATORIO/PLANTA INDUSTRIAL': 'LABORATORY / INDUSTRIAL PLANT',
        'OFICINAS/LABORATORIO/NAVES': 'OFFICES / LABORATORY / WAREHOUSES',
        'RIEGOS': 'IRRIGATIONS'
    }
}

## Energy Efficiency Certificates
ENERGY_EFFICIENCY_CERTIFICATES_COLUMNS = {
    'Posicion': 'Position',
    'Num inscripción': 'Registration number',
    'Fecha inscripción': 'Registration date',
    'Tipo de uso del edificio': 'Building use type',
    'Uso del edificio': 'Building use',
    'Dirección': 'Direction',
    'longitud': 'longitude',
    'latitud': 'latitude',
    'Municipio': 'Municipality',
    'Provincia': 'Province',
    'N ratio consumo primario': 'primary consumption ratio',
    'Calif energía primaria': 'Primary energy label',
    'Num ratio emisiones CO2': 'CO2 emissions ratio',
    'Califemisiones': 'CO2 emitions Rating',
    'Num demanda calef': 'Heating demand ratio',
    'Calif demanda calefac': 'Heating demand rating',
    'N demanda refrig': 'Cooling demand ratio',
    'Calif demanda refriger': 'Cooling demand ratio'
}

ENERGY_EFFICIENCY_CERTIFICATES_VALUES = {
    'Tipo de uso del edificio': {
        'BLOQUES DE VIVIENDAS': 'HOUSING BLOCKS',
        'VIVIENDAS UNIFAMILIARES': 'SINGLE FAMILY HOUSES',
        'EDIFICIOS DEL SECTOR TERCIARIO': 'TERTIARY SECTOR BUILDINGS'
    },
    'Uso del edificio': {
        'VIVIENDA INDIVIDUAL EN BLOQUE': 'INDIVIDUAL HOUSING IN BLOCK',
        'VIVIENDA UNIFAMILIAR ADOSADA': 'SINGLE-FAMILY TOWNHOUSE',
        'VIVIENDA UNIFAMILIAR AISLADA': 'ISOLATED SINGLE-FAMILY HOUSE',
        'LOCAL': 'LOCAL',
        'VIVIENDA UNIFAMILIAR PAREADA': 'SINGLE-FAMILY PAIRED HOUSE',
        'BLOQUE DE VIVIENDAS COMPLETO': 'COMPLETE HOUSING BLOCK',
        'OFICINAS': 'OFFICES',
        'OTROS USOS TERCIARIOS': 'OTHER TERTIARY USES',
        'CENTRO DOCENTE': 'TEACHING CENTER',
        'ADMINISTRATIVO': 'ADMINISTRATIVE',
        'HOTELES Y RESIDENCIAS': 'HOTELS AND RESIDENCES',
        'COMERCIAL': 'COMMERCIAL',
        'SANITARIO': 'SANITARY',
        'EDIFICIO DE OFICINAS': 'OFFICE BUILDING',
        'INSTALACIONES DEPORTIVAS': 'SPORTS FACILITIES',
        'VIVIENDAS UNIFAMILIARES': 'SINGLE FAMILY HOUSES'
    }
}

## - Natural gas consumption of the Regional Administration buildings
NATURAL_GAS_CONSUMPTION_DATASET_COLUMNS = {
    'ORGANISMO / CONSEJERÍA': 'ORGANISM / COUNSIL',
    'CENTRO GESTOR': 'MANAGEMENT CENTER',
    'ID OPTE CENTRO DE GASTO': 'SPENDING CENTER ID',
    'CENTRO DE GASTO': 'SPENDING CENTER',
    'TIPO DE CENTRO DE CONSUMO': 'TYPE OF CONSUMER CENTER',
    'ID OPTE CENTRO DE CONSUMO': 'CONSUMER CENTER ID',
    'CENTRO DE CONSUMO': 'CONSUMER CENTER',
    'CUPS GAS NATURAL': 'NATURAL GAS CUPS',
    'TIPO DE ENERGÍA': 'TYPE OF ENERGY',
    'DISTRIBUIDORA GAS NATURAL': 'NATURAL GAS DISTRIBUTOR',
    'USO GAS NATURAL': 'USE NATURAL GAS',
    'TARIFA GAS NATURAL': 'NATURAL GAS TARIFF',
    'AÑO': 'YEAR',
    'MES': 'MONTH',
    'CONSUMO MENSUAL TOTAL GAS NATURAL (kWh)': 'TOTAL MONTHLY CONSUMPTION OF NATURAL GAS (kWh)',
    'G.D. en Base 20': 'G.D. in Base 20',
    'G.D. en Base 26': 'G.D. in Base 26',
    'TIPO DE CENTRO A NIVEL DE ADMINISTRACIÓN AUTONÓMICA': 'TYPE OF CENTER AT THE REGIONAL ADMINISTRATION LEVEL',
    'CÓDIGO MUNICIPIO DIRECCIÓN': 'MUNICIPAL CODE ADDRESS',
    'MUNICIPIO DIRECCIÓN': 'MUNICIPALITY ADDRESS',
    'COORDENADA X LONGITUD': 'COORDINATE X LENGTH',
    'COORDENADA Y LATITUD': 'COORDINATE Y LATITUDE',
    'POSICIÓN': 'POSITION',
    'FECHA': 'DATE'
}

NATURAL_GAS_CONSUMPTION_DATASET_COLUMN_VALUES = {
    'ORGANISMO / CONSEJERÍA': {
        '05 - SANIDAD': '05 - HEALTH',
        '07 - EDUCACIÓN': '07 - EDUCATION',
        '08 - EMPLEO E INDUSTRIA': '08 - EMPLOYMENT AND INDUSTRY',
        '09 - FAMILIA E IO (BIS)': '09 - FAMILY AND IO (BIS)',
        '02 - ECONOMIA Y HACIENDA': '02 - ECONOMY AND FINANCE',
        '10 - CULTURA Y TURISMO': '10 - CULTURE AND TOURISM',
        '00 - FAMILIA E IGUAL.OPOR': '00 - FAMILY AND EQUAL.',
        '03 - AGRIC. Y G.': '03 - AGRIC. And G.',
        '04 - FOMENTO Y M. AMBIENTE': '04 - DEVELOPMENT AND ENVIRONMENT',
        '01 - DE LA PRESIDENCIA': '01 - FROM THE PRESIDENCY',
        '14 - PRESIDENCIA DE LAS CORTES CYL': '14 - PRESIDENCY OF THE COURTS CYL',
    },
    'CENTRO GESTOR': {
        '0702 - D.G. CENTROS, PLANI, ORD EDUCA': '0702 - D.G. CENTERS, PLANI, ORD EDUCA',
        '0401 - SG FOMENTO Y MEDIO AMBIENTE': '0401 - SG DEVELOPMENT AND ENVIRONMENT',
        '0524 - GRS (GAP)': '0524 - GRS (GAP)',
        '0301 - SG AGRICULTURA Y GANADERIA': '0301 - SG AGRICULTURE AND LIVESTOCK',
        '0921 - GERENCIA SERV.SOC.': '0921 - SERV.SOC MANAGEMENT.',
        '1003 - CULTURA Y TURISMO': '1003 - CULTURE AND TOURISM',
        '0823 - SERVIC.PÚBL.EMPLEO': '0823 - EMPLOYMENT PUBLIC SERVICE',
        '0522 - GRS(GAE)': '0522 - GRS (GAE)',
        '0821 - ICE': '0821 - ICE',
        '0201 - SG ECONOMIA Y HACIENDA': '0201 - SG ECONOMY AND FINANCE',
        '0501 - SG SANIDAD': '0501 - SG HEALTH',
        '0922 - INSTITUTO JUVENTUD': '0922 - YOUTH INSTITUTE',
        '0021 - GSS': '0021 - GSS',
        '0801 - SG EMPLEO': '0801 - SG EMPLOYMENT',
        '0701 - S. G. EDUCACION': '0701 - S. G. EDUCACION',
        '0103 - SG PRESIDENCIA': '0103 - SG PRESIDENCY',
        '0523 - GRS (GSA)': '0523 - GRS (GSA)',
        '0822 - ENTE REG.ENERGIA': '0822 - ENERGY REGISTRATION ENTITY',
        '1400 - PRESIDENCIA DE LAS CORTES CYL': '1400 - PRESIDENCY OF THE CORTES CYL',
        '0901 - SG FAMILIA': '0901 - SG FAMILY',
        '0022 - INSTI. JUVENTUD': '0022 - INSTI. YOUTH',
    },
    'TIPO DE CENTRO DE CONSUMO': {
        'CENTRO DE DÍA PARA LA ATENCIÓN DE PERSONAS MAYORES': 'DAY CENTER FOR THE CARE OF ELDERLY PEOPLE',
        'SERVICIOS ADMINISTRATIVOS': 'ADMINISTRATIVE SERVICES',
        'COMEDOR SOCIAL': 'SOCIAL LUNCHROOM',
        'CENTRO OCUPACIONAL': 'OCCUPATIONAL CENTER',
        'CENTRO DE EDUCACIÓN INFANTIL': "CHILDREN'S EDUCATION CENTER",
        'UNIDAD DE INTERVENCIÓN EDUCATIVA': 'EDUCATIONAL INTERVENTION UNIT',
        'VIVIENDA TUTELADA PARA PERSONAS CON DISCAPACIDAD': 'TUTELED HOUSING FOR PEOPLE WITH DISABILITIES',
        'RESIDENCIA DE PROTECCIÓN A LA INFANCIA': 'CHILD PROTECTION RESIDENCE',
        'RESIDENCIA DE PERSONAS MAYORES': 'RESIDENCE OF THE ELDERLY',
        'CENTRO DE ATENCIÓN A MINUSVÁLIDOS PSÍQUICOS': 'CENTER OF ATTENTION TO THE PSYCHIC DISABLED',
        'ALBERGUE JUVENIL': 'YOUTH HOSTEL',
        'EDIF. ADMINISTRATIVO': 'EDIF. ADMINISTRATIVE',
        'RESIDENCIA JUVENIL': 'YOUTH RESIDENCE',
        'VIVIENDA': 'LIVING PLACE',
        'ARCHIVO': 'ARCHIVE',
        'OFICINA': 'OFFICE',
        'MUSEO': 'MUSEUM',
        'BIBLOTECA/FILMOTECA': 'LIBRARY / FILM LIBRARY',
        'DEPORTIVO': 'SPORTS',
        'RESIDENCIA': 'HOME',
        'EDIFICIO CALEFACTADO': 'HEATED BUILDING',
        'ADMINISTRATIVO': 'ADMINISTRATIVE',
        'CENTRO DE SALUD CON URGENCIAS': 'EMERGENCY HEALTH CENTER',
        'CENTRO DE SALUD SIN URGENCIAS': 'HEALTH CENTER WITHOUT EMERGENCIES',
        'OTRO TIPO DE CENTRO': 'ANOTHER KIND OF CENTER',
        'EDIFICIO ADMINISTRATIVO': 'ADMINISTRATIVE BUILDING',
        'INSTITUTO DE EDUCACION SECUNDARIA': 'INSTITUTE OF SECONDARY EDUCATION',
        'CENTRO PÚBLICO DE EDUCACIÓN DE PERSONAS ADULTAS': 'PUBLIC CENTER FOR EDUCATION OF ADULTS',
        'COLEGIO DE EDUCACIÓN ESPECIAL': 'COLLEGE OF SPECIAL EDUCATION',
        'ESCUELA OFICIAL DE IDIOMAS': 'OFFICIAL SCHOOL OF LANGUAGES',
        'CIFP': 'CIFP',
        'CONSERVATORIO DE MÚSICA': 'CONSERVATORY OF MUSIC',
        'ESCUELA DE ARTE': 'ART SCHOOL',
        'CENTRO DE FORMACIÓN DEL PROFESORADO E INNOVACIÓN EDUCATIVA': 'TEACHER TRAINING AND EDUCATIONAL INNOVATION CENTER',
        'INSTITUTO DE EDUCACION SECUNDARIA OBLIGATORIA': 'INSTITUTE OF COMPULSORY SECONDARY EDUCATION',
        'ESCUELA HOGAR': 'HOME SCHOOL',
        'FORMACIÓN': 'TRAINING',
        'CENTRO DE ATENCIÓN A MINUSVÁLIDOS PSÍQUICOS Y CENTRO OCUPACIONAL': 'CENTER OF ATTENTION TO THE PSYCHIC DISABLED AND OCCUPATIONAL CENTER',
        'CENTRO BASE DE ATENCIÓN A  PERSONAS CON DISCAPACIDAD': 'BASE CENTER OF CARE FOR PEOPLE WITH DISABILITIES',
        'CENTRO DE ATENCIÓN A LA INFANCIA': 'CHILD CARE CENTER',
        'DELEGACION TERRITORIAL': 'TERRITORIAL DELEGATION',
        'EDF. ADMINISTRATIVO': 'EDF. ADMINISTRATIVE',
        'EDIF. SERVICIOS': 'EDIF. SERVICES',
        'LABORATORIO': 'LABORATORY',
        'EDIFICIO ADMINISTRATIVO Y LABORATORIO': 'ADMINISTRATIVE AND LABORATORY BUILDING',
        'PARQUE MAQUINARIA': 'MACHINERY PARK',
        'OFICINAS': 'OFFICES',
        'HOSPITAL CON MAS DE 300 CAMAS': 'HOSPITAL WITH MORE THAN 300 BEDS',
        'HOSPITAL CON MENOS DE 300 CAMAS': 'HOSPITAL WITH LESS THAN 300 BEDS'
    },
    'TIPO DE ENERGÍA': {
        'GAS NATURAL': 'NATURAL GAS'
    },
    'USO GAS NATURAL': {
        'CALEFACCIÓN': 'HEATING',
        'COCINA': 'KITCHEN',
        'OTROS': 'OTHERS'
    },
    'MES': {
        'Febrero': 'February',
        'Mayo': 'May',
        'Junio': 'June',
        'Agosto': 'August',
        'Octubre': 'October',
        'Marzo': 'March',
        'Abril': 'April',
        'Julio': 'July',
        'Noviembre': 'November',
        'Diciembre': 'December',
        'Enero': 'January',
        'Septiembre': 'September'
    },
    'TIPO DE CENTRO A NIVEL DE ADMINISTRACIÓN AUTONÓMICA': {
        'C. ATENCIÓN SS': 'C. ATTENTION SS',
        'C. ADMINISTRATIVOS': 'C. ADMINISTRATIVE',
        'C. EDUCACIÓN INFANCIA': 'C. CHILDHOOD EDUCATION',
        'OTROS': 'OTHERS',
        'RESIDENCIA': 'HOME',
        'ALBERGUE': 'HOSTEL',
        'MUSEO': 'MUSEUM',
        'BIBLIOTECA': 'LIBRARY',
        'CENTROS DE SALUD': 'HEALTH CENTERS',
        'C. EDUCATIVOS': 'C. EDUCATIONAL',
        'C. FORMACIÓN JCyL': 'C. JCyL TRAINING',
        'LABORATORIO': 'LABORATORY',
        'HOSPITALES': 'HOSPITALS',
    }
}

DATASET_ORDER_DICT = [
    {
        'msg': 'Translate Categorical Values for: Regional Administration Energy Consumption Centres',
        'path': 'DATA/centros-de-consumo-energetico-de-la-administracion-autonoma-de-castilla-y-leon.csv',
        'dataset_values_dict': ADMINISTRATION_ENERGY_CONSUMPTION_CENTERS_VALUES,
        'dataset_columns_dict': ADMINISTRATION_ENERGY_CONSUMPTION_CENTERS_COLUMNS
    },
    {
        'msg': 'Translate categorical Values for: Electricity Consumption of the Administration Buildings',
        'path': 'DATA/consumo-de-electricidad-en-centros-de-la-administracion-autonomica-de-castilla-y.csv',
        'dataset_values_dict': ELECTRICITY_CONSUMPTION_DATASET_VALUES,
        'dataset_columns_dict': ELECTRICITY_CONSUMPTION_DATASET_COLUMNS
    },
    {
        'msg': 'Translate categorical Values for: Diesel consumption in education, health and culture centres of the Regional Administration of Castilla y León',
        'path': 'DATA/consumo-de-gasoil-en-centros-de-educacion-y-sanidad-de-la-administracion-autonom.csv',
        'dataset_values_dict': DIESEL_CONSUMPTION_DATASET_COLUMN_VALUES,
        'dataset_columns_dict': DIESEL_CONSUMPTION_DATASET_COLUMNS
    },
    {
        'msg': 'Translate categorical Values for: Hourly hospitals electricity consumption',
        'path': 'DATA/consumos-horarios-en-hospitales.csv',
        'dataset_values_dict': HOURLY_HOSPITAL_ENERGY_CONSUMPTION_VALUES,
        'dataset_columns_dict': HOURLY_HOSPITAL_ENERGY_CONSUMPTION_COLUMNS
    },
    {
        'msg': 'Translate categorical Values for: Gas Consumption of the Administration Buildings',
        'path': 'DATA/consumo-de-gas-en-centros-de-la-administracion-autonomica-de-castilla-y-leon.csv',
        'dataset_values_dict': NATURAL_GAS_CONSUMPTION_DATASET_COLUMN_VALUES,
        'dataset_columns_dict': NATURAL_GAS_CONSUMPTION_DATASET_COLUMNS
    },
    {
        'msg': 'Translate categorical Values for: Energy Efficiency Certificates Dataset',
        'path': 'DATA/certificados-de-eficiencia-energetica.csv',
        'dataset_values_dict': ENERGY_EFFICIENCY_CERTIFICATES_VALUES,
        'dataset_columns_dict': ENERGY_EFFICIENCY_CERTIFICATES_COLUMNS
    }
]
