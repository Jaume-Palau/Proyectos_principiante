# Este es un documento para tener una platilla de lo básico.

## Etiquetas básicas:

-h1 a h6 → títulos
-p → párrafos
-a → enlaces
-img → imágenes
-ul, ol, li → listas
-div → contenedor genérico
-span → contenedor en línea
-blockquote → citas largas
-cite → origen de la cita
-code → código literal
-strong → importancia
-em → énfasis

## Atajos útiles de Emmet (HTML)

### Plantilla base
!
→ Genera la estructura HTML5 completa

### Etiquetas básicas
div
p
h1
section
→ Crea la etiqueta correspondiente

### Clases e IDs
div.container
#main

<div class="container"></div>
<div id="main"></div>

### Anidar elementos
header>nav>ul>li

### Elementos hermanos
header+main+footer

### Multiplicar elementos
li*5

### Texto dentro de la etiqueta
p{Hola mundo}

### Atributos
a[href="#"]
img[src="img.jpg" alt="imagen"]

### Estructura típica de página
header>nav+main+footer

### Listas con clase
ul>li.item*3
