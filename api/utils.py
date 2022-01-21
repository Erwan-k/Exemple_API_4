def getMysqlConnection():
	url = make_url(os.getenv('DATABASE_URL'))
	mydb = mysql.connector.connect(host=url.host,user=url.username,passwd=url.password,database=url.database)
	return mydb

def ajouter_user(user,mdp,mycursor,mydb):
	val = (user,mdp)
	mycursor.execute("INSERT INTO Utilisateur (user,mdp) VALUES ("+",".join(["%s"]*len(val))+")", val)
	mydb.commit()
