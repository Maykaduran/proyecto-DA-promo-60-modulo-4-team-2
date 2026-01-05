5 enero 2025 - proyecto 4 

**TRANSFORMACION** - incluye el PIB dividido en 3 columnas facilitando el uso en Tableau/Power BI.

**IDEAS (chatGPT)** - para usar y representar WHR en el Dashboard:



Perfecto, con el World Happiness Report en mente, te propongo solo ideas sencillas, visuales y fáciles de explicar, pensadas desde el dashboard hacia la presentación (no desde economía ni estadística dura).

Voy por bloques 👇

🎯 Objetivo del dashboard (muy importante)

Que alguien que no conoce el dataset entienda en 30 segundos:

Qué países son más felices

Cómo influye la riqueza (sin tecnicismos)

Qué países “rinden mejor” o “peor” en bienestar

Cómo se comparan regiones

1️⃣ Métricas base (las que YA tenéis y funcionan)
✔ Felicidad absoluta

Life Ladder
👉 Es vuestro eje principal. Todo gira alrededor de esto.

Uso:

Rankings

Mapas

Comparaciones entre países

✔ Riqueza (versión visual)

GDP_k
👉 Usarla SIEMPRE en lugar de GDP.

Uso:

Eje X en scatter

Tooltips

Filtros (p. ej. “países con GDP_k > 20”)

✔ Felicidad relativa

Happiness_per_GDP

Uso:

Rankings “sorprendentes”

Top/bottom países

Insight narrativo para presentación

⚠️ Consejo:

Nunca usarla sola. Siempre explicarla como “relativa al nivel de riqueza”.

2️⃣ Métricas MUY útiles que ya están en el WHR (sin cálculos raros)

Estas son oro para dashboards 👇

🌱 Social support

Muy intuitiva

Fácil de explicar

Uso:

Scatter: Social support vs Life Ladder

Tooltip en mapas

🧘 Healthy life expectancy

Uso:

Comparar países ricos pero con mala salud

Muy potente visualmente

🕊️ Freedom to make life choices

Uso:

Comparar regiones

Gráficos de barras por región

🤝 Perceptions of corruption

Uso:

Contrastar con felicidad

Buen insight narrativo

3️⃣ Gráficos CLAVE (si solo pudierais hacer 4)
1️⃣ Scatter principal (el más importante)

Riqueza vs Felicidad

X → GDP_k

Y → Life Ladder

Color → Región

Tooltip → Social support, Freedom, Corruption

👉 Este gráfico explica el 60% del dataset.

2️⃣ Mapa mundial

Color → Life Ladder

Tooltip → GDP_k, Happiness_per_GDP

👉 Visual inmediato, muy bien para empezar la presentación.

3️⃣ Ranking “inteligente”

Top 10 felicidad relativa

País

Happiness_per_GDP

👉 Aquí salen los países que sorprenden (y engancha al público).

4️⃣ Comparación por regiones

Bar chart o boxplot:

Región

Media de Life Ladder

Media de GDP_k

👉 Perfecto para storytelling:

“Europa vs Latinoamérica vs África…”

4️⃣ Comparaciones fáciles de entender (para slides)

Estas frases salen directamente del dashboard:

“Países con menos PIB pero alta felicidad”

“Países ricos que no convierten riqueza en bienestar”

“El apoyo social pesa más que el PIB en algunos países”

“La libertad percibida correlaciona más que el dinero”

5️⃣ Qué NO recomiendo (para no liar)

🚫 Demasiadas métricas normalizadas
🚫 Índices compuestos complicados
🚫 Gráficos con más de 3 variables visibles
🚫 Ejes con números gigantes (usar _k)

6️⃣ Estructura ideal de la presentación (muy clara)

Mapa → visión global

Scatter GDP vs Happiness → relación clave

Ranking felicidad relativa → insight sorpresa

Factores sociales → explicación humana