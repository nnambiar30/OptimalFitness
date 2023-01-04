import mysql.connector

mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    database = 'optimal fitness',
    password = 'aryan123'
)

mycursor = mydb.cursor()
# test = ["s", "dosa", "400", "1"]
# sql = (f"INSERT INTO food_table (food_name, calories, servings) VALUES ('{test[1]}', '{test[2]}', '{test[3]}')")
# mycursor.execute(sql)
# mydb.commit()


def update_db(input_string, table_name):
    if(table_name == 'food_table'):
        print("update")
        sql = (f"UPDATE food_table SET calories = '{input_string[1]}' WHERE food_name LIKE '%{input_string[0]}%'")
        mycursor.execute(sql)
        mydb.commit()

    if(table_name == 'splits'):
        sql = (f"UPDATE splits SET workout_1 = '{input_string[1]}', workout_2 = '{input_string[2]}', workout_3 = '{input_string[3]}', workout_4 = '{input_string[4]}', workout_5 = '{input_string[5]}', workout_6 = '{input_string[6]}', workout_7 = '{input_string[7]}' WHERE split_id = '{input_string[0]}'")
        mycursor.execute(sql)
        mydb.commit()

    if(table_name == 'Equipment'):
        sql = (f"UPDATE Equipment SET type = '{input_string[1]}' WHERE equip_name LIKE '%{input_string[0]}%'")
        mycursor.execute(sql)
        mydb.commit()

    if(table_name == 'customers'):
        sql = (f"UPDATE customers SET height = '{input_string[1]}', weight = '{input_string[2]}', name = '{input_string[3]}', age = '{input_string[4]}', goal = '{input_string[5]}', calorie_count = '{input_string[6]}', split_id = '{input_string[7]}', favorite_food = '{input_string[8]}' WHERE customer_id = '{input_string[0]}'")
        mycursor.execute(sql)
        mydb.commit()

    if(table_name == 'exercises'):
        sql = (f"UPDATE exercises SET muscle_group = '{input_string[1]}', sets = '{input_string[2]}', weights = '{input_string[3]}', reps = '{input_string[4]}', equipment_name = '{input_string[5]}' WHERE name LIKE '%{input_string[0]}%'")
        mycursor.execute(sql)
        mydb.commit()



def insert_db(input_string, table_name):
    if(table_name == 'food_table'):
        print("insert")
        sql = (f"INSERT INTO food_table (food_name, calories, servings) VALUES ('{input_string[0]}', '{input_string[1]}', '{input_string[3]}')")
        mycursor.execute(sql)
        mydb.commit()

    if (table_name == 'splits'):
        sql = (f"INSERT INTO splits (split_id,workout_1,workout_2,workout_3,workout_4,workout_5,workout_6,workout_7) VALUES ('{input_string[0]}', '{input_string[1]}', '{input_string[2]}', '{input_string[3]}', '{input_string[4]}', '{input_string[5]}', '{input_string[6]}', '{input_string[7]}')")
        mycursor.execute(sql)
        mydb.commit()

    if(table_name == 'Equipment'):
        sql = (f"INSERT INTO Equipment (equip_name,type) VALUES ('{input_string[0]}', '{input_string[1]}')")
        mycursor.execute(sql)
        mydb.commit() 
    
    if(table_name == 'customers'):
        sql = (f"INSERT INTO customers (customer_id,height,weight,name,age,goal,calorie_count,split_id,favorite_food) VALUES ('{input_string[0]}', '{input_string[1]}', '{input_string[2]}', '{input_string[3]}', '{input_string[4]}', '{input_string[5]}', '{input_string[6]}', '{input_string[7]}', '{input_string[8]}')")
        mycursor.execute(sql)
        mydb.commit() 
    
    if(table_name == 'exercises'):
        sql = (f"INSERT INTO exercises (name,muscle_group,sets,weights,reps,equipment_name) VALUES ('{input_string[0]}', '{input_string[1]}', '{input_string[2]}', '{input_string[3]}', '{input_string[4]}', '{input_string[5]}', '{input_string[6]}')")
        mycursor.execute(sql)
        mydb.commit() 

def delete_db(input_string, table_name):
    if(table_name == 'food_table'):
        sql = (f"DELETE FROM food_table WHERE food_name LIKE '%{input_string[0]}%'")
        mycursor.execute(sql)
        mydb.commit()
    
    if(table_name == 'splits'):
        sql = (f"DELETE FROM splits WHERE split_id = '{input_string[0]}'")
        mycursor.execute(sql)
        mydb.commit()
    
    if(table_name == 'Equipment'):
        sql = (f"DELETE FROM Equipment WHERE equip_name LIKE '%{input_string[0]}%'")
        mycursor.execute(sql)
        mydb.commit()
    
    if(table_name == 'customers'):
        sql = (f"DELETE FROM customers WHERE customer_id = '{input_string[0]}'")
        mycursor.execute(sql)
        mydb.commit()
    
    if(table_name == 'exercises'):
        sql = (f"DELETE FROM exercises WHERE name LIKE '%{input_string[0]}%'")
        mycursor.execute(sql)
        mydb.commit()
    



def search_db(input_string, table_name):
    if(table_name == 'food_table'):
        sql = (f"SELECT * FROM food_table WHERE food_name LIKE '%{input_string[0]}%'")
        print(sql)
        mycursor.execute(sql)
        myresult = mycursor.fetchall()
        return myresult

    if(table_name == 'splits'):
        sql = (f"SELECT * FROM splits WHERE split_id = '{input_string[0]}'")
        mycursor.execute(sql)
        myresult = mycursor.fetchall()
        return myresult

    if(table_name == 'Equipment'):
        sql = (f"SELECT * FROM Equipment WHERE equip_name LIKE '%{input_string[0]}%'")
        mycursor.execute(sql)
        myresult = mycursor.fetchall()
        return myresult
    
    if(table_name == 'customers'):
        sql = (f"SELECT * FROM customers WHERE customer_id = '{input_string[0]}'")
        mycursor.execute(sql)
        myresult = mycursor.fetchall()
        return myresult
    
    if(table_name == 'exercises'):
        sql = (f"SELECT * FROM exercises WHERE name LIKE '%{input_string[0]}%'")
        mycursor.execute(sql)
        myresult = mycursor.fetchall()
        return myresult
    

    
def common_splits():
    mycursor = mydb.cursor(buffered=True)
    print("common splits")
    sql = ('''SELECT spl.split_id, COUNT(spl.split_id)
            FROM Customers cu NATURAL JOIN Splits spl
            GROUP BY spl.split_id
            HAVING COUNT(spl.split_id) > 1
            ORDER BY spl.split_id asc''')
    mycursor.execute(sql)
    mydb.commit()
    myresult = mycursor.fetchall()
    for x in myresult:
        print(x)
    return myresult

def fav_food(input_string):
    mycursor = mydb.cursor(buffered=True)
    print("fav food")
    sql = (f'''SELECT Food_Name, Calories FROM food_table WHERE 
    calories < (SELECT calorie_count FROM customers WHERE customer_id = '{input_string[0]}')

    UNION

    SELECT Food_Name, Calories FROM food_table 
    NATURAL JOIN customers WHERE favorite_food = food_name''')
    mycursor.execute(sql)
    mydb.commit()
    myresult = mycursor.fetchall()
    for x in myresult:
        print(x)
    return myresult

def get_user(id,table_name):
    mycursor = mydb.cursor(buffered=True)
    #print(f"get user with id : {id}")
    sql = (f"select * from {table_name} where customer_id = {id}")
    mycursor.execute(sql)
    mydb.commit()
    myresult = mycursor.fetchall()
    peak_list = []
    for x in myresult:
        peak_list.append(x)
    return peak_list

def get_max_customer_id(table_name):
    mycursor = mydb.cursor(buffered=True)
   # print("get max customer id")
    sql = (f"select max(customer_id) from {table_name}")
    mycursor.execute(sql)
    mydb.commit()
    myresult = mycursor.fetchall()
    peak_list = []
    for x in myresult:
        peak_list.append(x[0])
    return peak_list

def stored_procedure(customer1, customer2):
    mycursor = mydb.cursor(buffered=True)
    print("stored procedure")
    sql = (f"CALL Result({customer1},{customer2})")
    print(sql)
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    mycursor.close()
    peak_list = [] 
    for x in myresult:
        print(x)
        peak_list.append((x[2],x[4]))
    return peak_list

def get_stored_procedure():
    mycursor = mydb.cursor(buffered=True)
    sql = (f"SELECT * FROM newtable")
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    mycursor.close()
    peak_list = []
    for x in myresult:
        peak_list.append((x[2],x[4]))
    return peak_list

def work_around(customer1, customer2):
    mycursor = mydb.cursor(buffered=True)
    sql = (f"CREATE TABLE Temp (customer1 int, customer2 int)")
    mycursor.execute(sql)
    sql = (f"INSERT INTO Temp VALUES ({customer1},{customer2})")
    mycursor.execute(sql)
    mydb.commit()
    return

def get_work_around():
    mycursor = mydb.cursor(buffered=True)
    sql = (f"SELECT * FROM Temp")
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    peak_list = []
    for x in myresult:
        peak_list.append((x[0],x[1]))
    sql = (f"DROP TABLE Temp")
    mycursor.execute(sql)
    mydb.commit()
    return peak_list