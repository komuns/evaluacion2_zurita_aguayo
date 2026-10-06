from django.shortcuts import render

def inicio(request):
    # Diccionario con los datos dinámicos exigidos por la rúbrica
    contexto = {
        'temas': [
            {
                'nombre': '🕹️ Videojuegos y Arcades',
                'descripcion': 'Colección de títulos retro y consolas clásicas.',
                'foto1': 'images/tema1_foto1.jpg.jpg',
                'foto2': 'images/tema1_foto2.jpg.jpg'
            },
            {
                'nombre': '💻 Hardware Gamer',
                'descripcion': 'Componentes de alto rendimiento e iluminación RGB.',
                'foto1': 'images/tema2_foto1.jpg.jpg',
                'foto2': 'images/tema2_foto2.jpg.jpg'
            }
        ]
    }
    return render(request, 'index.html', contexto)