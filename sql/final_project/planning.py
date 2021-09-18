import psycopg2
import datetime
import itertools


def get_quarter_id(qr, year):
    return str(year) + '.' + str(qr)


def start_planning(year, quarter, user, pwd=''):
    conn = psycopg2.connect(database='planning', user=user, password=pwd, host='localhost')

    cur = conn.cursor()

    # clear tables
    clear_plan_data_qr = """DELETE FROM plan_data WHERE quarterid = %s"""
    clear_plan_status_qr = """DELETE FROM plan_status WHERE quarterid = %s"""

    current_quarter_id = get_quarter_id(quarter, year)

    cur.execute(clear_plan_data_qr, (current_quarter_id,))
    conn.commit()

    cur.execute(clear_plan_status_qr, (current_quarter_id,))
    conn.commit()

    # fill plan_status
    timestamp = datetime.datetime.now().timestamp()
    countries_qr = """select * from country2"""

    cur.execute(countries_qr)

    plan_status_records = []
    for record in cur:
        plan_status_records.append([current_quarter_id, timestamp, user, record[0]])

    insert_plan_status_qr = """INSERT INTO plan_status VALUES (%s, 'R', to_timestamp(%s), %s, %s)"""

    for record in plan_status_records:
        cur.execute(insert_plan_status_qr, record)

    conn.commit()

    # fill plan_data
    cur.execute('select productcategoryid from productcategory')
    categories = [item[0] for item in cur.fetchall()]

    cur.execute('select countrycode from country2')
    countries = [item[0] for item in cur.fetchall()]

    combinations = itertools.product(categories, countries)

    planned_salesamt_qr = """select categoryid, c.countrycode, sum(salesamt)/2 as salesamt from company_sales cs
        inner join company c
        on cs.cid = c.id
        where (qr = %s or qr = %s) and ccls in ('A', 'B')
        group by categoryid, c.countrycode"""

    cur.execute(planned_salesamt_qr, [get_quarter_id(quarter, year-2), get_quarter_id(quarter, year-1)])

    average_saleamn = cur.fetchall()

    insert_plan_data_qr = """INSERT INTO plan_data VALUES (%s, %s, %s, %s, %s)"""

    for comb in combinations:
        res = list(filter(lambda item: item[0] == comb[0] and item[1] == comb[1], average_saleamn))

        if res:
            row_data = res[0]
            cur.execute(insert_plan_data_qr, ['N', row_data[1], current_quarter_id, row_data[0], row_data[2]])
            cur.execute(insert_plan_data_qr, ['P', row_data[1], current_quarter_id, row_data[0], row_data[2]])
        else:
            cur.execute(insert_plan_data_qr, ['N', comb[1], current_quarter_id, comb[0], 0])
            cur.execute(insert_plan_data_qr, ['P', comb[1], current_quarter_id, comb[0], 0])

    conn.commit()


# start_planning(2014, 1, 'kirill')
# start_planning(2014, 1, 'sophie')


def set_lock(year, quarter, user, pwd=''):
    conn = psycopg2.connect(database='planning', user=user, password=pwd, host='localhost')

    cur = conn.cursor()

    timestamp = datetime.datetime.now().timestamp()
    current_quarter = get_quarter_id(quarter, year)

    cur.execute(
        """UPDATE plan_status
            SET status = 'L', modifieddatetime = to_timestamp(%s), author = %s
            FROM country_managers
            WHERE country_managers.country = plan_status.country and
                country_managers.username = current_user and
                quarterid = %s""",
        [timestamp, user, current_quarter]
    )

    conn.commit()


# set_lock(2014, 1, 'kirill')
# set_lock(2014, 1, 'sophie')


def remove_lock(year, quarter, user, pwd=''):
    conn = psycopg2.connect(database='planning', user=user, password=pwd, host='localhost')

    cur = conn.cursor()

    timestamp = datetime.datetime.now().timestamp()
    current_quarter = get_quarter_id(quarter, year)

    cur.execute(
        """UPDATE plan_status
            SET status = 'R', modifieddatetime = to_timestamp(%s), author = %s
            FROM country_managers
            WHERE country_managers.country = plan_status.country and
                country_managers.username = current_user and
                quarterid = %s""",
        [timestamp, user, current_quarter]
    )

    conn.commit()


# remove_lock(2014, 2, 'sophie', '')


def accept_plan(year, quarter, user, pwd=''):
    conn = psycopg2.connect(database='planning', user=user, password=pwd, host='localhost')

    cur = conn.cursor()

    timestamp = datetime.datetime.now().timestamp()
    current_quarter = get_quarter_id(quarter, year)

    new_plan_qr = """select pd.versionid, pd.country, pd.quarterid, pd.pcid, salesamt from plan_data pd
        join plan_status ps on pd.country = ps.country and pd.quarterid = ps.quarterid
        join country_managers cm on pd.country = cm.country
        where pd.quarterid = %s and versionid = 'P' and ps.status = 'R' and cm.username = current_user"""

    cur.execute(new_plan_qr, [current_quarter])
    new_plan_records = cur.fetchall()

    cur.execute('select country from country_managers where username = current_user')
    current_user_countries = tuple([item[0] for item in cur.fetchall()])

    delete_old_plan_qr = """delete from plan_data
        where versionid = 'A' and quarterid = %s and country in %s"""

    cur.execute(delete_old_plan_qr, [current_quarter, (current_user_countries)])
    conn.commit()

    print(new_plan_records)

    for record in new_plan_records:
        print(*record[1:])
        cur.execute("""INSERT INTO plan_data VALUES ('A', %s, %s, %s, %s)""", [*record[1:]])

    conn.commit()

    update_plan_status_qr = """UPDATE plan_status
        SET status = 'A', modifieddatetime = to_timestamp(%s)
        WHERE quarterid = %s and author = current_user and country in %s"""

    timestamp = datetime.datetime.now().timestamp()
    cur.execute(update_plan_status_qr, [timestamp, current_quarter, (current_user_countries)])
    conn.commit()


accept_plan(2014, 1, 'kirill')
accept_plan(2014, 1, 'sophie')
