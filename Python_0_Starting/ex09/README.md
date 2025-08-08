# ft_package

Un petit package Python d’exemple.

- Nom: ft_package
- Version: 0.0.1
- Résumé: A sample test package
- Auteur: eagle
- Email: eagle@42.fr
- Licence: MIT
- Home-page: https://github.com/eagle/ft_package

## Fonctionnalité

- `count_in_list(lst, item)` retourne le nombre d’occurrences de `item` dans `lst`.

Exemple:
```python
from ft_package import count_in_list

print(count_in_list(["toto", "tata", "toto"], "toto"))  # 2
print(count_in_list(["toto", "tata", "toto"], "tutu"))  # 0
```

## Installation

Depuis les artefacts construits (les deux commandes doivent fonctionner):
```bash
pip install ./dist/ft_package-0.0.1.tar.gz
pip install ./dist/ft_package-0.0.1-py3-none-any.whl
```

Vérifier l’installation:
```bash
pip list | grep ft_package
pip show -v ft_package
```

Sortie attendue (exemple):
```
Name: ft_package
Version: 0.0.1
Summary: A sample test package
Home-page: https://github.com/eagle/ft_package
Author: eagle
Author-email: eagle@42.fr
License: MIT
Location: /home/eagle/...
Requires:
Required-by:
Metadata-Version: 2.1
Installer: pip
Classifiers:
Entry-points:
```

## Construction des artefacts

Si vous partez du code source:
```bash
python -m pip install --upgrade build
python -m build
# Les fichiers .tar.gz et .whl apparaissent dans ./dist/
```