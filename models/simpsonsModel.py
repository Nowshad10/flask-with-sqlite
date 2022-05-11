import sqlite3

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

class Simpson:
    def __init__(self, id, name, age):
        self.id = id,
        self.name = name,
        self.age = age
    
    @staticmethod
    def get_all():
        data = []
        conn = get_db_connection()
        simpsons = conn.execute('SELECT * FROM simpsons').fetchall()
        for s in simpsons:
            simpsonsData = {
                "id": s["id"],
                "name": s["name"],
                "age": s["age"]
            }
            data.append(simpsonsData)
        conn.close()
        return data

    @classmethod
    def show(self, id):
        data = []
        conn = get_db_connection()
        simpsons = conn.execute('SELECT * FROM simpsons WHERE id = ?', (id,)).fetchall()
        simpsonsData = {
            "id": simpsons[0]["id"],
            "name": simpsons[0]["name"],
            "age": simpsons[0]["age"]
        }
        data.append(simpsonsData)
        conn.close()
        return data
    
    @classmethod
    def create(self, req_data):
        data = []
        conn = get_db_connection()
        simpsons = conn.execute('INSERT INTO simpsons (name, age) VALUES (?,?) RETURNING *', (req_data["name"], req_data["age"])).fetchall()
        simpsonsData = {
            "id": simpsons[0]["id"],
            "name": simpsons[0]["name"],
            "age": simpsons[0]["age"]
        }
        data.append(simpsonsData)
        conn.commit()
        conn.close()
        return data
    
    def update(current_data, new_data):
        data = []
        conn = get_db_connection()
        simpsons = conn.execute('UPDATE simpsons SET name = ?, age = ? WHERE id = ? RETURNING *', (new_data['name'], new_data['age'], current_data['id']))
        for s in simpsons:
            simpsonsData = {
                "id": s["id"],
                "name": s["name"],
                "age": s["age"]
            }
            data.append(simpsonsData)
        conn.commit()
        conn.close()
        return data
    
    def delete(id):
        conn = get_db_connection()
        conn.execute('DELETE FROM simpsons WHERE id=?', (id,))
        conn.commit()
        conn.close()
        return
