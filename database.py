import sqlite3

con = sqlite3.connect('database.db')

cur = con.cursor()

cur.execute('''
    CREATE TABLE IF NOT EXISTS drivers(
        first_name,
        last_name,
        driver_number INTEGER PRIMARY KEY,
        link
    )
''')

cur.execute('''
    CREATE TABLE IF NOT EXISTS teams(
        team_name,
        link
    )
''')

try:
    cur.execute("INSERT INTO drivers VALUES ('Max', 'Verstappen', 1, 'https://www.formula1.com/en/drivers/max-verstappen')")
    cur.execute("INSERT INTO drivers VALUES ('Yuki', 'Tsunoda', 22, 'https://www.formula1.com/en/drivers/yuki-tsunoda')")
    cur.execute("INSERT INTO drivers VALUES ('Lando', 'Norris', 4, 'https://www.formula1.com/en/drivers/lando-norris')")
    cur.execute("INSERT INTO drivers VALUES ('Oscar', 'Piastri', 81, 'https://www.formula1.com/en/drivers/oscar-piastri')")
    cur.execute("INSERT INTO drivers VALUES ('Charles', 'Leclerc', 16, 'https://www.formula1.com/en/drivers/charles-leclerc')")
    cur.execute("INSERT INTO drivers VALUES ('Lewis', 'Hamilton', 44, 'https://www.formula1.com/en/drivers/lewis-hamilton')")
    cur.execute("INSERT INTO drivers VALUES ('Liam', 'Lawson', 30, 'https://www.formula1.com/en/drivers/liam-lawson')")
    cur.execute("INSERT INTO drivers VALUES ('Isack', 'Hadjar', 6, 'https://www.formula1.com/en/drivers/isack-hadjar')")
    cur.execute("INSERT INTO drivers VALUES ('Nico', 'Hulkenberg', 27, 'https://www.formula1.com/en/drivers/nico-hulkenberg')")
    cur.execute("INSERT INTO drivers VALUES ('Gabriel', 'Bortoleto', 5, 'https://www.formula1.com/en/drivers/gabriel-bortoleto')")
    cur.execute("INSERT INTO drivers VALUES ('Lance', 'Stroll', 18, 'https://www.formula1.com/en/drivers/lance-stroll')")
    cur.execute("INSERT INTO drivers VALUES ('Fernando', 'Alonso', 14, 'https://www.formula1.com/en/drivers/fernando-alonso')")
    cur.execute("INSERT INTO drivers VALUES ('Alexander', 'Albon', 23, 'https://www.formula1.com/en/drivers/alexander-albon')")
    cur.execute("INSERT INTO drivers VALUES ('Carlos', 'Sainz', 55, 'https://www.formula1.com/en/drivers/carlos-sainz')")
    cur.execute("INSERT INTO drivers VALUES ('George', 'Russell', 63, 'https://www.formula1.com/en/drivers/george-russell')")
    cur.execute("INSERT INTO drivers VALUES ('Kimi', 'Antonelli', 12, 'https://www.formula1.com/en/drivers/kimi-antonelli')")
    cur.execute("INSERT INTO drivers VALUES ('Esteban', 'Ocon', 31, 'https://www.formula1.com/en/drivers/esteban-ocon')")
    cur.execute("INSERT INTO drivers VALUES ('Oliver', 'Bearman', 87, 'https://www.formula1.com/en/drivers/oliver-bearman')")
    cur.execute("INSERT INTO drivers VALUES ('Pierre', 'Gasly', 10, 'https://www.formula1.com/en/drivers/pierre-gasly')")
    cur.execute("INSERT INTO drivers VALUES ('Jack', 'Doohan', 7, 'https://www.formula1.com/en/drivers/jack-doohan')")

    cur.execute("INSERT INTO teams VALUES ('Oracle Red Bull Racing', 'https://www.formula1.com/en/teams/red-bull-racing')")
    cur.execute("INSERT INTO teams VALUES ('McLaren Formula 1 Team', 'https://www.formula1.com/en/teams/mclaren')")
    cur.execute("INSERT INTO teams VALUES ('Scuderia Ferrari HP', 'https://www.formula1.com/en/teams/ferrari')")
    cur.execute("INSERT INTO teams VALUES ('Visa Cash App Racing Bulls Formula One Team', 'https://www.formula1.com/en/teams/racing-bulls')")
    cur.execute("INSERT INTO teams VALUES ('Stake F1 Team Kick Sauber', 'https://www.formula1.com/en/teams/kick-sauber')")
    cur.execute("INSERT INTO teams VALUES ('Aston Martin Aramco Formula One Team', 'https://www.formula1.com/en/teams/aston-martin')")
    cur.execute("INSERT INTO teams VALUES ('Atlassian Williams Racing', 'https://www.formula1.com/en/teams/williams')")
    cur.execute("INSERT INTO teams VALUES ('Mercedes-AMG PETRONAS Formula One Team', 'https://www.formula1.com/en/teams/mercedes')")
    cur.execute("INSERT INTO teams VALUES ('MoneyGram Haas F1 Team', 'https://www.formula1.com/en/teams/haas')")
    cur.execute("INSERT INTO teams VALUES ('BWT Alpine Formula One Team', 'https://www.formula1.com/en/teams/alpine')")

    con.commit()

except sqlite3.IntegrityError:
    print("Value already added")

con.close()

# cur.execute("SELECT * FROM drivers")
# rows = cur.fetchall()
# for row in rows:
#     print(row)

# cur.execute("SELECT * FROM teams")
# rows = cur.fetchall()
# for row in rows:
#     print(row)

def short_team_name(user_request):
    con = sqlite3.connect('database.db')
    cur = con.cursor()

    cur.execute("SELECT * FROM teams WHERE team_name LIKE ?", (f'%{user_request}%',))
    rows = cur.fetchall()
    con.close()
    for row in rows:
        return row[1]

def short_driver_name_number(user_request):
    con = sqlite3.connect('database.db')
    cur = con.cursor()

    if user_request.isdigit():
        cur.execute("SELECT * FROM drivers WHERE driver_number=?", (user_request,))
    else:
        cur.execute("SELECT * FROM drivers WHERE first_name LIKE ? or last_name LIKE ?", (f'%{user_request}%', f'%{user_request}%'))
    rows = cur.fetchall()
    con.close()
    for row in rows:
        return row[3]
    
