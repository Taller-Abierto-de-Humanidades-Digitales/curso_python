
import json

biografias_boom = {
    "Ernesto Sabato": {
        "nacionalidad": "Argentina",
        "bio": """Ernesto Sabato (pronunciado /sáβato/)2​ (Rojas, 24 de junio de 1911-Santos Lugares, 30 de abril de 2011)3​ fue un ensayista, novelista, físico y pintor argentino. Su obra narrativa consiste en tres novelas: El túnel, Sobre héroes y tumbas (consideradas unas de las mejores novelas argentinas del siglo XX) y Abaddón el exterminador. También se destacó como ensayista, autor de libros como Uno y el Universo, Hombres y engranajes, El escritor y sus fantasmas o Apologías y rechazos, en los que reflexiona sobre la condición humana, la vocación de la escritura o los problemas culturales del siglo xx. Fue el segundo argentino galardonado con el Premio Miguel de Cervantes (1984), luego de Jorge Luis Borges (1979)..""",
        "obra_principal": "El túnel",
        "fecha_publicacion": "1948",
        "vivo": False,
    },
    "José Eustasio Rivera": {
        "nacionalidad": "Colombia",
        "bio": """
        José Eustasio Rivera Salas (San Mateo-Rivera, Huila, 19 de febrero de 1888 – Nueva York, 1 de diciembre de 1928), conocido como José Eustasio Rivera, fue un escritor colombiano destacado por su obra poética pero sobre todo por su novela [La vorágine], considerada un clásico de la literatura hispanoamericana.
        """,
        "obra_principal": "La Vorágine",
        "fecha_publicacion": "1924",
        "vivo": False,
    },
    "Jorge Icaza": {
        "nacionalidad": "Ecuador",
        "bio": """
        Jorge Icaza Coronel (Quito, 10 de junio de 1906 - Quito, 26 de mayo de 1978) fue un novelista ecuatoriano. Después de graduarse en la Universidad Central del Ecuador, en Colombia trabajó como escritor y director teatral. Ya había escrito seis obras teatrales, cuando en 1934 fue publicada su más célebre novela, Huasipungo, que le daría fama internacional y que lo llevaría a ser el escritor ecuatoriano más leído de la historia republicana. Es considerado junto con el boliviano Alcides Arguedas y los peruanos Ciro Alegría y José María Arguedas como uno de los máximos representantes del ciclo de la narrativa indigenista del siglo XX
        """,
        "obra_principal": "Huaispungo",
        "fecha_publicacion": "1934",
        "vivo": False,
    },

    "Juan Carlos Onetti": {
        "nacionalidad": "Uruguay",
        "bio": """
            Juan Carlos Onetti Borges (Montevideo, 1 de julio de 1909-Madrid, 30 de mayo de 1994) fue un escritor uruguayo, considerado uno de los narradores más importantes de su país y de la literatura hispanoamericana. Precursor de la novela moderna y la literatura existencialista, obtuvo el prestigioso Premio Miguel de Cervantes en 1980 y el Gran Premio Nacional de Literatura de Uruguay en 1985.
            """,
        "obra_principal": "La vida breve",
        "fecha_publicacion": "1950",
        "vivo": True,
    }}


# save biografias_boom as json file

with open('data/precursores_boom.json', 'w') as f:
    json.dump(biografias_boom, f, indent=4, ensure_ascii=False)
