import csv
import glob
full_new_db = []

data = []
variables = []
JnJ_check = []
index = []
l1 = []
dups = []
dups_index = []
dups_index_full = []
left_3_vars = []
new_db = []

path = "C:/Users/wburke/Documents/PythonProjects/AssetTracker/pulled for program/*.csv"



def full_send():
    for i in variables:
        if i not in l1:
            l1.append(i)
            unique_index = variables.index(i)
            index.append(unique_index)
        else:
            if i not in dups:
                dups.append(i)
                var1 = [x for x, e in enumerate(variables) if e == i]
                dups_index.append(var1)
                dups_index_full.append([i, var1])
            else:
                pass

    length = len(variables)

    #new_db = []

    for i in range(0, length):
        new_row = []
        if i in index:
            working_var = data[i]
            #new sample
            new_row.append(left_3_vars[0])
            new_row.append(left_3_vars[1])
            new_row.append(left_3_vars[2])
            #end new sample
            new_row.append(working_var[3])
            new_row.append(working_var[4])
            new_row.append(working_var[7])
            new_row.append(working_var[9])
            new_row.append(working_var[20])
            new_row.append(working_var[18])
            new_row.append(working_var[26])
            new_row.append(working_var[27])
            new_db.append(new_row)
        else:
            for lists in dups_index:
                if i in lists:
                    already_saved_var = lists[0]
                    asset_name_ASV = variables[already_saved_var]
                    index_AN_ASV = variables.index(asset_name_ASV)
                    new_indication = data[i][18]

                    for row in new_db:
                        if asset_name_ASV in row:
                            index_in_new_db = row.index(asset_name_ASV)
                            row[8] = row[8] + " / " + new_indication
                        else:
                            pass
                else:
                    pass
    #print(new_db)
    #full_new_db.append(new_db)
    '''with open(excel_output_name + '.csv', 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerows(new_db)'''

def JNJ():
    jnj_name = "Johnson & Johnson"
    jnj_name_2 = "JNJ"
    jnj_name_3 = "Janssen"
    for i in variables:
        if i not in l1:
            l1.append(i)
            unique_index = variables.index(i)
            index.append(unique_index)
        else:
            if i not in dups:
                dups.append(i)
                var1 = [x for x, e in enumerate(variables) if e == i]
                dups_index.append(var1)
                dups_index_full.append([i, var1])
            else:
                pass

    length = len(variables)

    #new_db = []

    for i in range(0, length):
        if i == 0 or data[i][7] == (jnj_name or jnj_name_2 or jnj_name_3) or data[i][9] == (jnj_name or jnj_name_2 or jnj_name_3):
            new_row = []
            if i in index:
                working_var = data[i]
                new_row.append(left_3_vars[0])
                new_row.append(left_3_vars[1])
                new_row.append(left_3_vars[2])
                new_row.append(working_var[3])
                new_row.append(working_var[4])
                new_row.append(working_var[7])
                new_row.append(working_var[9])
                new_row.append(working_var[20])
                new_row.append(working_var[18])
                new_row.append(working_var[26])
                new_row.append(working_var[27])
                new_db.append(new_row)
            else:
                for lists in dups_index:
                    if i in lists:
                        already_saved_var = lists[0]
                        asset_name_ASV = variables[already_saved_var]
                        index_AN_ASV = variables.index(asset_name_ASV)
                        new_indication = data[i][18]

                        for row in new_db:
                            if asset_name_ASV in row:
                                index_in_new_db = row.index(asset_name_ASV)
                                row[8] = row[8] + " / " + new_indication
                            else:
                                pass
                    else:
                        pass
        else:
            pass
    #full_new_db.append(new_db)
    '''with open(excel_output_name + '.csv', 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerows(new_db)'''

def need_jnj():
    if ("Johnson & Johnson" or "Janssen" or "JNJ" or "Johnson and Johnson") in JnJ_check:
        JNJ()
        print("JNJ check positive")
    else:
        full_send()
        print("sent")


for fname in glob.glob(path):
    excel_file = fname
    excel_file = excel_file[73:-4]
    # excel_output_name = excel_file + "_output"
    left_3_vars_from_excel = excel_file.split("_")
    left_3_vars = left_3_vars_from_excel
#    left_3_vars.append(left_3_vars_from_excel)
    f = open(fname)
    csv_f = csv.reader(f)

    for row in csv_f:
        data.append(row)
        variables.append(row[3])
        JnJ_check.append(row[7])
        JnJ_check.append(row[9])

    need_jnj()
    data.clear()
    variables.clear()
    JnJ_check.clear()
    index.clear()
    l1.clear()
    dups.clear()
    dups_index.clear()
    dups_index_full.clear()
    left_3_vars.clear()

print(new_db)
with open('output.csv', 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerows(new_db)
