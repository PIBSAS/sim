const subjects2011 = [
  { id: 'B5', name: 'Álgebra y Geometría Analítica', approved: false },
  { id: 'B6', name: 'Análisis Matemático I', approved: false },
  { id: 'B7', name: 'Física I', approved: false },
  { id: 'B8', name: 'Química General', approved: false },
  { id: 'B9', name: 'Informática I', approved: false },
  { id: 'B10', name: 'Inglés Técnico I', approved: false },
  { id: 'B11', name: 'Análisis Matemático II', approved: false },
  { id: 'B12', name: 'Física II', approved: false },
  { id: 'B13', name: 'Técnicas Digitales I', approved: false },
  { id: 'B14', name: 'Dispositivos Electrónicos', approved: false },
  { id: 'B15', name: 'Informática II', approved: false },
  { id: 'B16', name: 'Inglés Técnico II', approved: false },
  { id: 'B17', name: 'Probabilidad y Estadística', approved: false },
  { id: 'B18', name: 'Análisis de Señales y Sistemas', approved: false },
  { id: 'B19', name: 'Teoría de los Circuitos I', approved: false },
  { id: 'B20', name: 'Electrónica Aplicada I', approved: false },
  { id: 'B21', name: 'Técnicas Digitales II', approved: false },
  { id: 'B22', name: 'Instrumentos y Mediciones', approved: false },
  { id: 'B23', name: 'Dibujo Asistido por PC', approved: false },
  { id: 'B24', name: 'Teoría de los Circuitos II', approved: false },
  { id: 'B25', name: 'Electrónica Aplicada II', approved: false },
  { id: 'B26', name: 'Medios de Enlace', approved: false },
  { id: 'B27', name: 'Ingeniería y Sociedad', approved: false },
  { id: 'B28', name: 'Sistemas de Control', approved: false },
  { id: 'B29', name: 'Taller de Proyecto', approved: false },
  { id: 'B30', name: 'Seguridad, Higiene y Medio Ambiente', approved: false },
  { id: 'B31', name: 'Economía, Planificación y Gestión', approved: false },
  { id: 'B32', name: 'Legislación y Ejercicio Profesional', approved: false },
  { id: 'B33', name: 'Práctica Pre-profesional Supervisada', approved: false },
  { id: 'B34', name: 'Redes IA', approved: false },
  { id: 'B35', name: 'Redes IB', approved: false },
  { id: 'B36', name: 'Redes IIA', approved: false },
  { id: 'B37', name: 'Entornos C y Java', approved: false },
  { id: 'B38', name: 'Sistemas de Comunicaciones I', approved: false },
  { id: 'B39', name: 'Redes IIB', approved: false },
  { id: 'B40', name: 'Sistemas Distribuidos', approved: false },
  { id: 'B41', name: 'Redes III', approved: false },
  { id: 'B42', name: 'Tratamiento Digital de Señales', approved: false },
  { id: 'B43', name: 'Antenas y Propagación', approved: false },
  { id: 'B44', name: 'Sistemas de Comunicación III', approved: false },
  { id: 'B45', name: 'Óptica y sonido', approved: false },
  { id: 'B46', name: 'Imagen y Acústica', approved: false },
  { id: 'B47', name: 'Grabación', approved: false },
  { id: 'B48', name: 'Audio digital', approved: false },
  { id: 'B49', name: 'Sistema de Video I', approved: false },
  { id: 'B50', name: 'Sistemas de Video II', approved: false },
  { id: 'B51', name: 'Televisión Digital', approved: false },
  { id: 'B52', name: 'Ruido Acústico', approved: false },
  { id: 'B53', name: 'Mastering y Post prod. de sonido', approved: false },
  { id: 'B54', name: 'Electroacústica', approved: false },
  { id: 'B55', name: 'Sonido en vivo', approved: false },
  { id: 'B56', name: 'Laboratorio de Acústica', approved: false },
  { id: 'B57', name: 'Fundamentos Agronómicos I', approved: false },
  { id: 'B58', name: 'Fundamentos Agronómicos II', approved: false },
  { id: 'B59', name: 'Mecanización Agrícola', approved: false },
  { id: 'B60', name: 'Tecnologías Inalámbricas para el Agro', approved: false },
  { id: 'B61', name: 'Electrónica Aplicada al Agro', approved: false },
  { id: 'B62', name: 'Sistema de Posicionamiento Satelital', approved: false },
  { id: 'B63', name: 'Sensores y Buses de Comunicación', approved: false },
  { id: 'B64', name: 'Diseño de Dispositivos para Uso Agropecuario', approved: false },
  { id: 'B65', name: 'Sistemas para Agro Meteorología', approved: false },
  { id: 'B66', name: 'Electrónica Aplicada a la Ganaderia de Precisión', approved: false },
  { id: 'B67', name: 'Sistemas de Teledetección', approved: false },
  { id: 'B68', name: 'Telemetría y Trazabilidad Electrónica', approved: false },
  { id: 'B69', name: 'Sistemas Electrónicos para Producciones', approved: false },
];

const subjects2024 = [
  { id: 'E5', name: 'Matemática 1', approved: false, equiv: 'Álgebra y Geometría Analítica o Análisis Matemático I' },
  { id: 'E6', name: 'Física 1', approved: false, equiv: 'Física I' },
  { id: 'E7', name: 'Introducción a la Ingeniería Electrónica', approved: false, equiv: 'Física II' },
  { id: 'E8', name: 'Informática 1', approved: false, equiv: 'Informática I' },
  { id: 'E9', name: 'Inglés Técnico 1', approved: false, equiv: 'Inglés Técnico I' },
  { id: 'E10', name: 'Matemática 2a', approved: false, equiv: 'Álgebra y Geometría Analítica Y Análisis Matemático I' },
  { id: 'E11', name: 'Matemática 2b', approved: false, equiv: 'Álgebra y Geometría Analítica Y Análisis Matemático I' },
  { id: 'E12', name: 'Física 2', approved: false, equiv: 'Física I' },
  { id: 'E13', name: 'Técnicas Digitales 1', approved: false, equiv: 'Técnicas Digitales I' },
  { id: 'E14', name: 'Inglés Técnico 2', approved: false, equiv: 'Inglés Técnico II' },
  { id: 'E15', name: 'Matemática 3', approved: false, equiv: 'Análisis Matemático II' },
  { id: 'E16', name: 'Física 3', approved: false, equiv: 'Física II' },
  { id: 'E17', name: 'Informática 2', approved: false, equiv: 'Informática II' },
  { id: 'E18', name: 'Dispositivos Semiconductores', approved: false, equiv: 'Dispositivos Electrónicos' },
  { id: 'E19', name: 'Química General e Inorgánica', approved: false, equiv: 'Química General' },
  { id: 'E20', name: 'Matemática 4', approved: false, equiv: 'Análisis Matemático II' },
  { id: 'E21', name: 'Señales y Sistemas', approved: false, equiv: 'Análisis de Señales y Sistemas' },
  { id: 'E22', name: 'Teoría de circuitos 1', approved: false, equiv: 'Teoría de los Circuitos I' },
  { id: 'E23', name: 'Electrónica aplicada 1', approved: false, equiv: 'Electrónica Aplicada I' },
  { id: 'E24', name: 'Técnicas digitales 2', approved: false, equiv: 'Técnicas Digitales II' },
  { id: 'E25', name: 'Ingeniería y Sociedad', approved: false, equiv: 'Ingeniería y Sociedad' },
  { id: 'E26', name: 'Probabilidad, estadística y procesos estocásticos', approved: false, equiv: 'Probabilidad y Estadística' },
  { id: 'E27', name: 'Teoría de circuitos 2', approved: false, equiv: 'Teoría de los Circuitos II' },
  { id: 'E28', name: 'Electrónica aplicada 2', approved: false, equiv: 'Electrónica Aplicada II' },
  { id: 'E29', name: 'Electromagnetismo aplicado', approved: false, equiv: 'Medios de Enlace' },
  { id: 'E30', name: 'Dibujo asistido por PC', approved: false, equiv: 'Dibujo Asistido por PC' },
  { id: 'E31', name: 'Diseño electrónico', approved: false, equiv: 'Electrónica Aplicada II' },
  { id: 'E32', name: 'Técnicas Digitales 3', approved: false, equiv: 'Técnicas Digitales II' },
  { id: 'E33', name: 'Principios de Comunicaciones Digitales', approved: false, equiv: 'Sistemas de Comunicaciones I' },
  { id: 'E34', name: 'Redes de datos', approved: false, equiv: 'Redes IA Y Redes IB Y Redes IIA' },
  { id: 'E35', name: 'Electrónica de Potencia', approved: false, equiv: '' },
  { id: 'E36', name: 'Análisis de datos', approved: false, equiv: 'Entornos C y Java' },
  { id: 'E37', name: 'Instrumentos y Mediciones Electrónicas', approved: false, equiv: 'Instrumentos y Mediciones' },
  { id: 'E38', name: 'Sistemas de comunicaciones', approved: false, equiv: 'Sistemas de Comunicación III' },
  { id: 'E39', name: 'Sistemas de control', approved: false, equiv: 'Sistemas de Control' },
  { id: 'E40', name: 'Electiva 1', approved: false, equiv: 'una asignatura de orientación' },
  { id: 'E41', name: 'Física electrónica', approved: false, equiv: 'Física II' },
  { id: 'E42', name: 'Diseño de Aplicaciones Web', approved: false, equiv: 'Entornos C y Java' },
  { id: 'E43', name: 'Procesamiento digital de señales', approved: false, equiv: 'Tratamiento Digital de Señales' },
  { id: 'E44', name: 'Sistemas de automatización', approved: false, equiv: 'Sistemas de Control' },
  { id: 'E45', name: 'Electiva 2', approved: false, equiv: 'dos asignaturas de orientación' },
  { id: 'E46', name: 'Práctica Profesional Supervisada', approved: false, equiv: 'Práctica Pre-profesional Supervisada' },
  { id: 'E47', name: 'Trabajo Final de Grado', approved: false, equiv: 'Taller de Proyecto' },
  { id: 'E48', name: 'Taller de proyectos', approved: false, equiv: 'Taller de Proyecto' },
  { id: 'E49', name: 'Economía, planificación y gestión', approved: false, equiv: 'Economía, Planificación y Gestión' },
  { id: 'E50', name: 'Seguridad, higiene y medio ambiente', approved: false, equiv: 'Seguridad, Higiene y Medio Ambiente' },
  { id: 'E51', name: 'Electiva 3', approved: false, equiv: 'tres asignaturas de orientación' },
  { id: 'E52', name: 'Legislación y Ejercicio profesional', approved: false, equiv: 'Legislación y Ejercicio Profesional' },
  { id: 'E53', name: 'Ingles técnico 3', approved: false, equiv: '' },
  { id: 'E54', name: 'Electiva 4', approved: false, equiv: 'cuatro asignaturas de orientación' },
];

function countOrientacionAprobadas() {
  // Redes: B34-B44 (índices 29-39)
  // Multimedia: B45-B56 (índices 40-51)
  // Agro: B57-B69 (índices 52-64)
  const indicesOrientacion = [
    ...Array.from({length: 11}, (_, i) => 29 + i), // Redes (B34-B44)
    ...Array.from({length: 12}, (_, i) => 40 + i), // Multimedia (B45-B56)
    ...Array.from({length: 13}, (_, i) => 52 + i)  // Agro (B57-B69)
  ];
  
  return indicesOrientacion.filter(idx => subjects2011[idx].approved).length;
}

function getSubjectStatus(sub2024) {
  const cond = sub2024.equiv;
  if (!cond) return { status: 'pending', missing: [] };
  // CASO ESPECIAL: Electivas (E40, E45, E51, E54)
  if (sub2024.id === 'E40' || sub2024.id === 'E45' || sub2024.id === 'E51' || sub2024.id === 'E54') {
    const orientCount = countOrientacionAprobadas();
    let needed = 0;
    if (sub2024.id === 'E40') needed = 1;
    else if (sub2024.id === 'E45') needed = 2;
    else if (sub2024.id === 'E51') needed = 3;
    else if (sub2024.id === 'E54') needed = 4;
    
    if (orientCount >= needed) {
      return { status: 'approved', missing: [] };
    } else {
      const faltan = needed - orientCount;
      return { status: 'pending', missing: [`Faltan ${faltan} materia(s) de orientación`] };
    }
  }
  
  if (cond.includes(' o ')) {
    const parts = cond.split(' o ').map(s => s.trim());
    const anyApproved = parts.some(name => {
      if (name.includes('asignatura de orientación')) return false;
      const found = subjects2011.find(s => s.name === name);
      return found ? found.approved : false;
    });
    return { status: anyApproved ? 'approved' : 'pending', missing: [] };
  }
  
  if (cond.includes(' Y ')) {
    const parts = cond.split(' Y ').map(s => s.trim());
    const missing = [];
    let approvedCount = 0;
    
    parts.forEach(name => {
      if (name.includes('asignatura de orientación')) return;
      const found = subjects2011.find(s => s.name === name);
      if (found && found.approved) {
        approvedCount++;
      } else {
        missing.push(name);
      }
    });
    
    if (approvedCount === parts.length && parts.length > 0) {
      return { status: 'approved', missing: [] };
    }
    else if (approvedCount > 0 && approvedCount < parts.length) {
      return { status: 'partial', missing: missing };
    }
    else {
      return { status: 'pending', missing: parts };
    }
  }
  
  if (!cond.includes('asignatura de orientación')) {
    const found = subjects2011.find(s => s.name === cond);
    if (found && found.approved) {
      return { status: 'approved', missing: [] };
    }
  }
  return { status: 'pending', missing: [] };
}

function render() {
  const grid2011 = document.getElementById('plan2011-grid');
  const grid2024 = document.getElementById('plan2024-grid');

  grid2011.innerHTML = '';
  grid2024.innerHTML = '';

  subjects2011.forEach((sub, index) => {
    const div = document.createElement('div');
    div.className = 'subject-item';
	if (index === 37) {
		div.classList.add('categoria-redes-multimedia');
	} else if (index >= 0 && index <= 28) { // B5:B33 - Obligatorias
		div.classList.add('categoria-obligatoria');
	} else if (index >= 29 && index <= 39) { // B34:B44 - Redes
		div.classList.add('categoria-redes');
	} else if (index >= 40 && index <= 51) { // B45:B56 - Multimedia
		div.classList.add('categoria-multimedia');
	} else if (index >= 52 && index <= 64) { // B57:B69 - Agro
		div.classList.add('categoria-agro');
	}
	
    if (sub.approved) div.classList.add('aprobada');
    div.dataset.id = sub.id;
    div.innerHTML = `
      <span class="subject-name">${sub.name}</span>
      <span class="subject-badge">${sub.approved ? '✅ APROBADA' : '⏳ pendiente'}</span>
    `;
    div.addEventListener('click', () => handleClick2011(sub.id));
    grid2011.appendChild(div);
  });

  subjects2024.forEach((sub) => {
    const div = document.createElement('div');
    div.className = 'subject-item';
    
    const { status, missing } = getSubjectStatus(sub);
    
    if (status === 'approved') {
      div.classList.add('aprobada');
      sub.approved = true;
    } else if (status === 'partial') {
      div.classList.add('parcial');
      sub.approved = false;
    } else {
      sub.approved = false;
    }
    
    div.dataset.id = sub.id;
    
    let badgeText = '—';
    if (status === 'approved') {
      badgeText = '✅ APROBADA';
    } else if (status === 'partial') {
      badgeText = missing.join(' + ');
    } else {
      badgeText = sub.equiv || '—';
    }
    
    div.innerHTML = `
      <span class="subject-name">${sub.name}</span>
      <span class="subject-badge">${badgeText}</span>
    `;
    div.addEventListener('click', () => handleClick2024(sub.id));
    grid2024.appendChild(div);
  });

  updateStats();
}

function handleClick2011(id) {
  const sub = subjects2011.find(s => s.id === id);
  if (sub) {
    sub.approved = !sub.approved;
    render();
  }
}

function handleClick2024(id) {
  const sub = subjects2024.find(s => s.id === id);
  if (sub) {
    sub.approved = !sub.approved;
    render();
  }
}

function updateStats() {
  const count2011 = subjects2011.filter(s => s.approved).length;
  const count2024 = subjects2024.filter(s => s.approved).length;
  const total2024 = subjects2024.length;
  const faltan = total2024 - count2024;

  document.getElementById('count2011').textContent = count2011;
  document.getElementById('count2024').textContent = count2024;
  document.getElementById('countFaltan').textContent = faltan;
  document.getElementById('count2024detail').textContent = count2024;
  document.getElementById('countFaltanDetail').textContent = faltan;

  const obligatorias = subjects2011.slice(0, 29).filter(s => s.approved).length;
  const redes = subjects2011.slice(29, 40).filter(s => s.approved).length;
  const multimedia = subjects2011.slice(40, 52).filter(s => s.approved).length;
  const agro = subjects2011.slice(52, 65).filter(s => s.approved).length;
  const mayor = Math.max(redes, multimedia, agro);

  document.getElementById('sumOblig').textContent = obligatorias;
  document.getElementById('sumRedes').textContent = redes;
  document.getElementById('sumMultimedia').textContent = multimedia;
  document.getElementById('sumAgro').textContent = agro;
  document.getElementById('maxOrient').textContent = mayor;
}

render();
