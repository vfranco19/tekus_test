class Config:
    """Configuracion centralizada del proyecto.

    Modifica esta clase con los datos de tu aplicacion.
    """

    # URL base del sitio a automatizar
    BASE_URL = "https://automationexercise.com"

    # Tiempo de espera explicito para elementos (segundos)
    TIMEOUT = 10

    # Credenciales de testing
    TEST_USER_EMAIL = "victor_test_001@prueba.com"
    TEST_USER_PASSWORD = "12345"

    # Datos de registro (ajustar segun el formulario)
    SIGNUP_NAME = "Test User"
    SIGNUP_EMAIL = "ictor_test_003@prueba.com"
