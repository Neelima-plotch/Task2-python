import mysql.connector as MySQLdb

# MySQL database configuration (replace with your actual database credentials)
db_config = MySQLdb.connect (
  host="localhost",
  user="root",
  password="neelima_2012",
  database="movies"
)

mycursor = db_config.cursor()

def average_visitor_count(query):
    # Calculating the average visitor count
    query = "SELECT AVG(visits) FROM visitors"
    mycursor.execute(query)
    avg_visitor_count = mycursor.fetchone()[0]
    return avg_visitor_count

def get_movies_above_avg(mycursor, avg_visitor_count):
    # Getting the movie with visitor count greater than the average
    query = "SELECT movie_id FROM visitors WHERE visits > %s"
    mycursor.execute(query, (avg_visitor_count,))
    movies_above_avg = mycursor.fetchall()
    return movies_above_avg

def get_movie_name_by_id(mycursor,movie_id):
    # Getting the movie name by it's ID
    query="SELECT movie_name from movie WHERE id= %s"
    mycursor.execute(query,(movie_id,))
    movie_name = mycursor.fetchone()
    return movie_name
    
def main_function():

    try:
        # Calculate average visitor count
        avg_visitor_count = average_visitor_count(mycursor)

        # Get movies with visitor count greater than the average
        movies_above_avg = get_movies_above_avg(mycursor, avg_visitor_count)

        for movie_id in movies_above_avg:
            movie_name = get_movie_name_by_id(mycursor,movie_id[0])
              # Print the result
            print(f"Movies with visitor count > {avg_visitor_count}: {movie_name}")

    except Exception as e:
         print(f'Error{e}')

def __del__(self):
     mycursor.close()
     db_config.close()


if __name__ == '__main__':
    main_function()