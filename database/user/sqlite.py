import sqlite3 as sq


async def db_start():
    global db, cur

    db = sq.connect('users.db')
    cur = db.cursor()

    cur.execute(
        'CREATE TABLE IF NOT EXISTS users('
        'user_id TEXT PRIMARY KEY,'
        'username TEXT,'
        'first_name TEXT,'
        'last_name TEXT,'
        'age INT,'
        'description TEXT,'
        'photo TEXT)'
    )

    db.commit()


async def create_user(user_id: str, username: str = None, first_name: str = None, last_name: str = None,
                      age: str = None,
                      description: str = None, photo: str = None):
    user = cur.execute(f'SELECT user_id FROM users WHERE user_id = {user_id}').fetchone()

    if not user:
        cur.execute('INSERT INTO users VALUES(?,?,?,?,?,?,?)',
                    (user_id, username, first_name, last_name, age, description, photo))
        db.commit()


async def edit_username(user_id: str, username: str):
    cur.execute('''UPDATE users SET username = "{}" WHERE user_id = "{}"'''.format(username, user_id))
    db.commit()


async def edit_first_name(user_id: str, first_name: str):
    cur.execute(f'''UPDATE users SET first_name="{first_name}" WHERE user_id = "{user_id}"''')
    db.commit()


async def edit_last_name(user_id: str, last_name: str):
    cur.execute(f'''UPDATE users SET last_name="{last_name}" WHERE user_id = "{user_id}"''')
    db.commit()


async def edit_age(user_id: str, age: int):
    cur.execute(f'''UPDATE users SET age={age} WHERE user_id = "{user_id}"''')
    db.commit()


async def edit_description(user_id: str, description: str):
    cur.execute(f'''UPDATE users SET description="{description}" WHERE user_id = "{user_id}"''')
    db.commit()


async def edit_photo(user_id: str, photo: str):
    cur.execute(f'''UPDATE users SET photo="{photo}" WHERE user_id = "{user_id}"''')
    db.commit()


async def edit_user(user_id, username: str = None, first_name: str = None,
                    last_name: str = None, age: int = None, description: str = None, photo: str = None):
    cur.execute(f'UPDATE users'
                f' SET username = "{username}", first_name = "{first_name}", last_name = "{last_name}",'
                f' age = {age}, description = "{description}", photo = "{photo}"'
                f' WHERE user_id = "{user_id}"')
    db.commit()


async def get_user_by_id(user_id: int):
    user = cur.execute(f'SELECT * FROM users WHERE user_id={user_id}').fetchone()
    return {'user_id': user[0], 'username': user[1], 'first_name': user[2],
            'last_name': user[3], 'age': user[4], 'description': user[5], 'photo': user[6]}
