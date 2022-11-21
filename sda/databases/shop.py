'''
    1. O sa avem niste utilizatori care trebuie sa aiba neaparat un nume, email, parola.
    2. O sa avem produse pe care utilizatorii le pot cumpara daca sunt disponibile.
       Un produs are denumire, cantitate, pret.

    Inainte sa fie logat utilizatorul:
    1. Log-in (cerem de la utilizator email si parola)
    2. Register (cerem de la utilizator nume, email si parola si ii facem un cont)
    0. Exit application

    Dupa login:
    1. Afiseaza lista de produse disponibile (afisam produsele care au cantitatea > 0)
    2. Cumpara produs (ii cerem un id de produs si o cantitate si daca exista suficienta cantitate il lasam sa cumpere (scade cantitatea de pe produs si se adauga in istoric cumparatura)
    3. Afiseaza istoric cumparaturi (ii afisam ce produs a cumparat, cand l-a cumparat (data si ora) si cat a platit in total (cantitate * pret))
    4. Log out - se intoarce la primul meniu
    0. Exit application
'''
import mysql.connector as mysql
import datetime


def create_structure():
    conn = mysql.connect(
        host="localhost",
        user="root",
        password="password",
        database="",
    )

    with conn.cursor() as c:
        c.execute("CREATE DATABASE IF NOT EXISTS shop;")
        c.execute("""
            CREATE TABLE IF NOT EXISTS shop.utilizator (
                id INT PRIMARY KEY AUTO_INCREMENT,
                nume TEXT NOT NULL,
                email TEXT NOT NULL,
                parola TEXT NOT NULL
            );
        """)
        c.execute("""
            CREATE TABLE IF NOT EXISTS shop.produs (
                id INT PRIMARY KEY AUTO_INCREMENT,
                denumire TEXT NOT NULL,
                cantitate INT NOT NULL,
                pret DECIMAL(8, 2) NOT NULL 
            );
        """)
        c.execute("""
            CREATE TABLE IF NOT EXISTS shop.istoric (
                id INT PRIMARY KEY AUTO_INCREMENT,
                user_id INT NOT NULL,
                produs_id INT NOT NULL,
                data TIMESTAMP NOT NULL,
                cantitatea_cumparata INT NOT NULL,
                CONSTRAINT fk_user_id FOREIGN KEY(user_id) REFERENCES shop.utilizator(id),
                CONSTRAINT fk_produs_id FOREIGN KEY(produs_id) REFERENCES shop.produs(id)
            );
        """)

    conn.close()


create_structure()


def show_menu_1():
    print("1. Login")
    print("2. Register")
    print("0. Exit application")


def show_menu_2():
    print("1. Show product list")
    print("2. Buy product")
    print("3. Show history")
    print("4. Logout")
    print("5. Add product")
    print("0. Exit application")


conn = mysql.connect(
    host="localhost",
    user="root",
    password="password",
    database="shop",
)

user_logat = None

while True:
    if user_logat is None:
        show_menu_1()
        optiune = int(input("Optiunea este: "))

        if optiune == 0:
            break
        elif optiune == 1:
            email = input("Email = ")
            parola = input("Parola = ")

            with conn.cursor() as c:
                c.execute("SELECT id FROM utilizator WHERE email = %s AND parola = %s;", (email, parola))
                result = c.fetchone()  # (1,)
                if result:  # fetch one ne returneaza None daca nu s-au gasit date (daca nu exista email-ul cu parola respectiva)
                    user_logat = result[0]
                else:
                    print("Username/Parola nu exista.")
        elif optiune == 2:
            nume = input("Nume = ")
            email = input("Email = ")
            parola = input("Parola = ")

            with conn.cursor() as c:
                c.execute("INSERT INTO utilizator (nume, email, parola) VALUES (%s, %s, %s);", (nume, email, parola))
                conn.commit()
    else:
        show_menu_2()
        optiune = int(input("Optiunea este: "))

        if optiune == 0:
            break
        elif optiune == 1:
            # Afiseaza lista de produse disponibile (afisam produsele care au cantitatea > 0)
            with conn.cursor() as c:
                c.execute("SELECT * FROM produs WHERE cantitate > 0")
                produse = c.fetchall()
                print("Lista de produse:")
                for produs in produse:  # produs = (id, denumire, cantitate, pret)
                    print(f"Produsul {produs[1]} cu id-ul {produs[0]} are cantitatea {produs[2]} si pretul {produs[3]} lei")
                print("--------------------")
        elif optiune == 2:
            # Cumpara produs (ii cerem un id de produs si o cantitate si daca exista suficienta cantitate il lasam sa cumpere (scade cantitatea de pe produs si se adauga in istoric cumparatura)
            id_produs = int(input("Id produs = "))
            cantitatea = int(input("Cantitatea = "))

            with conn.cursor() as c:
                c.execute("SELECT * FROM produs WHERE id = %s AND cantitate >= %s;", (id_produs, cantitatea))
                result = c.fetchone()
                if result:
                    # exista produsul si cantitatea dorita
                    c.execute("UPDATE produs SET cantitate = cantitate - %s WHERE id = %s;", (cantitatea, id_produs))
                    c.execute("INSERT INTO istoric (user_id, produs_id, data, cantitatea_cumparata) VALUES (%s, %s, %s, %s);",
                              (user_logat, id_produs, datetime.datetime.now(), cantitatea))
                    conn.commit()
                else:
                    print("Nu exista produsul sau cantitate suficienta")
        elif optiune == 3:
            # Afiseaza istoric cumparaturi (ii afisam ce produs a cumparat, cand l-a cumparat (data si ora) si cat a platit in total (cantitate * pret))
            with conn.cursor() as c:
                c.execute(
                    "SELECT p.denumire, p.pret * i.cantitatea_cumparata, i.data FROM istoric i INNER JOIN produs p ON i.produs_id = p.id WHERE i.user_id = %s;",
                    (user_logat,))
                results = c.fetchall()
                print("Istoric cumparaturi: ")
                for result in results:  # result (denumire_produs, pret_total, data)
                    print(f"Ati cumparat {result[0]} in valoare de {result[1]} lei la data de {result[2]}")
                print("--------------------")
        elif optiune == 5:
            denumire = input("Denumire = ")
            cantitate = input("Cantitatea = ")
            pret = int(input("Pret = "))
            with conn.cursor() as c:
                c.execute(f"INSERT INTO produs (denumire, cantitate, pret) VALUES ('{denumire}','{cantitate}', '{pret}');")
                conn.commit()
        elif optiune == 4:
            user_logat = None
conn.close()
