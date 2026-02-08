from django.core.management.base import BaseCommand
from games.models import Categoria, Juego
from reviews.models import Reseña, PerfilUsuario
from django.contrib.auth.models import User
from datetime import date


class Command(BaseCommand):
    help = 'Poblar la base de datos con datos de prueba para Fase B'
    
    def handle(self, *args, **kwargs):
        self.stdout.write('Creando categorías...')
        
        # Crear categorías
        categorias_nombres = ['Acción', 'RPG', 'Aventura', 'Deportes', 'Estrategia', 'Indie']
        categorias = {}
        for nombre in categorias_nombres:
            cat, created = Categoria.objects.get_or_create(nombre=nombre)
            categorias[nombre] = cat
            if created:
                self.stdout.write(self.style.SUCCESS(f'  ✓ Categoría "{nombre}" creada'))
        
        self.stdout.write('\nCreando juegos...')
        
        # Crear juegos
        juegos_data = [
            {
                'titulo': 'The Legend of Zelda: Breath of the Wild',
                'plataforma': 'Switch',
                'precio': 59.99,
                'fecha_lanzamiento': date(2017, 3, 3),
                'categorias': ['Aventura', 'Acción']
            },
            {
                'titulo': 'Elden Ring',
                'plataforma': 'PC',
                'precio': 49.99,
                'fecha_lanzamiento': date(2022, 2, 25),
                'categorias': ['RPG', 'Acción']
            },
            {
                'titulo': 'Hades',
                'plataforma': 'PC',
                'precio': 24.99,
                'fecha_lanzamiento': date(2020, 9, 17),
                'categorias': ['Indie', 'Acción']
            },
            {
                'titulo': 'FIFA 24',
                'plataforma': 'PlayStation',
                'precio': 69.99,
                'fecha_lanzamiento': date(2023, 9, 29),
                'categorias': ['Deportes']
            },
        ]
        
        juegos = []
        for juego_data in juegos_data:
            cats = juego_data.pop('categorias')
            juego, created = Juego.objects.get_or_create(
                titulo=juego_data['titulo'],
                defaults=juego_data
            )
            if created:
                for cat_nombre in cats:
                    juego.categorias.add(categorias[cat_nombre])
                juegos.append(juego)
                self.stdout.write(self.style.SUCCESS(f'  ✓ Juego "{juego.titulo}" creado'))
        
        self.stdout.write('\nCreando usuarios de prueba...')
        
        # Crear usuarios de prueba
        usuarios_data = [
            {'username': 'gamer1', 'email': 'gamer1@test.com', 'password': 'test123'},
            {'username': 'gamer2', 'email': 'gamer2@test.com', 'password': 'test123'},
        ]
        
        usuarios = []
        for user_data in usuarios_data:
            user, created = User.objects.get_or_create(
                username=user_data['username'],
                defaults={'email': user_data['email']}
            )
            if created:
                user.set_password(user_data['password'])
                user.save()
                usuarios.append(user)
                self.stdout.write(self.style.SUCCESS(f'  ✓ Usuario "{user.username}" creado'))
        
        self.stdout.write('\nActualizando perfiles de usuario...')
        
        # Actualizar perfiles (se crean automáticamente por signal)
        for user in User.objects.all():
            perfil = user.perfil
            if user.username == 'admin':
                perfil.bio = 'Administrador de PlayHub. Amante de los videojuegos desde 1990.'
                perfil.plataforma_favorita = 'PC'
            elif user.username == 'gamer1':
                perfil.bio = 'Jugador casual que disfruta de RPGs y juegos de aventura.'
                perfil.plataforma_favorita = 'Switch'
            elif user.username == 'gamer2':
                perfil.bio = 'Competitivo en juegos de deportes y estrategia.'
                perfil.plataforma_favorita = 'PlayStation'
            perfil.save()
            self.stdout.write(self.style.SUCCESS(f'  ✓ Perfil de "{user.username}" actualizado'))
        
        self.stdout.write('\nCreando reseñas de ejemplo...')
        
        # Crear reseñas
        if juegos and usuarios:
            reseñas_data = [
                {
                    'juego': juegos[0],  # Zelda
                    'usuario': usuarios[0],
                    'puntuacion': 10,
                    'comentario': 'Obra maestra absoluta. La libertad de exploración es incomparable y cada rincón del mapa esconde secretos fascinantes. Los puzzles de los santuarios son ingeniosos y la física del juego permite soluciones creativas.'
                },
                {
                    'juego': juegos[1],  # Elden Ring
                    'usuario': usuarios[1],
                    'puntuacion': 9,
                    'comentario': 'Un RPG épico con un mundo abierto impresionante. La dificultad es alta pero justa, y la sensación de superación al derrotar a cada jefe es increíble. La historia es profunda aunque críptica.'
                },
                {
                    'juego': juegos[2],  # Hades
                    'usuario': usuarios[0],
                    'puntuacion': 9,
                    'comentario': 'Roguelike adictivo con una narrativa excepcional. Cada carrera se siente única y los personajes están muy bien escritos. La jugabilidad es fluida y satisfactoria, perfecto para sesiones cortas o largas.'
                },
            ]
            
            for reseña_data in reseñas_data:
                reseña, created = Reseña.objects.get_or_create(
                    juego=reseña_data['juego'],
                    usuario=reseña_data['usuario'],
                    defaults={
                        'puntuacion': reseña_data['puntuacion'],
                        'comentario': reseña_data['comentario']
                    }
                )
                if created:
                    self.stdout.write(self.style.SUCCESS(
                        f'  ✓ Reseña de "{reseña.usuario.username}" para "{reseña.juego.titulo}" creada'
                    ))
        
        self.stdout.write(self.style.SUCCESS('\n¡Datos de prueba creados exitosamente!'))
