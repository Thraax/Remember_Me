import re
import sqlite3
from os import system, name


def validateEmail(validate_mail):
    if re.match(r"[^@]+@[^@]+\.[^@]+", validate_mail):
        return 1
    else:
        return 0


def insertAccount():
    inserted_mail = input("Enter the e-mail : ")

    if validateEmail(inserted_mail) == 1:
        password = input("Enter the e-mail password : ")
        site = input("Enter the site which associated with the email : ")
        try:
            query = "INSERT INTO accounts VALUES(?,?,?)"
            dataCursor.execute(query, (inserted_mail, password, site))
            connection.commit()
            print("The e-mail stored successfully")

        except sqlite3.Error as e:
            print(e)

    else:
        print("The insertion operation failed, try to enter the e-mail in correct format eg.(example@example.com)")


def insertLink():
    link = input("Enter the link : ")
    description = input("Enter the description for the link : ")
    try:
        query = "INSERT INTO links VALUES(?,?)"
        dataCursor.execute(query, (link, description))
        connection.commit()
        print("The link stored successfully\n")
    except sqlite3.Error as e:
        print(e)


def retrieveAccounts():
    try:
        dataCursor.execute("SELECT * FROM accounts")
        dataCursor.fetchone()
        print("-" * 25 + "\n")

        for email, password, site in dataCursor:
            if email != " ":
                print(">" * 20)
                print("Email --> {}".format(email))
                print("Site --> {}".format(site))
                print("Password --> {}".format(password))
                print(">" * 20)

            else:
                print("There is no any recorded emails yet.")

        print("-" * 25 + "\n")

    except sqlite3.Error as e:
        print(e)


def retrieveLinks():
    try:
        dataCursor.execute("SELECT * FROM links")
        dataCursor.fetchone()
        print("-" * 25 + "\n")

        for link, description in dataCursor:
            print(">" * 20)
            print("link --> {}".format(link))
            print("description --> {}".format(description))
            print("<" * 20)

        print("-" * 25 + "\n")

    except sqlite3.Error as e:
        print(e)


def updateAccount():
    query = ""
    print("1- Change email and keep password")
    print("2- Change password and keep email")
    print("3- Change the site")
    print("4- Change both")
    update_operation = input("Enter the operation number : ")

    # First condition

    if update_operation == "1":

        try:

            current_mail = input("Enter the e-mail that you want to change : ")

            if isExists_email(current_mail) == 1:
                changed_email = input("Enter the new e-mail address : ")
                query += "UPDATE accounts "
                query += "SET email = '" + changed_email + "' "
                query += "WHERE email = '" + current_mail + "' ;"
                dataCursor.execute(query)
                connection.commit()
                print("The e-mail has been updated successfully")
            else:
                print("This account does not exists")
        except sqlite3.Error as e:
            print(e)

    # Second condition

    elif update_operation == "2":
        try:
            current_mail = input("Enter the e-mail that you want to change his password: ")

            if isExists_email(current_mail) == 1:
                new_password = input("Enter the new password : ")
                query += "UPDATE accounts "
                query += "SET password = '" + new_password + "' "
                query += "WHERE email = '" + current_mail + "' ;"
                dataCursor.execute(query)
                connection.commit()
                print("The password has been updated successfully\n")

            else:
                print("This account does not exists")

        except sqlite3.Error as e:
            print(e)


    elif update_operation == "3":
        current_mail = input("Enter the account that you want to change site")

        if isExists_email(current_mail) == 1:
            new_site = input("Enter the new site description : ")
            query += "UPDATE accounts "
            query += "SET site = ? "
            query += "WHERE account = ?"
            dataCursor.execute(query, (new_site, current_mail))

        else:
            print("This account does not exists")

    # Fourth condition

    elif update_operation == "4":
        try:
            # Changing e-mail commands
            current_mail = input("Enter the e-mail that you want to change : ")

            if isExists_email(current_mail) == 1:

                changed_email = input("Enter the new e-mail address : ")
                query += "UPDATE accounts "
                query += "SET email = ?"
                query += "WHERE email = ?"
                dataCursor.execute(query, (changed_email, current_mail))
                connection.commit()
                print("The e-mail has been updated successfully\n")

                # Changing password commands

                new_password = input("Enter the new password : ")
                query += "UPDATE accounts "
                query += "SET password = '" + new_password + "' "
                query += "WHERE email = '" + changed_email + "' ;"
                dataCursor.execute(query)
                connection.commit()
                print("The password has been updated successfully\n")

            else:
                print("This account does not exists")
        except sqlite3.Error as e:
            print(e)


def updateLinks():
    query = ""
    print("1- Change link and keep description")
    print("2- Change description and keep link")
    print("3- Change both")
    update_operation = input("Enter the operation number : ")

    # First condition

    if update_operation == "1":

        try:
            current_link = input("Enter the link that you want to change : ")
            changed_link = input("Enter the new link : ")
            if isExists_link(current_link) == 1:
                query += "UPDATE links "
                query += "SET link = ?"
                query += "WHERE link = ?"
                dataCursor.execute(query, (changed_link, current_link))
                print("The link has been updated successfully")
            else:
                print("This link does not exists")

        except sqlite3.Error as e:
            print(e)

    # Second condition

    elif update_operation == "2":
        try:
            current_link = input("Enter the link that you want to change his description : ")
            new_description = input("Enter the new description : ")

            if isExists_link(current_link) == 1:
                query += "UPDATE links "
                query += "SET description = ?"
                query += "WHERE link = ?"
                dataCursor.execute(query, (new_description, current_link))
                connection.commit()
                print("The password has been updated successfully\n")
            else:
                print("This link does not exists")
        except sqlite3.Error as e:
            print(e)

    # Third condition

    elif update_operation == "3":

        try:

            # Changing link commands
            current_link = input("Enter the link that you want to change : ")
            if isExists_link(current_link) == 1:
                changed_link = input("Enter the new link : ")
                query += "UPDATE links "
                query += "SET link = ?"
                query += "WHERE link = ?"
                dataCursor.execute(query, (changed_link, current_link))
                connection.commit()
                print("The link has been updated successfully\n")

                # Changing description commands

                new_description = input("Enter the description : ")
                query += "UPDATE link "
                query += "SET description = ?"
                query += "WHERE link = ?"
                dataCursor.execute(query, (new_description, changed_link))
                print("The description has been updated successfully\n")

            else:
                print("This account does not exists")

        except sqlite3.Error as e:
            print(e)

    else:
        print("Wrong operation number")


def deleteAccount():
    query = ""
    delete_account = input("Enter the account that you want to delete : ")

    try:
        if isExists_email(delete_account) == 1:
            query += "DELETE FROM accounts "
            query += "WHERE email = (?)"
            dataCursor.execute(query, [delete_account])
            connection.commit()
            print("The email -> '{}' , has been deleted".format(delete_link))
        else:
            print("This account does not exists")

    except sqlite3.Error as e:
        print(e)


def delete_link():
    query = ""
    delete_link = input("Enter the link that you want to delete : ")
    try:
        if isExists_link(delete_link) == 1:
            query += "DELETE FROM links "
            query += "WHERE link = (?)"
            dataCursor.execute(query, [delete_link])
            connection.commit()
            print("The link -> '{}' , has been deleted".format(delete_link))
        else:
            print("This link does not exists")
    except sqlite3.Error as e:
        print(e)


def clear():
    if name == 'nt':
        _ = system('cls')

    else:
        _ = system('clear')


def isExists_email(findMail):
    dataCursor.execute("SELECT * FROM accounts")
    dataCursor.fetchone()
    for email, password, site in dataCursor:
        print(email)
        if email == findMail:
            return 1
    return 0


def isExists_link(findLink):
    for link, description in dataCursor.execute("SELECT *FROM links"):
        if link == findLink:
            return 1
    return 0


def assoc_link():
    key_word = input("Enter certain word to search links associated with it, ex.(Facebook,Twitter) : ")

    try:
        query = "SELECT *FROM links "
        query += "WHERE description LIKE ?"
        dataCursor.execute(query, ['%' + key_word + '%'])
        dataCursor.fetchone()

        print("-" * 25 + "\n")
        for link, description in dataCursor:
            print(">" * 20)
            print("link --> {}".format(link))
            print("description --> {}".format(description))
            print("<" * 20)

        print("-" * 25 + "\n")

    except sqlite3.Error as e:
        print(e)


def assoc_account():
    key_word = input("Enter certain word to search account associated with it, ex.(Facebook,Twitter) : ")

    try:
        query = "SELECT *FROM accounts "
        query += "WHERE site LIKE ?"
        dataCursor.execute(query, ['%' + key_word + '%'])
        dataCursor.fetchone()

        print("-" * 25 + "\n")
        for email, password, site in dataCursor:
            print(">" * 20)
            print("Email --> {}".format(email))
            print("Password --> {}".format(password))
            print("Site --> {}".format(site))
            print("<" * 20)

        print("-" * 25 + "\n")

    except sqlite3.Error as e:
        print(e)


connection = sqlite3.connect("lite.db")
dataCursor = connection.cursor()
dataCursor.execute("CREATE TABLE IF NOT EXISTS accounts (email TEXT , password TEXT , site TEXT)")
dataCursor.execute("CREATE TABLE IF NOT EXISTS links (link TEXT , description TEXT)")
connection.commit()
operation = ""

while operation != "12":
    
    print("1- Insert Account")
    print("2- Insert Link")
    print("3- Retrieve Accounts")
    print("4- Retrieve Links")
    print("5- Retrieve account with certain keyword")
    print("6- Retrieve Link with certain keyword")
    print("7- Update E-mail")
    print("8- Update Link")
    print("9- Delete Account")
    print("10- Delete Link")
    print("11- Clean Screen")
    print("12- Exit")
    operation = input("Enter the operation number : ")

    if operation == "1":
        insertAccount()

    elif operation == "2":
        insertLink()

    elif operation == "3":
        retrieveAccounts()

    elif operation == "4":
        retrieveLinks()

    elif operation == "5":
        assoc_account()

    elif operation == "6":
        assoc_link()

    elif operation == "7":
        updateAccount()

    elif operation == "8":
        updateLinks()

    elif operation == "9":
        deleteAccount()

    elif operation == "10":
        delete_link()

    elif operation == "11":
        clear()

    elif operation == "12":
        print("\nExit.....\n")
        break

    else:
        print("Enter correct input (1:12) \n")

dataCursor.close()
connection.close()
