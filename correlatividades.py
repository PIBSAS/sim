import graphviz as gv

# Materias
m ={
    # Matemática
    'Matemática 1': '110',
    'Matemática 2a': '115',
    'Matemática 2b': '116',
    'Matemática 3': '210',
    'Matemática 4': '215',
    'Probabilidad, Estadística\ny\nProcesos Estocásticos':'310',
    # Física
    'Física 1':'111',
    'Física 2':'117',
    'Física 3':'211',
    # Tecnología Básica en Electrónica
    'Introducción a la Ingeniería Electrónica':'112',
    'Técnicas Digitales 1':'118',
    'Dispositivos Semiconductores':'213',
    'Señales y Sistemas':'216',
    'Teoría de Circuitos 1':'217',
    'Electrónica Aplicada 1':'218',
    'Teoría de Circuitos 2':'311',
    'Electrónica Aplicada 2':'312',
    'Electromagnetismo Aplicado':'313',
    'Diseño Electrónico':'315',
    'Instrumentos\ny\nMediciones Electrónicas':'411',
    'Física Electrónica':'414',
    # Informatica
    'Informática 1':'113',
    'Informática 2':'212',
    # Digital
    'Técnicas Digitales 2':'219',
    'Técnicas Digitales 3':'316',
    'Procesamiento Digital de Señales':'416',
    # Comunicaciones
    'Principios de Comunicaciones Digitales':'317',
    'Redes de Datos':'318',
    'Sistemas de Comunicaciones':'412',
    # Automatización
    'Electrónica de Potencia':'319',
    'Sistemas de Control':'413',
    'Sistemas de Automatización':'417',
    # Análisis de Datos
    'Análisis de Datos':'410',
    'Diseño de Aplicaciones Web':'415',
    # Práctica Integradora Ingeniería en Electrónica
    'Gestión de Proyectos Electrónicos':'510',
    'Trabajo final de Grado':'516',
}

msin = {
    # Sin Correlativa
    'Sin correlativa':'000',
    # Química
    'Química General':'214',
    # Práctica Integradora Ingeniería en Electrónica
    'Ingeniería y Sociedad':'220',
    # Informática
    'Dibujo Asistido por PC':'314',
}

ming = {
    # Ingles
    'Inglés Técnico 1':'114',
    'Inglés Técnico 2':'119',
}

minicial = {
    # Ciclo Inicial
    'Ciclo Inicial':'001',
    # Ingles
    'Inglés Técnico 3':'514',
    'Legislación y Ejercicio Profesional':'513',
    'Práctica Pre Profesional Supervisada':'515',
    # Análisis Económico
    'Economía, Planificación y Gestión':'511',
    # Seguridad, Higiene y Ambiente
    'Seguridad, Higiene y Medio Ambiente':'512'
}

magro = {
    # Aplicaciones Agropecuarias
    'Área: Aplicaciones Agropecuarias':'002',
    'Fundamentos Agronómicos':'401-A',
    'Mecanización Agrícola':'402-A',
    'Electrónica Aplicada al Agro':'501-A',
    'Tecnologías Inalámbricas\ny\nSistemas para el Agro':'502-A'
}

mana = {
    # Análisis de Datos
    'Área: Análisis de Datos':'003',
    'Bases de Datos':'401-D',
    'Programación\nde\nAplicaciones Móviles\nen\ntiempo real':'402-D',
    'Visión por Computadora':'501-D',
    'Aplicaciones de Inteligencia Artificial en Electrónica':'502-D'
}

mauto = {
    # Automatización Industrial
    'Área: Automatización Industrial':'004',
    'Automatización Industrial':'401-I',
    'Protocolos y Buses de Comunicación':'402-I',
    'Robótica Industrial':'501-I',
    'Control Avanzado':'502-I'
}

mred = {
    # Redes de Telecomunicaciones
    'Área: Redes de Telecomunicaciones':'005',
    'Redes Inalámbricas':'401-T',
    'Redes de Datos 2':'402-T',
    'Propagación y Sistemas Irradiantes':'501-T',
    'Tecnologías IoT':'502-T',
}

inicial = {
    # Matemática
    'Matemática 1': '110',
    'Matemática 2a': '115',
    'Matemática 2b': '116',
    'Matemática 3': '210',
    'Matemática 4': '215',
    'Probabilidad, Estadística\ny\nProcesos Estocásticos':'310',
    # Física
    'Física 1':'111',
    'Física 2':'117',
    'Física 3':'211',
    # Tecnología Básica en Electrónica
    'Introducción a la Ingeniería Electrónica':'112',
    'Técnicas Digitales 1':'118',
    'Dispositivos Semiconductores':'213',
    'Señales y Sistemas':'216',
    'Teoría de Circuitos 1':'217',
    'Electrónica Aplicada 1':'218',
    'Teoría de Circuitos 2':'311',
    'Electrónica Aplicada 2':'312',
    'Electromagnetismo Aplicado':'313',
    'Diseño Electrónico':'315',
    # Informática
    'Informática 1':'113',
    'Informática 2':'212',
    'Dibujo Asistido por PC':'314',
    # Digital
    'Técnicas Digitales 2':'219',
    'Técnicas Digitales 3':'316',
    # Comunicaciones
    'Principios de Comunicaciones Digitales':'317',
    'Redes de Datos':'318',
    # Automatización
    'Electrónica de Potencia':'319',
    # Ingles
    'Inglés Técnico 1':'114',
    'Inglés Técnico 2':'119',
    # Química
    'Química General':'214',
    # Práctica Integradora Ingeniería en Electrónica
    'Ingeniería y Sociedad':'220', 
}
    
# Correlativas
c = {
    'Matemática 2a': ['110'],
    'Matemática 2b': ['110'],
    'Matemática 3': ['115', '116'],
    'Matemática 4': ['210'],
    # Física
    'Física 2':['111'],
    'Física 3':['116', '117'],
    'Física Electrónica':['211'],
    # Informática
    'Informática 2':['113'],
    # Digital
    'Técnicas Digitales 2':['118', '212'],
    'Análisis de Datos':['212', '310'],
    'Probabilidad, Estadística\ny\nProcesos Estocásticos':['215', '216'],
    'Técnicas Digitales 1':['112', '113'],
    'Dispositivos Semiconductores':['112'],
    'Señales y Sistemas':['210'],
    'Teoría de Circuitos 1':['111', '112'],
    'Electrónica Aplicada 1':['211', '213'],
    'Teoría de Circuitos 2':['216', '217'],
    'Electrónica Aplicada 2':['218'],
    'Electromagnetismo Aplicado':['211'],
    'Diseño Electrónico':['311', '312'],
    'Instrumentos\ny\nMediciones Electrónicas':['311', '312'],
    'Técnicas Digitales 3':['219'],
    'Procesamiento Digital de Señales':['316'],
    # Comunicaciones
    'Principios de Comunicaciones Digitales':['313', '310'],
    'Redes de Datos':['219'],
    'Sistemas de Comunicaciones':['317', '318'],
    # Automatización
    'Electrónica de Potencia':['217', '218'],
    'Sistemas de Control':['319'],
    'Sistemas de Automatización':['413'],
    # Análisis de Datos
    'Diseño de Aplicaciones Web':['410'],
    # Práctica Integradora Ingeniería en Electrónica
    'Gestión de Proyectos Electrónicos':['412', '413'],
    'Trabajo final de Grado':['412', '413'],   
}

csin = {
    # Sin Correlativa
    'Sin correlativa':['214', '220', '314'],
}

cing = {
    # Ingles
    'Inglés Técnico 2':['114'],
}

cinicial = {
    # Ingles
    'Inglés Técnico 3':['001'],
    # Práctica Integradora Ingeniería en Electrónica
    'Legislación y Ejercicio Profesional':['001'],
    'Práctica Pre Profesional Supervisada':['001'],
    # Análisis Económico
    'Economía, Planificación y Gestión':['001'],
    # Seguridad, Higiene y Ambiente
    'Seguridad, Higiene y Medio Ambiente':['001'],
}

cagro = {
    # Electivas
    'Área: Aplicaciones Agropecuarias':['401-A', '402-A', '501-A', '502-A'],
}

cana = {
    # Electivas
    'Área: Análisis de Datos':['401-D', '402-D', '501-D', '502-D'],
}

cauto = {
    # Electivas
    'Área: Automatización Industrial':['401-I', '402-I', '501-I', '502-I'],
}

cred = {
    # Electivas
    'Área: Redes de Telecomunicaciones':['401-T', '402-T', '501-T', '502-T'],
}

dot = gv.Digraph('round-table')
dotm = gv.Digraph('round-table')
dotmsin = gv.Digraph('round-table')
dotming = gv.Digraph('round-table')
dotminicial = gv.Digraph('round-table')
dotmagro = gv.Digraph('round-table')
dotmana = gv.Digraph('round-table')
dotmauto = gv.Digraph('round-table')
dotmred = gv.Digraph('round-table')

# Estetica
#dot.attr(bgcolor='#F8FAFC')
#dot.attr('node', style='filled', fillcolor='#DBEAFE', color='#3B82F6', fontname='Segoe UI')
area = {
    'Matemática':[
        'Matemática 1',
        'Matemática 2a',
        'Matemática 2b',
        'Matemática 3',
        'Matemática 4',
        'Probabilidad, Estadística\ny\nProcesos Estocásticos'],
    'Física':[
        'Física 1',
        'Física 2',
        'Física 3'],
    'Tecnología Básica en Electrónica':[
        'Introducción a la Ingeniería Electrónica',
        'Técnicas Digitales 1',
        'Dispositivos Semiconductores',
        'Señales y Sistemas',
        'Teoría de Circuitos 1',
        'Electrónica Aplicada 1',
        'Teoría de Circuitos 2',
        'Electrónica Aplicada 2',
        'Electromagnetismo Aplicado',
        'Diseño Electrónico',
        'Instrumentos\ny\nMediciones Electrónicas',
        'Física Electrónica'],
    'Informática':[
        'Informática 1',
        'Informática 2',
        'Dibujo Asistido por PC'],
    'Digital':[
        'Técnicas Digitales 2',
        'Técnicas Digitales 3',
        'Procesamiento Digital de Señales'],
    'Comunicaciones':[
        'Principios de Comunicaciones Digitales',
        'Redes de Datos',
        'Sistemas de Comunicaciones'],
    'Automatización':[
        'Electrónica de Potencia',
        'Sistemas de Control',
        'Sistemas de Automatización'],
    'Análisis de Datos':[
        'Análisis de Datos',
        'Diseño de Aplicaciones Web'],
    'Inglés':[
        'Inglés Técnico 1',
        'Inglés Técnico 2',
        'Inglés Técnico 3'],
    'Química':['Química General'],
    'Práctica Integradora Ingeniería en Electrónica':[
        'Ingeniería y Sociedad',
        'Gestión de Proyectos Electrónicos',
        'Legislación y Ejercicio Profesional',
        'Práctica Pre Profesional Supervisada',
        'Trabajo final de Grado'],
    'Análisis Económico':['Economía, Planificación y Gestión'],
    'Seguridad, Higiene y Ambiente':['Seguridad, Higiene y Medio Ambiente'],
    'Sin Correlativa':['Sin correlativa'],
    'Agropecuarias':[
        'Área: Aplicaciones Agropecuarias',
        'Fundamentos Agronómicos',
        'Mecanización Agrícola',
        'Electrónica Aplicada al Agro',
        'Tecnologías Inalámbricas\ny\nSistemas para el Agro'],
    'Datos':[
        'Área: Análisis de Datos',
        'Bases de Datos',
        'Programación\nde\nAplicaciones Móviles\nen\ntiempo real',
        'Visión por Computadora',
        'Aplicaciones de Inteligencia Artificial en Electrónica'],
    'Industrial':[
        'Área: Automatización Industrial',
        'Automatización Industrial',
        'Protocolos y Buses de Comunicación',
        'Robótica Industrial',
        'Control Avanzado'],
    'Telecomunicaciones':[
        'Área: Redes de Telecomunicaciones',
        'Redes Inalámbricas',
        'Redes de Datos 2',
        'Propagación y Sistemas Irradiantes',
        'Tecnologías IoT'],
    'Ciclo Inicial':['Ciclo Inicial'],
}

colores = {
    'Matemática': {
        'color': '#5C9AFF', 'borde': '#1D4ED8'
    },
    'Física': {
        'color': '#F4BC06', 'borde': '#A16207'
    },
    'Tecnología Básica en Electrónica': {
        'color': '#36C805', 'borde': '#166534'
    },
    'Informática': {
        'color': '#06B8F4', 'borde': '#0369A1'
    },
    'Digital': {
        'color': '#CFFAFE', 'borde': '#0E7490'
    },
    'Comunicaciones': {
        'color': '#E0F406', 'borde': '#717A00'
    },
    'Automatización': {
        'color': '#FFEDD5', 'borde': '#EA580C'
    },
    'Análisis de Datos': {
        'color': '#F3E8FF', 'borde': '#9333EA'
    },
    'Inglés': {
        'color': '#FB59F3', 'borde': '#A21CAF'
    },
    'Química': {
        'color': '#ECFCCB', 'borde': '#65A30D'
    },
    'Práctica Integradora Ingeniería en Electrónica': {
        'color': '#FEE2E2', 'borde': '#DC2626'
    },
    'Análisis Económico': {
        'color': '#CCFBF1', 'borde': '#0F766E'
    },
    'Seguridad, Higiene y Ambiente': {
        'color': '#E2E8F0', 'borde': '#475569'
    },
    'Sin Correlativa': {
        'color': '#F1F5F9', 'borde': '#94A3B8'
    },
    'Ciclo Inicial': {
        'color': '#E2E8F0', 'borde': '#475569'
    },
    'Agropecuarias': {
        'color': '#FFAE00', 'borde': '#A16207'
    },
    'Datos': {
        'color': '#D9F66D', 'borde': '#4D7C0F'
    },
    'Industrial': {
        'color': '#FED7AA', 'borde': '#C2410C'
    },
    'Telecomunicaciones': {
        'color': '#F45D06', 'borde': '#C2410C'
    },
}

# Crear nodos Materias
for asignatura, codigo in m.items():
    #print(asignatura, codigo)
    color = next(
        (nombre for nombre, materias in area.items()
         if asignatura in materias),
        None
    )

    if color is not None:
        dotm.node(
            codigo,
            asignatura,
            style=colores[color].get('style', 'filled'),
            fillcolor=colores[color]['color'],
            color=colores[color]['borde'],
            fontcolor='white' if color in [
                'Matemática',
                'Tecnología Básica en Electrónica',
                'Telecomunicaciones',
            ] else
                '#172033',
            fontname='Segoe UI Bold',
            penwidth='2.3'
        )
    else:
        dotm.node(codigo, asignatura)

# nodos Sin correlativa
for asignatura, codigo in msin.items():
    #print(asignatura, codigo)
    color = next(
        (nombre for nombre, materias in area.items()
         if asignatura in materias),
        None
    )

    if color is not None:
        dotmsin.node(
            codigo,
            asignatura,
            style=colores[color].get('style', 'filled'),
            fillcolor=colores[color]['color'],
            color=colores[color]['borde'],
            fontcolor='#172033',
            fontname='Segoe UI Bold',
            penwidth='2.3'
        )
    else:
        dotmsin.node(codigo, asignatura)

# Nodos ingles
for asignatura, codigo in ming.items():
    #print(asignatura, codigo)
    color = next(
        (nombre for nombre, materias in area.items()
         if asignatura in materias),
        None
    )

    if color is not None:
        dotming.node(
            codigo,
            asignatura,
            style=colores[color].get('style', 'filled'),
            fillcolor=colores[color]['color'],
            color=colores[color]['borde'],
            fontcolor='white' if color in [
                'Inglés',
            ] else
                '#172033',
            fontname='Segoe UI Bold',
            penwidth='2.3'
        )
    else:
        dotming.node(codigo, asignatura)

# Nodos ciclo inicial
for asignatura, codigo in minicial.items():
    #print(asignatura, codigo)
    color = next(
        (nombre for nombre, materias in area.items()
         if asignatura in materias),
        None
    )

    if color is not None:
        dotminicial.node(
            codigo,
            asignatura,
            style=colores[color].get('style', 'filled'),
            fillcolor=colores[color]['color'],
            color=colores[color]['borde'],
            fontcolor='#172033',
            fontname='Segoe UI Bold',
            penwidth='2.3'
        )
    else:
        dotminicial.node(codigo, asignatura)

# Nodos Agro
for asignatura, codigo in magro.items():
    #print(asignatura, codigo)
    color = next(
        (nombre for nombre, materias in area.items()
         if asignatura in materias),
        None
    )

    if color is not None:
        dotmagro.node(
            codigo,
            asignatura,
            style=colores[color].get('style', 'filled'),
            fillcolor=colores[color]['color'],
            color=colores[color]['borde'],
            fontcolor='#172033',
            fontname='Segoe UI Bold',
            penwidth='2.3'
        )
    else:
        dotmagro.node(codigo, asignatura)

# Nodos Analisis de Datos
for asignatura, codigo in mana.items():
    #print(asignatura, codigo)
    color = next(
        (nombre for nombre, materias in area.items()
         if asignatura in materias),
        None
    )

    if color is not None:
        dotmana.node(
            codigo,
            asignatura,
            style=colores[color].get('style', 'filled'),
            fillcolor=colores[color]['color'],
            color=colores[color]['borde'],
            fontcolor='#172033',
            fontname='Segoe UI Bold',
            penwidth='2.3'
        )
    else:
        dotmana.node(codigo, asignatura)

# Nodos Automatización
for asignatura, codigo in mauto.items():
    #print(asignatura, codigo)
    color = next(
        (nombre for nombre, materias in area.items()
         if asignatura in materias),
        None
    )

    if color is not None:
        dotmauto.node(
            codigo,
            asignatura,
            style=colores[color].get('style', 'filled'),
            fillcolor=colores[color]['color'],
            color=colores[color]['borde'],
            fontcolor='#172033',
            fontname='Segoe UI Bold',
            penwidth='2.3'
        )
    else:
        dotmauto.node(codigo, asignatura)

# Nodos Redes
for asignatura, codigo in mred.items():
    #print(asignatura, codigo)
    color = next(
        (nombre for nombre, materias in area.items()
         if asignatura in materias),
        None
    )

    if color is not None:
        dotmred.node(
            codigo,
            asignatura,
            style=colores[color].get('style', 'filled'),
            fillcolor=colores[color]['color'],
            color=colores[color]['borde'],
            fontcolor='white' if color in [
                'Telecomunicaciones',
            ] else
                '#172033',
            fontname='Segoe UI Bold',
            penwidth='2.3'
        )
    else:
        dotmred.node(codigo, asignatura)

# Correlativas
for materia, correlativas in c.items():
    grupo = next(
        (nombre for nombre, materias in area.items()
         if materia in materias),
        None
    )
    
    for correlativa in correlativas:
        dotm.edge(correlativa, m[materia],color=colores[grupo]['borde'] if grupo else '#64748B', penwidth='1.5')

# csin cing cinicial cagro cana cauto cred
for materia, correlativas in csin.items():
    grupo = next(
        (nombre for nombre, materias in area.items()
         if materia in materias),
        None
    )
    
    for correlativa in correlativas:
        dotmsin.edge(correlativa, msin[materia],color=colores[grupo]['borde'] if grupo else '#64748B', penwidth='1.5')

# Correlativas inglés
for materia, correlativas in cing.items():
    grupo = next(
        (nombre for nombre, materias in area.items()
         if materia in materias),
        None
    )
    
    for correlativa in correlativas:
        dotming.edge(correlativa, ming[materia],color=colores[grupo]['borde'] if grupo else '#64748B', penwidth='1.5')

# Correlativas Ciclo Inicial
for materia, correlativas in cinicial.items():
    grupo = next(
        (nombre for nombre, materias in area.items()
         if materia in materias),
        None
    )
    
    for correlativa in correlativas:
        dotminicial.edge(correlativa, minicial[materia],color=colores[grupo]['borde'] if grupo else '#64748B', penwidth='1.5')

# Correlativas Agro
for materia, correlativas in cagro.items():
    grupo = next(
        (nombre for nombre, materias in area.items()
         if materia in materias),
        None
    )
    
    for correlativa in correlativas:
        dotmagro.edge(correlativa, magro[materia],color=colores[grupo]['borde'] if grupo else '#64748B', penwidth='1.5')

# Correlativas Análisis de Datos
for materia, correlativas in cana.items():
    grupo = next(
        (nombre for nombre, materias in area.items()
         if materia in materias),
        None
    )
    
    for correlativa in correlativas:
        dotmana.edge(correlativa, mana[materia],color=colores[grupo]['borde'] if grupo else '#64748B', penwidth='1.5')

# Correlativas Automatización
for materia, correlativas in cauto.items():
    grupo = next(
        (nombre for nombre, materias in area.items()
         if materia in materias),
        None
    )
    
    for correlativa in correlativas:
        dotmauto.edge(correlativa, mauto[materia],color=colores[grupo]['borde'] if grupo else '#64748B', penwidth='1.5')

# Correlativas Redes
for materia, correlativas in cred.items():
    grupo = next(
        (nombre for nombre, materias in area.items()
         if materia in materias),
        None
    )
    
    for correlativa in correlativas:
        dotmred.edge(correlativa, mred[materia],color=colores[grupo]['borde'] if grupo else '#64748B', penwidth='1.5')

dot.attr(rankdir='TB', newrank='true')

# Cluster Materias
with dot.subgraph(name='cluster_m') as sm:
    sm.attr(label='Correlatividades', labelloc='t', style='rounded', margin = '55', fontname='Segoe UI Bold', fontsize='20', fontcolor='#172033')
    sm.body.extend(dotm.body)

# Cluster Materias Sin correlativa
with dot.subgraph(name='cluster_msin') as smsin:
    smsin.attr(label='Sin Correlativas', labelloc='t',style='rounded', margin = '55', fontname='Segoe UI Bold', fontsize='20', fontcolor='#172033')
    smsin.body.extend(dotmsin.body)

# Cluster Materias Inglés
with dot.subgraph(name='cluster_ming') as sming:
    sming.attr(label='Inglés', labelloc='t',style='rounded', margin = '55', fontname='Segoe UI Bold', fontsize='20', fontcolor='#172033')
    sming.body.extend(dotming.body)

# Cluster Materias Ciclo Inicial
with dot.subgraph(name='cluster_minicial') as sminicial:
    sminicial.attr(label='Requiere el Ciclo Inicial', labelloc='t',style='rounded', margin = '55', fontname='Segoe UI Bold', fontsize='20', fontcolor='#172033')
    sminicial.body.extend(dotminicial.body)

# Cluster Materias Agro
with dot.subgraph(name='cluster_magro') as smagro:
    smagro.attr(label='Aplicaciones Agropecuarias', labelloc='t', style='rounded', margin = '55', fontname='Segoe UI Bold', fontsize='20', fontcolor='#172033')
    smagro.body.extend(dotmagro.body)

# Cluster Materias Análisis de Datos
with dot.subgraph(name='cluster_mana') as smana:
    smana.attr(label='Análisis de Datos', labelloc='t',style='rounded', margin = '55', fontname='Segoe UI Bold', fontsize='20', fontcolor='#172033')
    smana.body.extend(dotmana.body)

# Cluster Materias Automatización
with dot.subgraph(name='cluster_mauto') as smauto:
    smauto.attr(label='Automatización Industrial', labelloc='t',style='rounded', margin = '55', fontname='Segoe UI Bold', fontsize='20', fontcolor='#172033')
    smauto.body.extend(dotmauto.body)

# Cluster Materias Redes
with dot.subgraph(name='cluster_mred') as smred:
    smred.attr(label='Redes de Telecomunicaciones', labelloc='t',style='rounded', margin = '55', fontname='Segoe UI Bold', fontsize='20', fontcolor='#172033')
    smred.body.extend(dotmred.body)

# Union invisible
dot.edge('516', '214', style='invis', weight='100')
dot.edge('000', '114', style='invis', weight='100')
dot.edge('119', '001', style='invis', weight='100')
dot.edge('515', '402-A', style='invis', weight='100')
dot.edge('002', '402-D', style='invis', weight='100')
dot.edge('003', '501-I', style='invis', weight='100')
dot.edge('004', '402-T', style='invis', weight='100')

dot.format = 'svg'

# Guardar como pdf y mostrar
dot.render('salida', view=True, cleanup=True)
