# NUEVA TAREA:
- anoto [ESIR-XXXX] Breve descrip en mi bloc de notas TODO
- hago pull de master remoto a local
- brancheo rama desde master: [ESIR-XXXX] Breve descrip

# TAREAS EN CURSO:

## DEV:
- hago commit
- pusheo commit
- Jenkins: despliego mi rama a entorno dev
	- me tengo que poner de acuerdo con NTT para que los repositorios que subimos al entorno dev no se pisen
	- abro mi email para cazar errores de Jenkins (subbuzón de soporte)
	- SI no paso lint: me llegará un email a mi subbuzón de soporte
	- SI no se despliega bien: me llegará un email a mi subbuzón de soporte
	- para comprobar que se ha desplegado bien busco "SUCCESS" en el log
	- anoto en jira naturgy que se ha desplegado, además de cualquier otra observación relevante
- Jenkins: ejecuto mi rama en entorno dev (la pruebo)
	- ya me he puesto de acuerdo con NTT anteriormente cuando la he desplegado
	- puedo ver el estado de la ejecución en luigi dev
	- SI no se ejecuta bien: me llegará un email a mi subbuzón de soporte
	- para comprobar que se ha ejecutado bien busco una carita feliz en el log (?)
	- cuando termine las pruebas pertinentes aviso de que he terminado
	- anoto en jira naturgy que se ha probado, además de cualquier otra observación relevante

## PRE:
- Hago pull de master a local
- Mergeo master a mi rama
- Mergeo mi rama a la rama dev y pusheo
- Mergeo mi rama a la rama pre y pusheo
- Jenkins: enciendo servidor si no está ya encendido
	- para ello chequeo web esir pre
- Jenkins: despliego mi rama a entorno pre
	- detalles análogos a los de DEV
	- **NO** hace falta ponerse de acuerdo con NTT por teams
- Jenkins: ejecuto mi rama en entorno pre (la pruebo)
	- detalles análogos a los de DEV

## PRO:
- **esperamos visto bueno de negocio**
- Hago pull de master a local
- Mergeo master a mi rama
- Mergeo mi rama a la rama pro y pusheo
- Jenkins: enciendo servidor si no está ya encendido
	- para ello chequeo web esir pro
- Jenkins: despliego mi rama a entorno pre
	- detalles análogos a los de DEV
	- **SÍ** hace falta ponerse de acuerdo con NTT por teams
- **NO EJECUTO EN ENTORNO PRO. SE HACE DE MADRUGADA**

# TAREA TERMINADA:
- asociarle una release en jira
- asociarle el tiempo de resolución en jira
- asociarle una release en el excel con ntt

# AL COMENZAR EL DÍA...
- Hacer pulls de mi rama, dev, pre y master en el repo en el que vaya a trabajar. Así lo mantengo up to date.
- Si he subido algo a PRO el día anterior, comprobar que no haya petado.
- borrar porquerías del script de prueba de Dbeaver

# AL TERMINAR EL DÍA...
- Jira Naturgy: anotar el tiempo que he invertido en cada tarea
    
