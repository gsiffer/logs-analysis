#!/usr/bin/env python
"""This program makes various sql queries from the newsdata.sql file"""
import psycopg2


class ReadDataBase:  # Open db and evaluate the SQL command.
    def query(self, chosen_question):
        return self.open_db(chosen_question[0]), chosen_question[1]

    def open_db(self, chosen_question):
        db = psycopg2.connect('dbname = news')
        c = db.cursor()
        c.execute(chosen_question)
        posts = c.fetchall()
        db.close()
        return posts


class NewsQuery:  # Where the program stars. It creates different SQL queries.
    def __init__(self, q1):
        self.query = q1

    def start_query(self):
        chosen_question = self.intro()
        received_data = self.query.query(chosen_question)
        self.text(received_data[0], received_data[1])
        self.the_end()

    def intro(self):  # User can choose between different queries.
        print('\nWhat would you like to know today?\n')
        chosen_number = raw_input('1. What are the most popular three articles'
                                  ' of all time?\n2. Who are the most popular '
                                  'article authors of all time?\n3. On which '
                                  'days did more than 1% of requests lead '
                                  'to errors?\nEnter a number(1, 2 or 3):>>> ')
        while (chosen_number.strip() != '1' and chosen_number.strip() !=
               '2' and chosen_number.strip() != '3'):
            chosen_number = raw_input("Please enter 1, 2 or 3:>>> ")
        print('Please wait.....\n')
        return self.evaluate(chosen_number.strip())

    def evaluate(self, chosen_number):  # Return with the chosen SQL command.
        if chosen_number == '1':
            chosen_question = '''SELECT title,
                                        count(*) AS num
                                 FROM splitpath
                                 GROUP BY title
                                 ORDER BY num DESC
                                 LIMIT 3;'''
        elif chosen_number == '2':
            chosen_question = '''SELECT name,
                                        count(*) AS num
                                 FROM authors,
                                      splitpath
                                 WHERE splitpath.author = authors.id
                                 GROUP BY name
                                 ORDER BY num DESC;'''
        else:
            chosen_number = '3'
            chosen_question = '''SELECT connection.alldate,
                                        div.round
                                 FROM CONNECTION,

                                   (SELECT alldate,
                                           round(cast(float8(failcon*100/
                                                 allcon::float) AS numeric), 2)
                                    FROM CONNECTION)AS div
                                 WHERE connection.alldate = div.alldate
                                   AND round > 1;'''
        return chosen_question, chosen_number

    def text(self, answers, query_id):  # It prints out the result.
        if (query_id == '1' or query_id == '2'):
            message = ' views'
        else:
            message = '% errors'
        for element in answers:
            print('** {} -- {}{}'.format(element[0], element[1], message))
        print('')

    def the_end(self):  # User can make new queries or leaves the program.
        query_again = raw_input('Would you like to make a query '
                                'again?(y/n) >>> ')
        while (query_again.lower().strip() != 'y' and
               query_again.lower().strip() != 'n'):
            query_again = raw_input("Please chose('y/n'). >>> ")
        query_again = query_again.lower().strip()
        if query_again == 'y':
            self.start_query()
        else:
            exit()


if __name__ == '__main__':
    query = NewsQuery(ReadDataBase())
    query.start_query()
