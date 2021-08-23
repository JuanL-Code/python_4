def run():


    #Primeros 1000 raices de naturales con solo 2 digitos decimales
    my_dict = {i : round(i**0.5,2) for i in  range(1,1001)}

    print(my_dict)

if __name__=='__main__':
    run()

