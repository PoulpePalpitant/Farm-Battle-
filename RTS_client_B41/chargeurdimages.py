# changer pour changeurdimages

from tkinter import PhotoImage
    # toutes les images devraient �tre ins�r�es ici    
def chargerimages():
    images={
            'javelotGH':PhotoImage(file='./images/divers/javelotGH.png'),
            'javelotGB':PhotoImage(file='./images/divers/javelotGB.png'),
            'javelotDH':PhotoImage(file='./images/divers/javelotDH.png'),
            'javelotDB':PhotoImage(file='./images/divers/javelotDB.png'),
            'cerfD':PhotoImage(file='./images/animal/cerfD.png'),
            'cerfG':PhotoImage(file='./images/animal/cerfG.png'),
            'cheval':PhotoImage(file='./images/animal/cheval.png'),
            'chevalG':PhotoImage(file='./images/animal/chevalG.png'),
            'daimMORT':PhotoImage(file='./images/animal/daimMORT.png'),
            'daimDB':PhotoImage(file='./images/animal/daimDB.png'),
            'daimDH':PhotoImage(file='./images/animal/daimDH.png'),
            'daimGB':PhotoImage(file='./images/animal/daimGB.png'),
            'daimGH':PhotoImage(file='./images/animal/daimGH.png'),
            'ours60_db':PhotoImage(file='./images/animal/ours60_db.png'),
            'ours60_dh':PhotoImage(file='./images/animal/ours60_dh.png'),
            'ours60_gb':PhotoImage(file='./images/animal/ours60_gb.png'),
            'ours60_gh':PhotoImage(file='./images/animal/ours60_gh.png'),
            'arbre0grand':PhotoImage(file='./images/arbre/arbre0grand.png'),
            'arbre0petit':PhotoImage(file='./images/arbre/arbre0petit.png'),
            'arbre1grand':PhotoImage(file='./images/arbre/arbre1grand.png'),
            'arbre2grand':PhotoImage(file='./images/arbre/arbre2grand.png'),
            'arbresapin0grand':PhotoImage(file='./images/arbre/arbresapin0grand.png'),
            'arbresapin0petit':PhotoImage(file='./images/arbre/arbresapin0petit.png'),
            'baiegrand':PhotoImage(file='./images/arbuste/arbustebaiesgrand.png'),
            'baiepetit':PhotoImage(file='./images/arbuste/arbustebaiespetit.png'),
            'baievert':PhotoImage(file='./images/arbuste/arbustevert.png'),
            'aureusbrillant':PhotoImage(file='./images/aureus/aureusbrillant.png'),
            'aureusD_':PhotoImage(file='./images/aureus/aureusD_.png'),
            'aureusG':PhotoImage(file='./images/aureus/aureusG.png'),
            'aureusrocgrand':PhotoImage(file='./images/aureus/aureusrocgrand.png'),
            'aureusrocmoyen':PhotoImage(file='./images/aureus/aureusrocmoyen.png'),
            'aureusrocpetit':PhotoImage(file='./images/aureus/aureusrocpetit.png'),
            'B_abri':PhotoImage(file='./images/bleu/B_abri.png'),
            'B_maison':PhotoImage(file='./images/bleu/B_maison.png'),
            'B_ouvrierD':PhotoImage(file='./images/bleu/B_ouvrierD.png'),
            'B_ouvrierG':PhotoImage(file='./images/bleu/B_ouvrierG.png'),
            'gazonfond':PhotoImage(file='./images/divers/gazonfond.png'),
            'quaiD':PhotoImage(file='./images/divers/quaiD.png'),
            'quaiG':PhotoImage(file='./images/divers/quaiG.png'),
            'eau':PhotoImage(file='./images/eau/eau.png'),
            'eaugrand':PhotoImage(file='./images/eau/eaugrand.png'),
            'eaugrand1':PhotoImage(file='./images/eau/eaugrand1.png'),
            'eaugrand2':PhotoImage(file='./images/eau/eaugrand2.png'),
            'eaugrand3':PhotoImage(file='./images/eau/eaugrand3.png'),
            'eaujoncD':PhotoImage(file='./images/eau/eaujoncD.png'),
            'eaujoncG':PhotoImage(file='./images/eau/eaujoncG.png'),
            'eaumoyen':PhotoImage(file='./images/eau/eaumoyen.png'),
            'eaupetit':PhotoImage(file='./images/eau/eaupetit.png'),
            'eauquenouillesD':PhotoImage(file='./images/eau/eauquenouillesD.png'),
            'eauquenouillesG':PhotoImage(file='./images/eau/eauquenouillesG.png'),
            'eauquenouillesgrand':PhotoImage(file='./images/eau/eauquenouillesgrand.png'),
            'eautourbillon':PhotoImage(file='./images/eau/eautourbillon.png'),
            'eautroncs':PhotoImage(file='./images/eau/eautroncs.png'),
            'culturegrand':PhotoImage(file='./images/ferme/culturegrand.png'),
            'culturemoyen':PhotoImage(file='./images/ferme/culturemoyen.png'),
            'culturepetit':PhotoImage(file='./images/ferme/culturepetit.png'),
            'J_abri':PhotoImage(file='./images/jaune/J_abri.png'),
            'J_maison':PhotoImage(file='./images/jaune/J_maison.png'),
            'J_ouvrierD':PhotoImage(file='./images/jaune/J_ouvrierD.png'),
            'J_ouvrierG':PhotoImage(file='./images/jaune/J_ouvrierG.png'),
            'marais1':PhotoImage(file='./images/marais/marais1.png'),
            'marais2':PhotoImage(file='./images/marais/marais2.png'),
            'marais3':PhotoImage(file='./images/marais/marais3.png'),
            'roches1 grand':PhotoImage(file='./images/roche/roches1 grand.png'),
            'roches1petit':PhotoImage(file='./images/roche/roches1petit.png'),
            'roches2grand':PhotoImage(file='./images/roche/roches2grand.png'),
            'roches2petit':PhotoImage(file='./images/roche/roches2petit.png'),
            'roches3grand':PhotoImage(file='./images/roche/roches3grand.png'),
            'roches3petit':PhotoImage(file='./images/roche/roches3petit.png'),
            'roches4grand':PhotoImage(file='./images/roche/roches4grand.png'),
            'roches4petit':PhotoImage(file='./images/roche/roches4petit.png'),
            'roches5grand':PhotoImage(file='./images/roche/roches5grand.png'),
            'R_abri':PhotoImage(file='./images/rouge/R_abri.png'),
            'R_maison':PhotoImage(file='./images/rouge/R_maison.png'),
            'R_ouvrierD':PhotoImage(file='./images/rouge/R_ouvrierD.png'),
            'R_ouvrierG':PhotoImage(file='./images/rouge/R_ouvrierG.png'),
            'V_abri':PhotoImage(file='./images/vert/V_abri.png'),
            'V_maison':PhotoImage(file='./images/vert/V_maison.png'),
            'V_ouvrierD':PhotoImage(file='./images/vert/V_ouvrierD.png'),
            'V_ouvrierG':PhotoImage(file='./images/vert/V_ouvrierG.png'),
            'V_chickenD':PhotoImage(file='./images/vert/V_chickenD.png'),
            'V_chickenG':PhotoImage(file='./images/vert/V_chickenG.png'),
            'J_chickenD':PhotoImage(file='./images/jaune/J_chickenD.png'),
            'J_chickenG':PhotoImage(file='./images/jaune/J_chickenG.png'),
            'B_chickenD':PhotoImage(file='./images/bleu/B_chickenD.png'),
            'B_chickenG':PhotoImage(file='./images/bleu/B_chickenG.png'),
            'R_chickenD':PhotoImage(file='./images/rouge/R_chickenD.png'),
            'R_chickenG':PhotoImage(file='./images/rouge/R_chickenG.png'),
            'V_chickenCoop':PhotoImage(file='./images/vert/V_chickenCoop.png'),
            'J_chickenCoop':PhotoImage(file='./images/jaune/J_chickenCoop.png'),
            'B_chickenCoop':PhotoImage(file='./images/bleu/B_chickenCoop.png'),
            'R_chickenCoop':PhotoImage(file='./images/rouge/R_chickenCoop.png'),
            'V_pigPen':PhotoImage(file='./images/vert/V_pigPen.png'),
            'B_pigPen':PhotoImage(file='./images/bleu/B_pigPen.png'),
            'J_pigPen':PhotoImage(file='./images/jaune/J_pigPen.png'),
            'R_pigPen':PhotoImage(file='./images/rouge/R_pigPen.png'),
            'V_pigD':PhotoImage(file='./images/vert/V_pigD.png'),
            'V_pigG':PhotoImage(file='./images/vert/V_pigG.png'),
            'B_pigD':PhotoImage(file='./images/bleu/B_pigD.png'),
            'B_pigG':PhotoImage(file='./images/bleu/B_pigG.png'),
            'J_pigD':PhotoImage(file='./images/jaune/J_pigD.png'),
            'J_pigG':PhotoImage(file='./images/jaune/J_pigG.png'),
            'R_pigD':PhotoImage(file='./images/rouge/R_pigD.png'),
            'R_pigG':PhotoImage(file='./images/rouge/R_pigG.png'),
            'silo':PhotoImage(file='./images/xxxbatiment/silo.png'),
            'B_silo':PhotoImage(file='./images/xxxbatiment/B_silo.png'),
            'J_silo':PhotoImage(file='./images/xxxbatiment/J_silo.png'),
            'R_silo':PhotoImage(file='./images/xxxbatiment/R_silo.png'),
            'V_silo':PhotoImage(file='./images/xxxbatiment/V_silo.png')}
    return images



def loadGif():
    gifs = {}
    sprites = ["poissons.gif"]
    path = './images/GIFS/'

    for name in sprites:
        spriteImages = []
        truthTest = True
        noindex = 0

        while truthTest:
            try:
                img = PhotoImage(file = path + name, format="gif -index " + str(noindex)) # ne réussit jamais à passer somehow
                spriteImages.append(img)
                noindex+=1

            except Exception:
                truthTest = False
                gifs[name[:-4]] = spriteImages

    return gifs 

if __name__ == '__main__':
    print( loadGif())
