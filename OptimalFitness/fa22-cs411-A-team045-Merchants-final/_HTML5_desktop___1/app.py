# input string "Splits, Push-1, Bench Press, Bench Press, Bench Press"

# output list of strings ["Splits", "Push-1", "Bench Press", "Bench Press", "Bench Press"]
from flask import Flask, request, render_template, url_for, redirect, session
import sys
import random
import db as db
import save as save

# #joe mama, 78, 180, bulk, Carrots, 34

#text = ""
split_id_count = random.randint(1001, 99999)
global_curr_user = []
#name, customer id, calories, split id
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get-text', methods=['GET', 'POST'])
def req():
    #if(request)
    if(request.form['submit_button'] == 'submit'):
        text = request.form['test']
        text = parse_input(text) #name, height, weight, goals, favorite food, age
        cals = calculate_calories(text[2], text[1], text[5])
        #print(db.get_max_customer_id('customers'))
        cur_cus_id = (db.get_max_customer_id('customers'))[0] + 1
        cur_split_id = split_id_count
        global_curr_user = [cur_cus_id] + [text[1]] + [text[2]] + [text[0]] + [text[5]] + [text[3]] + [cals] + [cur_split_id] + [text[4]]
        db.insert_db(global_curr_user, 'customers')
        #db.update_db(text) #TODO: update db
        return redirect(url_for('frame_1'))

@app.route('/frame_1', methods=['GET', 'POST'])
def frame_1():
    #global_curr_user = db.get_user(id, table_name)
    #print(global_curr_user, file=sys.stderr)
    curr_user_id = (db.get_max_customer_id('customers'))[0]
    #print(curr_user_id, file=sys.stderr)
    global_curr_user = (db.get_user(curr_user_id, 'customers'))[0]
    #print(global_curr_user, file=sys.stderr)
    return render_template('frame_1.html', name = global_curr_user[3],customer_id = global_curr_user[0],  cals = global_curr_user[6], split_id = global_curr_user[7])
        
@app.route('/frame_1/get-text', methods=['GET', 'POST'])
def frame_1_req():
    if(request.form['submit_button'] == 'food'):
        # text = request.form['test']
        # text = parse_input(text)
        # #db.update_db(text) #TODO: update db
        return redirect(url_for('frame_2'))

    if(request.form['submit_button'] == 'update_split'):
        # text = request.form['test']
        # text = parse_input(text)
        # #db.update_db(text) #TODO: update db
        return redirect(url_for('frame_3'))

    if(request.form['submit_button'] == 'same_split'):
        # text = request.form['test']
        # text = parse_input(text)
        # #db.update_db(text) #TODO: update db
        return redirect(url_for('frame_4'))

@app.route('/frame_2', methods=['GET', 'POST'])
def frame_2():
    return render_template('frame_2.html')

@app.route('/frame_2/get-text', methods=['GET', 'POST'])
def frame_2_req():
    if(request.form['submit_button'] == 'submit'):
        text = request.form['test']
        text = parse_input(text) #food
        print(text, file=sys.stderr)
        res = db.search_db(text, 'food_table')
        print(res, file=sys.stderr)
        if res == None:
            return redirect(url_for('frame_1'))
        curr_user_id = (db.get_max_customer_id('customers'))[0]
        global_curr_user = list((db.get_user(curr_user_id, 'customers'))[0])
        print(global_curr_user, file=sys.stderr)
        new_cals = global_curr_user[6] - res[0][1]
        global_curr_user[6] = new_cals
        db.update_db(global_curr_user, 'customers')
        # #db.update_db(text) #TODO: update db
        return redirect(url_for('frame_1'))

    if(request.form['submit_button'] == 'find_food'):
        text = request.form['test']
        text = parse_input(text)
        print(text, file=sys.stderr)
        xd = db.work_around(text[0], text[1])
        # text = request.form['test']
        # text = parse_input(text)
        # #db.update_db(text) #TODO: update db
        return redirect(url_for('frame_5'))

@app.route('/frame_3', methods=['GET', 'POST']) #update split
def frame_3():
    curr_user_id = (db.get_max_customer_id('customers'))[0]
    global_curr_user = (db.get_user(curr_user_id, 'customers'))[0]
    print(global_curr_user, file=sys.stderr)
    display_split = (db.search_db([global_curr_user[7]], 'splits'))
    print(display_split, file=sys.stderr)
    return render_template('frame_3.html', split = display_split)

@app.route('/frame_3/get-text', methods=['GET', 'POST'])
def frame_3_req():
    if(request.form['submit_button'] == 'submit'):
        text = request.form['test']
        text = parse_input(text) #workout 1, workout 2, workout 3, workout 4, workout 5, workout 6, workout 7
        curr_user_id = (db.get_max_customer_id('customers'))[0]
        global_curr_user = (db.get_user(curr_user_id, 'customers'))[0]
        text = [global_curr_user[7]] + text
        while(len(text) < 8):
            text.append("")
        db.insert_db(text, 'splits')
        # text = request.form['test']
        # text = parse_input(text)
        # #db.update_db(text) #TODO: update db
        return redirect(url_for('frame_1'))

@app.route('/frame_4', methods=['GET', 'POST'])
def frame_4():
    splits = db.common_splits()
    return render_template('frame_4.html', splits = splits)

@app.route('/frame_5', methods=['GET', 'POST'])
def frame_5():
    xd = db.get_work_around()
    print(xd, file=sys.stderr)
    store = db.stored_procedure(xd[0][0], xd[0][1])
    return render_template('frame_5.html', foods = store)


    


def get_global_curr_user():
    return global_curr_user

def calculate_calories(weight, height, age):
    #print(weight,height, age, file=sys.stderr)
    bmr = 655 + ((9.6 * float(weight))/ 2.2) + (1.8 * float(height) * 2.54) - (4.7 * float(age))
    #bmr = 10
    return int(bmr*1.5)


def parse_input(input_string):
    return [x.strip() for x in input_string.split(',')]

def update_db(input_string):
    return
def get_exercise_list():
    # parse input
    exercise_list = parse_input(text)
    # return list
    #print(exercise_list, file=sys.stderr)
    return exercise_list 

if __name__ == '__main__':
    app.run()

#get_exercise_list()


#def get