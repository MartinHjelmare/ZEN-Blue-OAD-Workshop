import csv
from System import Array

def Conv2Array(filename, rowoffset, delim):
 
    legnames = [];
    data = []
    for row in csv.reader(open(filename), delimiter=delim):
        data.append(row)
    
    headers = data[0] # contains the column names
    
    # determine the number of measured parameters
    numvar = len(headers)
    # determine the number of rows of the CSV table
    numrows = len(data)
    entries = numrows-1
    print 'Number of Vars    :', numvar
    print 'Number of Entries :', entries
    
    # initialize 2D array to store all parameter values 
    values = Array.CreateInstance(float, numrows-rowoffset, numvar)
    # define empty list with ... entries
    typelist = [None] * numvar
    
    # write values from table into array 
    for i in range(0, numrows-rowoffset,1 ):
        
        # write the data into array
        tmp = data[i+rowoffset]
        for k in range(0,len(tmp),1):
            # convert "," to "."
            tmp[k] = str.replace(tmp[k], ',','.')
            try:        
                values[i,k] = float(tmp[k])
                if (i==0):
                   typelist[k] = 'float' # type of data for current column = float
            except:
                values[i,k] = float('nan')
                if (i==0):
                    typelist[k] = 'str' # type of data for current column = str
    
    print typelist
    
    # create legend names             
    for i in range (0, numvar, 1):
        legname_tmp = headers[i]    
        legnames.append(legname_tmp)
    
    return values, legnames, numvar, entries, typelist

def Conv2List(filename, rowoffset, delim, column):
    
    legnames = [];
    
    data = []
    for row in csv.reader(open(filename), delimiter=delim):
        data.append(row)
    
    headers = data[0] # contains the column names
    # determine the number of measured parameters and row number
    numvar = len(headers)
    numrows = len(data)
    
    # initialize 2D array to store all parameter values 
    labels = ([])
    
    # write values from table into array 
    for i in range(0, numrows-rowoffset, 1 ):
    
        tmp = data[i+rowoffset]
        labels.append(tmp[column])
    # create legend names             
    for i in range (0, numvar, 1):
        legname_tmp = headers[i]    
        legnames.append(legname_tmp)
    
    return labels

def CreateTable(data, col, rows, legends, startcol, tablename, typelist, table):
    
    # Create new table
    #table = ZenTable(tablename)
    
    for i in range(startcol, col, 1):
        
        print 'Column Type : ',typelist[i]
        if (typelist[i] == 'float'):
            table.Columns.Add(legends[i], float)
        if (typelist[i] == 'str'):
            table.Columns.Add(legends[i], str)
      
    # Write meta data values in table
    for r in range(0,rows,1):
        table.Rows.Add()
        for c in range(0, col-startcol,1):
            #set values for cells
            table.SetValue(r, c, data[r,c+startcol])
    
    print 'Table created.'
    
    return table


def AddLabels(table, labels, numrows, col2insert):

    for r in range(0,numrows,1):
        table.SetValue(r, col2insert,labels[r])
    
    return table

    
def ReadResultTable(filename, rowoffset, delim, tablename, table):
    
    # Get the Results Table from Fiji
    ValuesArray, Legends, numvar, entries, coltypelist = Conv2Array(filename, rowoffset, delim)
    table = CreateTable(ValuesArray, numvar, entries, Legends, 1, tablename, coltypelist, table)
    # Read the slice or frame labels separately since those are strings
    labels = Conv2List(filename, rowoffset, delim, 1)
    # Add them to the Zen table to replace the NaNs
    table = AddLabels(table, labels, entries, 0)
    
    return table

