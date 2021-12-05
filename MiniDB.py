import csv


class MiniDB:
    def save(self, fuel_general, distance_general):
        to_save = [fuel_general, distance_general]
        with open('FuelUsageDB.csv', 'a') as db_csv:
            db_reader = csv.writer(db_csv, delimiter=';')
            db_reader.writerow(to_save)

        db_csv.close()

    def load(self, col_index):
        with open('FuelUsageDB.csv') as db_csv:
            db_reader = csv.reader(db_csv, delimiter=';')

            rows = [row for row in db_reader]

            return rows[-2][col_index]

    def clear_db(self):
        with open('FuelUsageDB.csv') as db_csv:
            db_reader = csv.reader(db_csv, delimiter=';')

            rows = [row for row in db_reader]

            if len(rows) >= 10:
                try:
                    y = 1
                    for x in rows:
                        rows.pop(y)
                        y += 1
                except IndexError:
                    pass

                z = 0
                while z < 4:
                    rows.pop(0)
                    z += 1

                with open('FuelUsageDB.csv', 'w') as db_file:
                    db_clear = csv.writer(db_file, delimiter=';')
                    for x in rows:
                        db_clear.writerow(x)

        db_csv.close()
