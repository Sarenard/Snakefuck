# Layout mémoire du brainfuck

(potentiel changement : boites plus grandes ? 1024 semble beaucoup mais serait bien.)
La tape est composée de boites de taille 64 cases.
On alterne des boites de travail et des boites "utiles" qui sont des objets.
Les boites de travail sont 0 par défaut.
Les boites utiles sont documentées ici

(potentiel changement : 64? est-ce vraiment utile?)
Les pointeurs vers les boites sont de taille 4 cases (32 bits).

(potentiel changement : anchor de 2 cases? de n cases?)
La première case de chaque boite est dédiée à une éventuelle anchor.

(potentiel changement : fix ça)
Aucun clean mémoire n'est prévu.

## Boite 0

case 0 : anchor de début de boite (toujours 255)
case 1 : anchor signifiant l'usage de la boite (0 = première boite)
(L'allocateur mémoire ne free jamais et croit juste)
case 2-5 : pointeur vers la prochaine case libre 
reste : non spécifié pour l'instant (servira aux calculs locaux)

## Definition : Stack Frame (PyFrameObject)

case 0 : anchor de début de boite (toujours 255)
case 1 : anchor signifiant l'usage de la boite (1 = FrameObject)

Une stackframe contient ces objets :

- f_back       : PyFrameObject *
- f_code       : PyCodeObject *
- f_builtins   : DictObject *
- f_globals    : DictObject *
- f_locals     : DictObject *
- f_valuestack : PyObject ** (List de PyObject*)
- f_stacktop   : PyObject *
- f_iblock     : Int32
- f_executing  : Int32

## Definition : Pointeur

case 0 : anchor de début de boite (toujours 255)
case 1 : anchor signifiant l'usage de la boite (6 = Pointeur vers qq chose)
case 2-5 : pointeur effectif de la boite vers laquelle on pointe
case 6 : 1 ssi élément suivant
case 7-10 : pointeur vers l'élément suivant, si il y en a un, 0 sinon
case 11 : 1 ssi élément précédent
case 12-15 : pointeur vers l'élément précédent, si il y en a un, 0 sinon

## Definition : PyCodeObject

case 0 : anchor de début de boite (toujours 255)
case 1 : anchor signifiant l'usage de la boite (2 = PyCodeObject)

Du bytecode, voir BYTECODE.md (TODO : l'écrire)

## Definition : DictObject
Note : ce n'est pas un dict python ! (ça nous permet d'éviter de l'autoréférencement plus tard)

case 0 : anchor de début de boite (toujours 255)
case 1 : anchor signifiant l'usage de la boite (3 = DictObject)
case 2-(2 + (4*2)*7 - 1 )=57 liste de paires de pointeurs (nom, valeur)
case 58 : vide (padding)
case 59 : 1 ssi le dict continue plus loin
case 60-63 : pointeur vers la suite

## Definition : PyObject

case 0 : anchor de début de boite (toujours 255)
case 1 : anchor signifiant l'usage de la boite (4 = PyObject)
case 2 : tag donnant le type d'objet (voir TAG.md)
case 3-6 : pointeur vers le contenu (on fait tjrs un pointeur même pour smallint)

## definition : Int32

case 0 : anchor de début de boite (toujours 255)
case 1 : anchor signifiant l'usage de la boite (5 = Int32)
case 2-5 : valeur du Int32
