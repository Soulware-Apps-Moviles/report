### Source Code Management

En Soulware, la gestión del código fuente de las soluciones se realiza a través de Git como sistema de control de versiones y Github, como repositorio de alojamiento descentralizado. 

Se ajunta a continuación los enlaces de los repositorios de GitHub:

- Landing Page: [https://github.com/Soulware-Apps-Moviles/landing-page](https://github.com/Soulware-Apps-Moviles/landing-page)
- Mobile app Kotlin: [https://github.com/Soulware-Apps-Moviles/kotlin-app.git](https://github.com/Soulware-Apps-Moviles/kotlin-app.git)
- Mobile app Fluter: [https://github.com/Soulware-Apps-Moviles/flutter-app](https://github.com/Soulware-Apps-Moviles/flutter-app)
- RESTful API: [https://github.com/Soulware-Apps-Moviles/tcompro.git](https://github.com/Soulware-Apps-Moviles/tcompro.git)

Para su gestión interna, se aplicará GitFlow. Se explican a continuación las ramas a crear, así como las convenciones a utilizar para nombrarlas:

**RAMAS PRINCIPALES**

- **main**: Rama principal de producción. Aquí se encuentran las versiones estables del proyecto, listas para ser desplegadas. Toda publicación oficial se hace desde esta rama.

- **develop**: Rama de desarrollo. Aquí se integran las nuevas funcionalidades antes de ser lanzadas a producción. Es la base para las ramas de tipo *feature*, *release* y *bugfix*.

**RAMAS SECUNDARIAS**

- **feature/**: Ramas para el desarrollo de nuevas funcionalidades. Se crean a partir de `develop` y, una vez completadas, se integran de nuevo en `develop`.
  - **Convención de nombres**:  
    `feature/epic-id`  
    Ejemplo: `feature/ep10`

- **bugfix/**: Ramas para la correción de errores detectados en fase de desarrollo. Se crean a partir de `develop` y, una vez completadas, se integran de nuevo en `develop`.
  - **Convención de nombres**:  
    `bugfix/story-id`  
    Ejemplo: `feature/us77`

- **release/**: Ramas para preparar una nueva versión de producción. Se crean desde `develop` cuando ya se ha alcanzado un conjunto estable de funcionalidades. Sirven para realizar pruebas, ajustes menores y documentación. Al finalizar, se integran en `main` y `develop`.
  - **Convención de nombres**:  
    `release/x.y.z`  
    Ejemplo: `release/1.0.0`

- **hotfix/**: Ramas para corregir errores críticos detectados tardíamente en producción. Se crean desde `main` y se integran tanto en `main` como en `develop` (o en `release`, si hubiere alguna rama de ese tipo activa).
  - **Convención de nombres**:  
    `hotfix/story-id`  
    Ejemplo: `hotfix/swr35`