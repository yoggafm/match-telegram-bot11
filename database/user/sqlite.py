import sqlite3 as sq


async def db_start():
    global db, cur

    db = sq.connect('user.db')
    cur = db.cursor()

    cur.execute(
        'CREATE TABLE IF NOT EXISTS user('
        'user_id TEXT PRIMARY KEY,'
        'username TEXT,'
        'first_name TEXT,'
        'last_name TEXT,'
        'age TEXT,'
        'description TEXT,'
        'photo TEXT)'
    )

    db.commit()


async def create_user(user_id: str, username: str = None, first_name: str = None, last_name: str = None,
                      age: str = None,
                      description: str = None, photo: str = None):
    user = cur.execute(f'SELECT user_id FROM user WHERE user_id = {user_id}').fetchone()

    if not user:
        cur.execute('INSERT INTO user VALUES(?,?,?,?,?,?,?)',
                    (user_id, username, first_name, last_name, age, description, photo))
        db.commit()


async def edit_user(user_id, username: str = None, first_name: str = None, last_name: str = None, age: str = None,
                    description: str = None, photo: str = None):
    cur.execute(f'UPDATE user'
                f' SET username = {username}, first_name = {first_name}, last_name = {last_name},'
                f' age = {age}, description = {description}, photo = {photo}'
                f' WHERE user_id = {user_id}')
    db.commit()


async def get_user_by_id(user_id: int):
    user = cur.execute(f'SELECT * FROM user WHERE user_id={user_id}').fetchone()
    return {'user_id': user[0], 'username': user[1], 'first_name': user[2],
            'last_name': user[3], 'age': user[4], 'description': user[5], 'photo': user[6]}
