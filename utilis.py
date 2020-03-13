# Code jeu de la vie.
def calcul_nb_voisins(Z):
    """
    la fonction calcul_nb_voisins reçoit en entrée une liste de liste
       et renvoie le nombre de voisin(s) de chaque cellule en appliquant les règles du jeu. 
    """
    forme = len(Z), len(Z[0])
    N = [[0, ] * (forme[0]) for i in range(forme[1])]
    for x in range(1, forme[0] - 1):
        for y in range(1, forme[1] - 1):
            N[x][y] = Z[x-1][y-1]+Z[x][y-1]+Z[x+1][y-1] \
                + Z[x-1][y] + 0 +Z[x+1][y] \
                + Z[x-1][y+1]+Z[x][y+1]+Z[x+1][y+1]
    return N
               #####################################################
    
def iteration_jeu(Z):
    forme = len(Z), len(Z[0])
    N = calcul_nb_voisins(Z)
    for x in range(1,forme[0]-1):
        for y in range(1,forme[1]-1):
            if Z[x][y] == 1 and (N[x][y] < 2 or N[x][y] > 3):
                Z[x][y] = 0
            elif Z[x][y] == 0 and N[x][y] == 3:
                Z[x][y] = 1
return Z
    ####################################################
    
    
def calcul_nb_voisins_np(Z):
    
    """Calcul du nombre de voisins dans une grille grâce au slicing
    
    Entrée: Une matrice carrée composée de 1 et de 0
       
    Sortie: Le nombre de voisins de chaque cellule sauf pour le bord
    
    """
    
    Z = np.array(Z)
    nb_voisins_np = np.zeros(Z.shape) # matrice de la même dimension que Z remplie de zéros
    # chaque cellule est au plus entourée de 8 cellules
    #il nous faut sommer chacune de ces 8 cellules:
    nb_voisins_np[1:-1, 1:-1] = Z[1:-1, :-2] + \
    Z[:-2, :-2] + Z[:-2, 2:] + Z[2:, 2:] + Z[2:, :-2] + \
    Z[1:-1, 2:] + Z[:-2, 1:-1] + Z[2:, 1:-1]
    return(nb_voisins_np)
    
        ####################################################################################
    
 def mon_animation(Z_in, nb_iter):
    
    fig = plt.imshow(Z_in)
    plt.show()
    plt.title("Animation du jeu")
    

    def animate(nb_iters):
        fig.set_data(jeu_np(np.array(Z_in), nb_iters))
        return fig
    gif = animation.FuncAnimation(plt.figure(), animate, frames=nb_iter)
    return(gif)  
