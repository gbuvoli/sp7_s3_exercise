# Mi propio tablero en Streamlit

Puedes utilizar cualquier dataset que quieras trabajar pero para este ejemplo usaremos [The true cost of fast fashion](https://www.kaggle.com/datasets/khushikyad001/the-true-cost-of-fast-fashion-impact?select=true_cost_fast_fashion.csv)

## Paso 1: Crear repositorio en GITHUB para alojar mi proyecto

## Paso 2: Clonar repositorio en mi máquina local

Inicio Windows powershell o Anaconda powershell y **verifico que la ruta corresponda al directorio donde quiero guardar mi repo en local**

> Si quieres cambiar el directorio, recuerda que puedes navegar por las diferentes carpetas de tu computador utilizando el comando `cd`

Una vez me encuentro en el directorio en que quiero trabajar, procedo a clonar el repo.

```bash
git clone URL_DEL_REPOSITORIO

cd nombre_del_depositorio # Acceder a la carpeta del repositorio
```

## Paso 3: Inicio VS Code

Desde la misma consola,  inicio VS CODE con el comando:

```bash
code .
```

## Paso 4: Creo un ambiente virtual para mi proyecto

Creo un nuevo ambiente virtual y lo activo

```bash
conda create -n nombre_env

conda activate nombre_env
```

Debes observar que ahora aparece el nombre de tu ambiente al inicio de cada línea de la terminal.

## Paso 5: En VS Code, seleccionar intérprete

Debes establecer cuál interprete va a procesar tu código, es decir, indicarle el entorno virtual con el que vas a trabajar.

Presiona *Ctrl + Shift + p*  en Vs Code

En la barra que se despliega, escribe *Python: Select Interpreter*

Busca entre las opciones disponibles, el entorno que acabas de crear y seleccionalo.

> Si no aparece el entorno que creaste escoge la opción *Enter interpreter path*, y en la ventana que se abre, dirígete al directorio en el que se encuentra tu entorno, y selecciona el archivo *python.exe*

## Paso 6: Crea un notebook

> Asegurate de que el archivo .csv con los datos se encuentre en el mismo directorio del proyecto.

## Paso 7: Carga tus datos y genera tu análisis en el notebook

> Si necesitas instalar modulos y librerías, puedes hacerlo desde el terminal, asegurandote de tener el ambiente virtual activo.

Explora los datos, realiza un análisis exploratorio y crea visualizaciones que te ayuden a entender mejor la información utilizando plotly express. Estas visualizaciones serán la base de tu tablero en Streamlit.

puedes utilizar el siguiente código como ejemplo para cargar los datos y generar una visualización:

```python
import pandas as pd
import plotly.express as px
# Cargar los datos
df = pd.read_csv('true_cost_fast_fashion.csv')
# Visualizar los primeros registros
print(df.head())
# Crear una visualización
fig = px.bar(df, x='Country', y='Impact', title='Impact of Fast Fashion by Country')
# Mostrar la visualización  
fig.show()
```

## Paso 8: Crea un Script para tu aplicación de Streamlit

Crea un archivo nuevo que se llame `app.py`

Importa las liberías necesarias

> Puedes encontrar los diferentes elementos de streamlit [aquí](https://docs.streamlit.io/develop/api-reference)
> Los gráficos de plotly express [aquí](https://plotly.com/python/plotly-express/#gallery)

``` python
import pandas as pd
import streamlit as st
import plotly.express as xp

# Load the dataset
df = pd.read_csv("true_cost_fast_fashion.csv")

st.header("Fast Fashion Production Analysis")


st.sidebar.title("Filter Options")

# Continua con tu propio diseño y elementos


```

## Paso 9: Genera el archivo requirements

Crea un archivo que se llame *requirements.txt*
Dentro de el, escribe una lista de las librerías que estás utilizando.

``` python
pandas
streamlit
plotly
nbformat
```
##### Paso 10: Ejecuta tu aplicación de Streamlit
En la terminal, asegúrate de que el ambiente virtual esté activo y ejecuta el siguiente comando:

```bash
streamlit run app.py
```
# Esto abrirá tu aplicación en el navegador predeterminado.
```
# Paso 11: Carga tu aplicación en GitHub
Asegúrate de que todos los archivos necesarios estén en el repositorio, incluyendo el archivo `requirements.txt` y el script `app.py`.

```bash
git add .
git commit -m "Añadir aplicación Streamlit y requisitos"
git push origin main
```
# Paso 12: Despliega tu aplicación en Render
1. Crea una cuenta en [Render](https://render.com/).
2. Crea un nuevo servicio de tipo "Web Service".
3. Conecta tu repositorio de GitHub.
4. Configura el servicio:
   - Elige el branch que quieres desplegar (por ejemplo, `main`).
   - En "Build Command", escribe `pip install --upgrade pip && pip install -r requirements.txt`.
   - En "Start Command", escribe `streamlit run app.py`
5. Despliega tu aplicación.
