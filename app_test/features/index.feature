Feature: Autenticacion
    Como usuario del sistema
	Yo quiero que el sistema muestra mensajes personalizados de bienvenida a anónimos y a los usuarios registrados
	De modo que así saber si estoy logueado en el sistema.
 
	Scenario: Ingresa al sistema un usuario anónimo.
		Given Accedo a la url "/"
		Then El servidor envia un codigo http 200 de respuesta
		And Podemos ver "Bienvenido Usuario Anonimo"


