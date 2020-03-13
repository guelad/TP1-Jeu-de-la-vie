# TP1-Jeu-de-la-vie

   Introduction
   
Dans le cadre de l'évaluation de l'UE DEVELOPPEMENT (python), nous avons etudier le jeu de la vie qui est un automate cellulaire mise au point par le mathématicien britannique John Horton Conway en 1970.
Malgré des règles très simples, le jeu de la vie est Turing-complet. 
Le jeu de la vie est un jeu au sens mathématique plutôt que ludique. Bien que n'étant pas décrit par la théorie des jeux, certains le décrivent comme un « jeu à zéro joueur ». 

         developpememet 
         
Dans cette partie nous allons mettre en œuvre l’exercice  du TP sous deux paries
Partie1 : Implémentation sans numpy. 
On applique la fonction donnée calcul_nb_voisins à Z pour calculer le nombre de voisins des cellules de Z. A la sortie on obtient N-   nombre_de_voisin. Nous avons aussi comme donnée la fonction iteration_jeu qui applique les règles du jeu sur la graine Z pour donner la génération suivante. On va utiliser la fonction subplot et imshow de matplotlib pour faire l’affichage graphique de certains nombre d’étapes du jeu.

Parie2 : implelentation avec numpy
Dans cette partie on va creer une nouvelle fonction intitulée calcul_nb_voisins_np(Z)  qui prend en entrée une matrice Z et qui retourne le nombre de voisins pour chaque entrée et qui vaut zéro sur le pourtour. On a pu verifier que les resultats ce sont les memes avec la fonction calcul_nb_voisins. Apres ona fait une iteration pour avec une fonction appelée jeu_np.
Nous nous interessons maintenant sur l'animation grace à la matrice Z_huge.




