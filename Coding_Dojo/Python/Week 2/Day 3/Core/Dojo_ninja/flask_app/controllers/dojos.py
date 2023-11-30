def home():
    return redirect(url_for('dojos'))

# Dojo page
@app.route('/dojos')
def dojos():
    # Fetch all dojos from the database
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM dojos;')
    dojos = cur.fetchall()
    cur.close()
    
    return render_template('dojos.html', dojos=dojos)

# Dojo Show page
@app.route('/dojos/<int:dojo_id>')
def dojo_show(dojo_id):
    # Fetch the dojo and its ninjas from the database
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM dojos WHERE id = %s;', (dojo_id,))
    dojo = cur.fetchone()
    cur.execute('SELECT * FROM ninjas WHERE dojo_id = %s;', (dojo_id,))
    ninjas = cur.fetchall()
    cur.close()
    
    return render_template('dojo_show.html', dojo=dojo, ninjas=ninjas)

# Ninja page
@app.route('/ninjas')
def ninjas():
    # Fetch all dojos for the dropdown menu
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM dojos;')
    dojos = cur.fetchall()
    cur.close()
    
    return render_template('ninjas.html', dojos=dojos)

# Create Ninja route
@app.route('/ninjas/create', methods=['POST'])
def create_ninja():
    if request.method == 'POST':
        ninja_name = request.form['ninja_name']
        dojo_id = request.form['dojo_id']
        
        # Insert new ninja into the database
        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO ninjas (name, dojo_id) VALUES (%s, %s);', (ninja_name, dojo_id))
        mysql.connection.commit()
        cur.close()
        
        # Redirect to the Dojo Show page for the selected dojo
        return redirect(url_for('dojo_show', dojo_id=dojo_id))

if __name__ == '__main__':
    app.run(debug=True)