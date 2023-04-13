# -*- coding: utf-8 -*-

def check_files():
    i_file=input("Zadejte název vstupního textového souboru(bez .txt):")
    o_file=input("Zadejte název výstupního textového souboru(bez .txt):")
    try:
        file_group_numbers(i_file, o_file)
        print("\nSoubor úspěšně vytvořen.")
    except FileNotFoundError:
            print("\nVstupní soubor nenalezen.")
    except ValueError:
            print("\nŠpatně zadaná data ve vstupním souboru.")
            
def file_group_numbers(i_file,o_file):
    input_file=open(i_file+".txt")
    try:
        output_file=open(o_file+".txt","w")
        try:
            line = input_file.readline()
            while line != "":
                stripped_line=line.strip()
                line_list=stripped_line.split()
                new_list= [int(number) for number in line_list]
                line_sum=sum(new_list)
                output_file.write(str(line_sum))
                output_file.write("\n")
                line = input_file.readline()
        finally:
            output_file.close()
    finally:
        input_file.close() 

check_files()






    