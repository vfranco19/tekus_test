# tekus_test

Plantilla para proyectos de automatizacion web con **Selenium + pytest + Page Object Model**.

## Estructura

```
tekus_test/
├── config/
│   └── config.py          # URL, timeouts, credenciales
├── pages/
│   ├── base_page.py       # Clase base con metodos comunes
│   ├── home_page.py       # Page Object: pagina principal
│   └── login_page.py      # Page Object: pagina de login
├── test/
│   └── test_login.py      # Tests de ejemplo
├── utils/
│   ├── evidence_builder.py    # Recolector de evidencia JSON
│   ├── html_master_report.py  # Generador de reporte HTML
│   ├── logger.py              # Logger configurado
│   └── screenshot_manager.py  # Manager de screenshots
├── evidence/               # Generado automaticamente
│   ├── json/
│   ├── reports/
│   └── screenshots/
├── conftest.py             # Fixtures de pytest (driver, reportes)
├── pytest.ini              # Configuracion de pytest
├── requirements.txt        # Dependencias
└── .gitignore
```

## Inicio rapido

```bash
# 1. Crear entorno virtual
python -m venv venv
source venv/bin/activate

# 2. Instalar dependencias
pip install -r requirements.txt

# 3. Configurar tu sitio web en config/config.py
#    - BASE_URL
#    - Credenciales
#    - Datos de prueba

# 4. Crear tus Page Objects en pages/
# 5. Crear tus tests en test/

# 6. Ejecutar todos los tests
pytest

# 7. Ejecutar un solo archivo
pytest test/test_login.py

```

## Reportes

Al ejecutar `pytest`, se genera automaticamente:
- **JSON**: `evidence/json/execution_report.json`
- **HTML**: `evidence/reports/execution_report.html`

El reporte HTML incluye accordion expandible con screenshots inline.
