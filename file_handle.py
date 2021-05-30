def main():
    
    def value():
        #Create file and open
        archivo = input('Escribi el nombre del archivo: ') + '.txt'

        abrir = open(archivo, 'a')
        #Add words
        added_word = str(input('Escribi lo que quieras añadir al archivo: ').lower() + '\n')

        abrir.write(added_word)

        abrir.close()
        #Print file into screen
        lectura = open(archivo, 'r')

        lectura.close()
        #Print when Helen its mention (Example)
        story = open('story.txt')

        print()
        for line in story:
            if line.startswith('Helen'):  
                print(line.strip())

        story.close()

    value()

if __name__== "__main__":
    main()