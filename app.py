from flask import Flask, jsonify, render_template, request, redirect, flash
app = Flask(__name__)

import psycopg2

@app.route('/')
def index():
    return render_template('login1.html')

#logout
@app.route('/login1.html')
def login():
    return render_template('login1.html')

@app.route('/login1')
def login1():
    user=request.form.get('name')
    password=request.form.get('password')
    if user and password:
        return render_template('frame.html')


@app.route('/frame.html')
def frame():   
    return render_template('frame.html')

@app.route('/1_search.html')
def search1():
    return render_template('1_search.html')
@app.route('/1_searchaction/',methods=['POST'])
def search10():
    conn=psycopg2.connect(database="final",user="postgres",password="123")
    data=dict(request.form)
    cur=conn.cursor()
    sql="select * from aircraft where aircraft_code='{aircraft_code}' and departure_airport='{departure_airport}' and arrival_airport='{arrival_airport}'".format(**data)
    cur.execute(sql)
    result=cur.fetchall()
    conn.commit()
    conn.close()
    return render_template('1_list.html',userlist=result)

@app.route('/1_add.html')
def add1():
    return render_template('1_add.html')

@app.route('/1_addaction/',methods=['POST'])
def add10():
    conn=psycopg2.connect(database="final",user="postgres",password="123")
    data = dict (request.form)
    cur=conn.cursor()
    sql = "insert into aircraft values ('{aircraft_code}','{company}','{aircraft_type}','{departure_airport}','{arrival_airport}','{stopover_airport}','{departure_time}','{arrival_time}','{flight_weight}')".format (**data)
    cur.execute(sql)
    conn.commit()
    conn.close()
    return redirect('/1_add.html')

@app.route('/1_list.html')
def list1():
    return render_template('1_list.html')

@app.route('/1_delete')
def del1():
    conn=psycopg2.connect(database="final",user="postgres",password="123")
    aircraft_code=request.args.get('id') 
    cur=conn.cursor()
    cur.execute("delete from aircraft where aircraft_code='{}'".format(aircraft_code))
    conn.commit()
    conn.close()
    return redirect('1_list.html')  

@app.route('/1_update')
def update1():
    code=request.args.get('id')
    conn=psycopg2.connect(database="final",user="postgres",password="123")
    cur=conn.cursor()
    sql="select * from aircraft where aircraft_code='{}'".format(code)
    cur.execute(sql)
    result=cur.fetchall()
    conn.commit()
    conn.close()
    return render_template('1_update.html',userlist=result)

@app.route('/1_updateaction/',methods=['POST'])
def update10():
    conn=psycopg2.connect(database="final",user="postgres",password="123")
    data = dict (request.form)
    cur=conn.cursor()
    sql="update aircraft set company='{company}',aircraft_type='{aircraft_type}',departure_airport='{departure_airport}',arrival_airport='{arrival_airport}',stopover_airport='{stopover_airport}',departure_time='{departure_time}',arrival_time='{arrival_time}',flight_weight='{flight_weight}' where aircraft_code='{aircraft_code}'".format (**data)
    cur.execute(sql)
    sql="select * from aircraft where aircraft_code='{}'".format(data["aircraft_code"])
    cur.execute(sql)
    result=cur.fetchall()
    conn.commit()
    conn.close()        
    return render_template('1_list.html',userlist=result)


#second table operation
@app.route('/2_search.html')
def search2():
    return render_template('2_search.html')
@app.route('/2_searchaction/',methods=['POST'])
def search20():
    conn=psycopg2.connect(database="final",user="postgres",password="123")
    data=dict(request.form)
    cur=conn.cursor()
    sql="select * from aircraft_performance where aircraft_type='{aircraft_type}'".format(**data)
    cur.execute(sql)
    result=cur.fetchall()
    conn.commit()
    conn.close()
    return render_template('2_list.html',userlist=result)

@app.route('/2_add.html')
def add2():
    return render_template('2_add.html')

@app.route('/2_addaction/',methods=['POST'])
def add20():
    conn=psycopg2.connect(database="final",user="postgres",password="123")
    data = dict (request.form)
    cur=conn.cursor()
    sql = "insert into aircraft_performance values ('{aircraft_type}',{max_attitude},{max_fuel_load},{cruise},{climb_rate},{flight_duration},{max_speed},{min_speed},{takeoff_distance},{landing_distance},{safe_disdance})".format (**data)
    cur.execute(sql)
    conn.commit()
    conn.close()
    return redirect('/2_add.html')

@app.route('/2_list.html')
def list2():
    return render_template('2_list.html')

@app.route('/2_delete')
def del2():
    conn=psycopg2.connect(database="final",user="postgres",password="123")
    aircraft_type=request.args.get('id') 
    cur=conn.cursor()
    cur.execute("delete from aircraft_performance where aircraft_type='{}'".format(aircraft_type))
    conn.commit()
    conn.close()
    return redirect('2_list.html')  

@app.route('/2_update')
def update2():
    code=request.args.get('id')
    conn=psycopg2.connect(database="final",user="postgres",password="123")
    cur=conn.cursor()
    sql="select * from aircraft_performance where aircraft_type='{}'".format(code)
    cur.execute(sql)
    result=cur.fetchall()
    conn.commit()
    conn.close()
    return render_template('2_update.html',userlist=result)

@app.route('/2_updateaction/',methods=['POST'])
def update20():
    conn=psycopg2.connect(database="final",user="postgres",password="123")
    data = dict (request.form)
    cur=conn.cursor()

    sql="update aircraft_performance set max_attitude='{max_attitude}',max_fuel_load='{max_fuel_load}',cruise='{cruise}',climb_rate='{climb_rate}',flight_duration='{flight_duration}',max_speed='{max_speed}',min_speed='{min_speed}',takeoff_distance='{takeoff_distance}',landing_distance='{landing_distance}',safe_disdance='{safe_disdance}' where aircraft_type='{aircraft_type}'".format (**data)    
    cur.execute(sql)
    sql="select * from aircraft_performance where aircraft_type='{}'".format(data["aircraft_type"])
    cur.execute(sql)
    result=cur.fetchall()
    conn.commit()
    conn.close()        
    return render_template('2_list.html',userlist=result)




@app.route('/3_search.html')
def search3():
    return render_template('3_search.html')
@app.route('/3_searchaction/',methods=['POST'])
def search30():
    conn=psycopg2.connect(database="final",user="postgres",password="123")
    data=dict(request.form)
    cur=conn.cursor()
    sql="select * from airport where aircraft_code='{name}'".format(**data)
    cur.execute(sql)
    result=cur.fetchall()
    conn.commit()
    conn.close()
    return render_template('3_list.html',userlist=result)

@app.route('/3_add.html')
def add3():
    return render_template('3_add.html')

@app.route('/3_addaction/',methods=['POST'])
def add30():
    conn=psycopg2.connect(database="final",user="postgres",password="123")
    data = dict (request.form)
    cur=conn.cursor()
    sql = "insert into airport values ('{name}','{aircraft_code}','{situation}','{runway}','{sequence}','{wait_time}')".format (**data)
    cur.execute(sql)
    conn.commit()
    conn.close()
    return redirect('/3_add.html')

@app.route('/3_list.html')
def list3():
    return render_template('3_list.html')

@app.route('/3_delete')
def del3():
    conn=psycopg2.connect(database="final",user="postgres",password="123")
    aircraft_code=request.args.get('id') 
    cur=conn.cursor()
    cur.execute("delete from airport where aircraft_code='{}'".format(aircraft_code))
    conn.commit()
    conn.close()
    return redirect('3_list.html')  

@app.route('/3_update')
def update3():
    code=request.args.get('id')
    conn=psycopg2.connect(database="final",user="postgres",password="123")
    cur=conn.cursor()
    sql="select * from airport where aircraft_code='{}'".format(code)
    cur.execute(sql)
    result=cur.fetchall()
    conn.commit()
    conn.close()
    return render_template('3_update.html',userlist=result)

@app.route('/3_updateaction/',methods=['POST'])
def update30():
    conn=psycopg2.connect(database="final",user="postgres",password="123")
    data = dict (request.form)
    cur=conn.cursor()
    sql="update airport set name='{name}',aircraft_code='{aircraft_code}',situation='{situation}',runway='{runway}',sequence='{sequence}',wait_time='{wait_time}' where aircraft_code='{aircraft_code}'".format (**data)
    cur.execute(sql)
    sql="select * from airport where aircraft_code='{}'".format(data["aircraft_code"])
    cur.execute(sql)
    result=cur.fetchall()
    conn.commit()
    conn.close()        
    return render_template('3_list.html',userlist=result)





@app.route('/4_search.html')
def search4():
    return render_template('4_search.html')
@app.route('/4_searchaction/',methods=['POST'])
def search40():
    conn=psycopg2.connect(database="final",user="postgres",password="123")
    data=dict(request.form)
    cur=conn.cursor()
    sql="select * from environment where aircraft_code= '{aircraft_code}'".format(**data)
    cur.execute(sql)
    result=cur.fetchall()
    conn.commit()
    conn.close()
    return render_template('4_list.html',userlist=result)

@app.route('/4_add.html')
def add4():
    return render_template('4_add.html')

@app.route('/4_addaction/',methods=['POST'])
def add40():
    conn=psycopg2.connect(database="final",user="postgres",password="123")
    data = dict (request.form)
    cur=conn.cursor()
    sql = "insert into environment values ('{airport_code}','{humidity}','{landform}','{weather}','{wind_scale}','{wind_direction}')".format (**data)
    cur.execute(sql)
    conn.commit()
    conn.close()
    return redirect('/4_add.html')

@app.route('/4_list.html')
def list4():
    return render_template('4_list.html')

@app.route('/4_delete')
def del4():
    conn=psycopg2.connect(database="final",user="postgres",password="123")
    aircraft_code=request.args.get('id') 
    cur=conn.cursor()
    cur.execute("delete from environment where aircraft_code='{}'".format(aircraft_code))
    conn.commit()
    conn.close()
    return redirect('4_list.html')  

@app.route('/4_update')
def update4():
    code=request.args.get('id')
    conn=psycopg2.connect(database="final",user="postgres",password="123")
    cur=conn.cursor()
    sql="select * from environment where aircraft_code='{}'".format(code)
    cur.execute(sql)
    result=cur.fetchall()
    conn.commit()
    conn.close()
    return render_template('4_update.html',userlist=result)

@app.route('/4_updateaction/',methods=['POST'])
def update40():
    conn=psycopg2.connect(database="final",user="postgres",password="123")
    data = dict (request.form)
    cur=conn.cursor()
    sql="update environment set aircraft_code='{aircraft_code}',humidity='{humidity}',landform='{landform}',weather='{weather}',wind_scale='{wind_scale}',wind_direction='{wind_direction}' where aircraft_code='{aircraft_code}'".format (**data)
    cur.execute(sql)
    sql="select * from airport where aircraft_code='{}'".format(data["aircraft_code"])
    cur.execute(sql)
    result=cur.fetchall()
    conn.commit()
    conn.close()   
    return render_template('4_list.html',userlist=result)


@app.route('/5_search.html')
def search5():
    return render_template('5_search.html')
@app.route('/5_searchaction/',methods=['POST'])
def search50():
    conn=psycopg2.connect(database="final",user="postgres",password="123")
    data=dict(request.form)
    cur=conn.cursor()
    sql="select * from airport where aircraft_code='{aircraft_code}'".format(**data)
    cur.execute(sql)
    result=cur.fetchall()
    conn.commit()
    conn.close()
    return render_template('5_list.html',userlist=result)

@app.route('/5_add.html')
def add5():
    return render_template('5_add.html')

@app.route('/5_addaction/',methods=['POST'])
def add50():
    conn=psycopg2.connect(database="final",user="postgres",password="123")
    data = dict (request.form)
    cur=conn.cursor()
    sql = "insert into aircraft_condition values ('{aircraft_code}','{longtitude}','{latitude}','{flight_attitude}','{flight_direction}','{oil_remaining}','{time_flown}','{mile_flown}','{if_breakdown}','{if_off_course}','{if_arrival}','{if_pass_restricted}')".format (**data)
    cur.execute(sql)
    conn.commit()
    conn.close()
    return redirect('/5_add.html')

@app.route('/5_list.html')
def list5():
    return render_template('5_list.html')

@app.route('/5_delete')
def del5():
    conn=psycopg2.connect(database="final",user="postgres",password="123")
    aircraft_code=request.args.get('id') 
    cur=conn.cursor()
    cur.execute("delete from aircraft_condition where aircraft_code='{}'".format(aircraft_code))    
    conn.commit()
    conn.close()
    return redirect('4_list.html')  

@app.route('/5_update')
def update5():
    code=request.args.get('id')
    conn=psycopg2.connect(database="final",user="postgres",password="123")
    cur=conn.cursor()
    sql="select * from aircraft_condition where aircraft_code='{}'".format(code)
    cur.execute(sql)
    result=cur.fetchall()
    conn.commit()
    conn.close()
    return render_template('5_update.html',userlist=result)

@app.route('/5_updateaction/',methods=['POST'])
def update50():
    conn=psycopg2.connect(database="final",user="postgres",password="123")
    data = dict (request.form)
    cur=conn.cursor()
    sql="update aircraft_condition set aircraft_code='{aircraft_code}',longtitude='{longtitude}',latitude='{latitude}',flight_attitude='{flight_attitude}',oil_remaining='{oil_remaining}',time_flown='{time_flown}',mile_flown='{mile_flown}',if_breakdown='{if_breakdown}',if_off_course='{if_off_course}',if_arrival='{if_arrival}',if_pass_restricted='{if_pass_restricted}' where aircraft_code='{aircraft_code}'".format (**data)
    cur.execute(sql)
    sql="select * from aircraft_condition where aircraft_code='{}'".format(data["aircraft_code"])
    cur.execute(sql)
    result=cur.fetchall()
    conn.commit()
    conn.close()   
    return render_template('5_list.html',userlist=result)





if __name__=='__main__':
    app.run(debug=True)
