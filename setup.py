from setuptools import setup, find_packages

# Lire le fichier README.md pour la description longue
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='NVBLootChecker',  # Nom de votre projet
    version='0.1.0',  # Version de votre projet
    packages=find_packages(),  # Trouve automatiquement tous les packages dans le répertoire
    include_package_data=True,  # Inclure les fichiers non-code spécifiés dans MANIFEST.in
    install_requires=[
        'fastapi',  # Dépendances de votre projet
        'uvicorn',
        'jinja2',
    ],
    entry_points={
        'console_scripts': [
            'nvblootchecker=src.main',  # Point d'entrée pour le script de ligne de commande
        ],
    },
    author='Julien Balderiotti',  # Votre nom
    author_email='balderiotti@inocess.fr',  # Votre email
    description='Un outil pour vérifier les lots gagnants d\'un tirage au sort.',  # Brève description
    long_description=long_description,  # Description longue
    long_description_content_type='text/markdown',  # Type de contenu de la description longue
    url='https://github.com/julienbltt/NVBLootChecker.git',  # URL de votre dépôt
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.9',  # Version minimale de Python requise
)