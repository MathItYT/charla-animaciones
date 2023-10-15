---
marp: true
class: invert
---

# <spans style="font-size: 36pt">Animación y programación: Fuertes aliados :muscle:</spans>

**Benjamín Ubilla** :computer:

![bg right:40% 40%](osuc.svg)

---

# Desafío 1 :crossed_swords:
Intenta animar el gráfico de $f(x)=x^2$ como se muestra en el siguiente video:
<div style="text-align: center"><video src="challenge1.mp4" style="height: 250px" controls autoplay loop muted></video></div>

---

# Desafío 2 :crossed_swords:
Intenta animar el concepto de probabilidad frecuencial como se muestra en el siguiente video:
<div style="text-align: center"><video src="Challenge2.mp4" style="height: 250px" controls autoplay loop muted></video></div>

---

# Desafío 3 :crossed_swords:
Intenta animar la gráfica 3D de la función $\displaystyle f(x,y)=\frac{1}{5}\sin(5x)\cos(5y)$ como se muestra en el siguiente video:
<div style="text-align: center"><video src="0001-0300.mp4" style="height: 250px" controls autoplay loop muted></video></div>

---

# ¿Qué tienen en común los desafíos? :thinking:
Los tres desafíos requieren:
- **Conocimiento del tema** a animar.
- **Precisión** en la animación.

Sobre lo último, sería demasiado difícil realizar el gráfico (incluso sin animar) de la función $f(x)=x^2$ si no se tiene precisión en la ubicación de los puntos. Podríamos aproximarlo con curvas de Bézier de forma gráfica en Illustrator o Inkscape, pero no sería preciso.

---

<div>
<center style="font-size: 36pt">La solución:</center>
<center style="font-size: 48pt; font-weight: bold">Programar 👨‍💻</center>
</div>

---

# ¿Por qué programar? 😲
- Podemos controlar con **precisión** el cómo se efectuará la animación.
- Podemos **automatizar** la realización usando bucles.
- Podemos **reutilizar** el código para otras animaciones, ya sea con funciones o con clases.
- Podemos **compartir** el código con otros para que lo usen y mejoren. :heart:
- ¡Aprender a programar es **divertido**! :nerd_face::point_up:

---

# ¿Para qué realizar animaciones precisas? :thinking:
- Muchos tópicos que requieren este tipo de animaciones (como las matemáticas, ciencia de datos, física, etc.) **no son fáciles de enseñar**. :sweat_smile:
- Casi siempre estos tópicos tienen una relación íntima con la **programación**. :computer:
- **¡Es una gran oportunidad para aprender!** :smiley:

---

# ¿Qué necesitamos? :hammer_and_wrench:
- **Conocimiento del tema** a animar.
- **Conocimiento de programación**.
- **Lenguaje de programación**, **librerías** y ***software*** para realizar la animación.
- **Pasión** por aprender. :heart:

---

# Lenguajes de programación, librerías y *software* :computer:
| Lenguaje | Librerías o *plugins* | *Software* |
| :---: | :---: | :---: |
| Python :snake: | Matplotlib, Manim, Manim Studio | Jupyter Notebook, VS Code, Blender, FFmpeg, LaTeX |
| Frameworks de JavaScript :globe_with_meridians: | Remotion, Motion Canvas | VS Code, un navegador web |
| GUI (sin lenguaje) :desktop_computer: | Plugins de los *softwares* | Natron, Blender, After Effects, Premiere, Final Cut Pro, DaVinci Resolve |

---

<center style="font-size: 48pt; font-weight: bold">¡Manos a la obra! 🛠️</center>