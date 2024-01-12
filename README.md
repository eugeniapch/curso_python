// Revisar https://medium.com/analytics-vidhya/efficient-way-to-activate-conda-in-vscode-ef21c4c231f2

### Comandos de instalación de librerias 
sudo apt-get update
sudo apt-get upgrade
sudo apt-get install libgl1-mesa-glx libglu1-mesa libxrandr2 libxss1 libxcursor1 libxcomposite1 libasound2 libxi6 libxtst6


Si usamos conda:
conda create --name curso_v2
conda install -c conda-forge python numpy pandas

Su usamos el ambiente de Python (video 8):
python -m env curso_v2 

## Cargando en GitHub
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