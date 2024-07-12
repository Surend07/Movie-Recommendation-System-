import pandas as pd

def fetch_movie_details_local(movie_id):
    # Path to the Excel file
    file_path = "movies_details.xlsx"

    try:
        # Read the Excel file into a pandas DataFrame
        movies_details = pd.read_excel(file_path)

        # Check if the DataFrame is not empty
        if not movies_details.empty:
            # Get the details of the first movie in the DataFrame
            first_movie_details = movies_details.iloc[0]

            # Print the movie_id of the first movie
            print(f"Movie ID of the first movie: {first_movie_details['movie_id']}")

            # Convert the details to a dictionary
            movie_details_dict = first_movie_details.to_dict()

            return movie_details_dict
        else:
            print("No movies found in the DataFrame.")
            return {}
    except Exception as e:
        print(f"Error loading movie details: {e}")
        return {}

# Example: Print details of the first movie
fetch_movie_details_local(1)
