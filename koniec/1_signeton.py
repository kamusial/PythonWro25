class DatabaseConnection:

    _instance = None
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
            cls._instance.connection = 'Aktywne połączneie z bazą'
            print('Utworzono nowe połączenie')
        return cls._instance

    def query(self, sql):
        print(f"Wykonuję zapytanie: {sql}")
        return f"Wynik zapytania: {sql}"

db1 = DatabaseConnection()
db2 = DatabaseConnection()

print(db1 is db2)
print(db1.query("SELECT * FROM users"))
