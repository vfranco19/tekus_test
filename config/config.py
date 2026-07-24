class Config:
    """Configuracion centralizada del proyecto.

    Modifica esta clase con los datos de tu aplicacion.
    """

    # URL base del sitio a automatizar
    BASE_URL = "https://tu-sitio-web.com"

    # Tiempo de espera explicito para elementos (segundos)
    TIMEOUT = 10

    # Credenciales de testing
    TEST_USER_EMAIL = "usuario@prueba.com"
    TEST_USER_PASSWORD = "password123"

    # Datos de registro (ajustar segun el formulario)
    SIGNUP_NAME = "Test User"
    SIGNUP_EMAIL = "nuevo_usuario@prueba.com"
