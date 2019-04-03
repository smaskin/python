TABLES = {
    'categories': (
        'category_name TEXT PRIMARY KEY NOT NULL',
        'category_description TEXT NOT NULL'
    ),
    'units': (
        'unit_name TEXT PRIMARY KEY',
    ),
    'positions': (
        'position_name TEXT PRIMARY KEY',
    ),
    'goods': (
        'good_id INTEGER PRIMARY KEY AUTOINCREMENT',
        'good_name TEXT',
        'good_unit TEXT',
        'good_cat TEXT',
        'FOREIGN KEY(good_unit) REFERENCES units(unit)',
        'FOREIGN KEY(good_cat) REFERENCES categories(position)'
    ),
    'employees': (
        'employee_id INTEGER PRIMARY KEY AUTOINCREMENT',
        'employee_fio TEXT',
        'employee_position TEXT',
        'FOREIGN KEY(employee_position) REFERENCES positions(position)',
    ),
    'vendors': (
        'vendor_id INTEGER PRIMARY KEY AUTOINCREMENT',
        'vendor_name TEXT',
        'vendor_ownerchipform TEXT',
        'vendor_address TEXT',
        'vendor_phone TEXT',
        'vendor_email TEXT',
    ),
}

DATA = {
    'categories': [('Еда', 'Продукты питания'), ('Хоз. товары', 'Товары для дома')],
    'units': [('шт.',), ('кг.',)],
    'positions': [('Директор',), ('Программист',)],
    'goods': [('Хлеб', 'шт.', 'Еда'), ('Сахар', 'кг.', 'Еда')],
    'employees': [('Иванов Ива Иванович', 'Директор'), ('Петров Петр Пертович', 'Программист')],
    'vendors': [('IBM', '', 'Москва', '+79998887643', 'a@b.c')]
}


def create_tables(c):
    for name, columns in TABLES.items():
        sql = "CREATE TABLE IF NOT EXISTS {} ({})".format(name, ', '.join(columns))
        print(sql)
        c.execute(sql)


def insert_data(c):
    for table, values in DATA.items():
        columns = []
        for key, name in enumerate(TABLES[table]):
            column = name.split(' ')[0]
            if column != 'FOREIGN' and name.find('AUTOINCREMENT') == -1:
                columns.append(column)
        sql = "INSERT INTO {}({}) VALUES ({})".format(table, ', '.join(columns), ', '.join(['?'] * len(columns)))
        print(sql)
        c.executemany(sql, values)


def main():
    import sqlite3
    conn = sqlite3.connect('db.sqlite')

    cur = conn.cursor()
    create_tables(cur)
    insert_data(cur)

    conn.commit()
    conn.close()


if __name__ == '__main__':
    main()
