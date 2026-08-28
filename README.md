El Sistema de Reservas Veterinarias es una aplicación web desarrollada con Python y Flask, cuyo objetivo es gestionar de manera sencilla las reservas de atención veterinaria.

Este proyecto fue desarrollado utilizando Git y GitHub como herramientas de control de versiones, aplicando commits, ramas, stash, resolución de conflictos, rebase y etiquetas de versión.

🛠️ Tecnologías utilizadas

Python 3
Flask 3.1.2
Git
GitHub
HTML

🐶 Funcionalidades

El proyecto incluye las siguientes funcionalidades:

Página principal del sistema.
Visualización de reservas.
Creación de nuevas reservas.
Edición de reservas.
Gestión de cambios mediante Git.

🌿 Ramas utilizadas

Durante el desarrollo se utilizaron ramas para separar las diferentes etapas del proyecto.

Rama principal
main

Contiene las versiones estables del proyecto.

Rama de desarrollo
develop

Se utiliza para desarrollar nuevas funcionalidades y realizar pruebas antes de incorporarlas a la versión principal.

Ramas de funcionalidades

También pueden utilizarse ramas específicas para nuevas características:

git checkout -b feature/nueva-funcionalidad

📚 Control de versiones

Para este proyecto se aplicaron diferentes herramientas de Git solicitadas en la actividad.

Commit inicial

Se realizó un commit inicial para guardar el estado original del proyecto:

git add .
git commit -m "feat: commit inicial del sistema de reservas"
Commits significativos

Los cambios se guardaron mediante commits que representan funcionalidades o modificaciones concretas.

Ejemplo:

git commit -m "feat: agregar ruta para nuevas reservas"
Git Stash

Se utilizó git stash para guardar temporalmente cambios que todavía no estaban listos para ser confirmados:

git stash

Para recuperar los cambios:

git stash pop
Resolución de conflictos

Se simuló un conflicto entre ramas modificando la misma sección del código.

El conflicto fue revisado manualmente y posteriormente solucionado, realizando un nuevo commit:

git add .
git commit -m "fix: resolver conflicto en mensaje principal"
Rebase interactivo

Se utilizó un rebase interactivo para organizar y limpiar la historia de commits:

git rebase -i HEAD~3

Esto permitió combinar commits relacionados y mantener una historia más ordenada.

👩‍💻 Autora
Jhorgely Correa A.
