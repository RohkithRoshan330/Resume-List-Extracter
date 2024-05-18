import streamlit as st
import serpapi

def search_google(query, num_results=50):
    # Insert your actual SerpApi API key here (replace with 'YOUR_API_KEY')
    API_KEY = '0961588558451833cacc126696e070ea0c5d0bd53ed6aa34d92e38064394da85'

    # Search parameters
    params = {
        "api_key": API_KEY,
        "q": query,
        "engine": "google",  # Optional: Specify the search engine (default is Google)
        "num": num_results
    }

    try:
        results = serpapi.search(params)
        return results

    except Exception as e:
        return {"error": str(e)}

def main():
    st.title("Google Search Results") 
    # site: ' www.linkedin.com/in' ' Datascience OR AI engineer' Education: 'Bharathiyar University'



    # Input query from the user
    # response = provide me a boolean search query out of this provide me only the search query not anything more i need a iit madras data science candidate who is recently graduated use sites such as linkedin and github
    query = st.text_input("Enter your search query")

    if query:
        # Perform the search
        results = search_google(query , num_results= 50 )

        if results.get("search_metadata"):
            for result in results["organic_results"]:
                st.write(f"Title: {result['title']}")
                st.write(f"Snippet: {result['snippet']}")
                st.write(f"Link: {result['link']}")
                st.write("-" * 50)
        else:
            st.write(f"Error: {results.get('error')}")

if __name__ == "__main__":
    main()
