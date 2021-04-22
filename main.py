def extractInfo(file):
    f = open("scp_txts/" + file, "r")
    data = f.readlines()
    f.close()
    new_data = [x[:-1] for x in data]
    return new_data


def extractRowsAndColumns(data):
    rows, columns = data[0].split()
    rows = int(rows)
    columns = int(columns)
    return rows, columns 

def extractCosts(data, columns):
    start_of_costs = 1
    end_of_costs = columns // 12 + 1
    
    costs = data[start_of_costs:end_of_costs+1] # extract all the info first



    string = ""
    for line in costs:
        string += line
    
    costs = string.split()
    return costs, end_of_costs
    
def extractSets(data,end_of_costs):
    start_of_sets = end_of_costs + 1
    end_of_sets = len(data)

    setsInfo = data[start_of_sets:end_of_sets]

    size_of_sets = []
    sets = []

    i = 0
    while i < len(setsInfo):
        value = int(setsInfo[i])
        if value > 0 and value <= 12:
            size_of_sets.append(value)
                
            temp = setsInfo[i+1]

            sets.append(temp)

            i += 2
        elif value > 12 and value <= 24:
            size_of_sets.append(value)

            temp = setsInfo[i+1]
            temp2 = setsInfo[i+2]
            concatenation = temp + temp2

            sets.append(concatenation)
            i += 3 
        elif value > 24 and value <= 36:
            size_of_sets.append(value)

            temp = setsInfo[i+1]
            temp2 = setsInfo[i+2]
            temp3 = setsInfo[i+3]
            concatenation = temp + temp2 + temp3
                
            sets.append(concatenation)
            i += 4
        elif value < 36 and value <= 48:
            size_of_sets.append(value)

            temp = setsInfo[i+1]
            temp2 = setsInfo[i+2]
            temp3 = setsInfo[i+3]
            temp4 = setsInfo[i+4]
            concatenation = temp + temp2 + temp3 + temp4 
                
            sets.append(concatenation)
            i += 5
        elif value > 48 and value <= 60:
            size_of_sets.append(value)

            temp = setsInfo[i+1]
            temp2 = setsInfo[i+2]
            temp3 = setsInfo[i+3]
            temp4 = setsInfo[i+4]
            temp5 = setsInfo[i+5]
            concatenation = temp + temp2 + temp3 + temp4 + temp5
                
            sets.append(concatenation)
            i += 6
        elif value > 60 and value <= 72:
            size_of_sets.append(value)

            temp = setsInfo[i+1]
            temp2 = setsInfo[i+2]
            temp3 = setsInfo[i+3]
            temp4 = setsInfo[i+4]
            temp5 = setsInfo[i+5]
            temp6 = setsInfo[i+6]
            concatenation = temp + temp2 + temp3 + temp4 + temp5 + temp6
                
            sets.append(concatenation)
            i += 7
        elif value > 72 and value <= 84:
            size_of_sets.append(value)

            temp = setsInfo[i+1]
            temp2 = setsInfo[i+2]
            temp3 = setsInfo[i+3]
            temp4 = setsInfo[i+4]
            temp5 = setsInfo[i+5]
            temp6 = setsInfo[i+6]
            temp7 = setsInfo[i+7]
            concatenation = temp + temp2 + temp3 + temp4 + temp5 + temp6 + temp7
                
            sets.append(concatenation)
            i += 8
        elif value > 84 and value <= 96:
            size_of_sets.append(value)

            temp = setsInfo[i+1]
            temp2 = setsInfo[i+2]
            temp3 = setsInfo[i+3]
            temp4 = setsInfo[i+4]
            temp5 = setsInfo[i+5]
            temp6 = setsInfo[i+6]
            temp7 = setsInfo[i+7]
            temp8 = setsInfo[i+8]
            concatenation = temp + temp2 + temp3 + temp4 + temp5 + temp6 + temp7 + temp8
                
            sets.append(concatenation)
            i += 9
    return size_of_sets, sets

if __name__ == "__main__":
    
    data = extractInfo("scp42.txt")
    """ --------------------------------"""

    rows, columns = extractRowsAndColumns(data) # NUMERO DE FILAS Y COLUMNAS
    
    """ --------------------------------"""

    costs, end_of_costs = extractCosts(data,columns) # ARREGLO DE COSTOS
    """ --------------------------------"""

    size_of_sets, sets  = extractSets(data,end_of_costs) # EL TAMAÑO DE CADA CONJUNTO Y LOS ELEMENTOS QUE TIENE CADA UNO
    print(sets)
    """ --------------------------------"""
    # TODO: CPLEX VA A EMPEZAR AQUI