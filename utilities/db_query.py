import utilities.db_connection as db


def insert_bsnl_plans(plans, connection):
    cur = connection.cursor()
    for plan in plans:
        print(str(plan))
        cur.execute(
            "INSERT INTO plans (name, validity, operator, type, amount, description, circle_name, extra, benefits)"
            " VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
            (plan.get_plan_name(),
             plan.get_benefit(),
             'BSNL',
             'PREPAID', plan.get_amount(), plan.get_description(), plan.get_circle(), '', '')
        )
    connection.commit()


def insert_jio_plans(plans, connection):
    cur = connection.cursor()
    for plan in plans:
        extra = plan.sms + " | " + plan.voice + " Voice calls"
        print(str(plan))
        cur.execute(
            "INSERT INTO plans (name, validity, operator, type, amount, description, circle_name, extra, benefits)"
            " VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
            (plan.category, plan.validity, 'Jio', 'PREPAID', plan.amount,
             plan.description, 'All', extra, plan.data)
        )
    connection.commit()


def insert_airtel_plans(plans, connection):
    cur = connection.cursor()
    for plan in plans:
        print(str(plan))
        cur.execute(
            "INSERT INTO plans (name, validity, operator, type, amount, description, circle_name, extra, benefits)"
            " VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
            (plan.tag, plan.validity, 'Airtel', 'PREPAID', plan.amount,
             plan.additionalInfo, 'All', plan.otherInfo, plan.data + " " + plan.sms)
        )
    connection.commit()
