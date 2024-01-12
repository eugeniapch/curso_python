
# Curso completo de python

## Comandos de instalación de librerias 
```sh
sudo apt-get update
sudo apt-get upgrade
sudo apt-get install libgl1-mesa-glx libglu1-mesa libxrandr2 libxss1 libxcursor1 libxcomposite1 libasound2 libxi6 libxtst6
```

## Creación de ambientes virtuales
### Si usamos conda:
```sh
conda create --name curso_v2
conda install -c conda-forge python numpy pandas
```
Revisar https://medium.com/analytics-vidhya/efficient-way-to-activate-conda-in-vscode-ef21c4c231f2

### Si usamos el ambiente de Python (video 8):
```sh
python -m env curso_v2
```

## Configuración Git y GutHub

### Para activar las llaves SSH
```sh
eval "$(ssh-agent)"
ssh-add ~/.ssh/id_rsa # la clave es la de sudo en mi caso
```

### Para crear el repositorio en GitHub
```sh
git init
git status
git add README.md
git commit -m "first commit"
git add .
git config --global user.email "eugeniapch@gmail.com"
git config --global user.name "eugeniapch"
git branch -m master main
git commit -m "actualizacion curso python parte 04"
git remote add origin git@github.com:eugeniapch/curso_python.git
git push -u origin main
```
Mostrando todos los módulos instalados
```sh
# verificar la versión de conda
conda info
```