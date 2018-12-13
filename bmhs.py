#import pdb;pdb.set_trace()

def search_letter_in_pattern(pattern,letter):
    """
    Reemplazo de la tabla del last character del articulo
    """
    m = len(pattern)
    count = 1

    for i in range(m-1,-1,-1):
        if letter==pattern[i]:
            return count
        
        count = count+1
    
    return -1


def boyern_sunday(text,pattern):
    conincidencia = 0
    n = len(text)
    m = len(pattern)
    j = m-1
    i = m-1
    iteraciones = 0

    while(i<=n-1):
        if j==m-1:
            h = i  #el valor mas ala derecha 
        
        
        if text[i]==pattern[j]:
            
            if j==0:
                
                conincidencia = conincidencia+1
                
                
                j = m-1
                #Si suma i+m queda en el limite inferior del siguiente a preguntar pero realmente necesita
                #quedar en limite superior para moverse ala izquierda
                i = (i+m-1)+j
                iteraciones = iteraciones+1
                
            else:
                i = i-1
                j = j-1
        else:

            #Si entra aqui es por que el ultimo ya no converge y no hay necesidad de comparar mas
            if h==n-1:
                return conincidencia


            j = m-1
            #Busca la letra dentro del patron si no se encuentra devuelve -1
            l  = search_letter_in_pattern(pattern,text[h+1])
            
           

            if l<0:
                #el movimiento siguiente es  la cantidad del patron +1
                i = h+m+1
                iteraciones = iteraciones+1
                
            else:
                #Si encuentra una letra , el movimiento es la cantidad  es el numero de la letra
                i = h+l
                iteraciones = iteraciones+1
    
  
   
    return conincidencia
        



print(boyern_sunday("jairo jandresja","kl"))





