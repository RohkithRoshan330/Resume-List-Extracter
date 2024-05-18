import google.generativeai as genai
import serpapi
import streamlit as st
import csv


def generate_search_query(user_input):
    # Configure GenerativeAI
    genai.configure(api_key="AIzaSyAN5ejPtEN-ckL0ZSwAgJMYTSw2IzR5Z8o")

    # Initialize the GenerativeAI model
    model = genai.GenerativeModel('gemini-pro')

    response = model.generate_content(f'''prompt:provide me a boolean search query out of this provide me only the search query not anything more ["I need a MIT computer science graduate for python developer",
                                      "Web Developer with experience in React (University of Melbourne, Australia)",
"Data Analyst with experience in SQL (IIT Bombay, India)",
"Python Developer with linkedin contributions (University of Waterloo, Canada)",
"Data Scientist at Stanford (US)",
"University of California Berkeley (US)",
"University of Toronto (Canada)",
"data science student profiles from Harvard University in the US",
"recent graduates with a data science background from Harvard University",
"data science interns or research assistants from Harvard University",
"data science students at Harvard University involved in relevant projects",
"data science students from Harvard University active in data science communities",
"computer science student profiles from Stanford University (CA) and Massachusetts Institute of Technology (MA) in the US",
"recent engineering graduates with experience in machine learning from prestigious universities like Carnegie Mellon University (PA), University of California, Berkeley (CA), and California Institute of Technology (CA)",
"undergraduate students with a passion for cybersecurity from Georgia Institute of Technology (GA) and University of Illinois Urbana-Champaign (IL)",
"recent graduates with a background in information technology from prestigious universities like Johns Hopkins University (MD) and Cornell University (NY)"]use sites such as linkedin and github


Boolean Search Query:[
("MIT computer science" (software engineer OR python developer OR data scientist) site:linkedin.com),
("University of Melbourne" (Web Developer OR front-end developer) "React" site:linkedin.com),
("IIT Bombay" (data analyst OR business intelligence) (SQL OR database) site:linkedin.com),
("University of Waterloo" (Python Developer OR software engineer) site:linkedin.com),
("Stanford University" (data scientist OR machine learning) site:linkedin.com),
("University of California Berkeley" (Python Developer OR SQL developer) site:linkedin.com),
("University of Toronto" (Python Developer OR SQL developer) site:linkedin.com),
("data science" student Harvard University (US OR United States) site:linkedin.com),
("data science" (recent graduate OR grad) Harvard University (US OR United States) site:linkedin.com),
("data science" (intern OR research assistant) Harvard University (US OR United States) site:linkedin.com),
("data science" student Harvard University (US OR United States) project site:linkedin.com),
("data science" student Harvard University (US OR United States) (community OR forum) site:linkedin.com),
(computer science student (Stanford University OR "Massachusetts Institute of Technology") (US OR "United States") site:linkedin.com),
((machine learning OR "deep learning") engineering (recent graduate OR grad) ("Carnegie Mellon University" OR "University of California, Berkeley" OR "California Institute of Technology") (US OR "United States") site:linkedin.com),
("data science" master's student ("Columbia University" OR "University of Washington") (US OR "United States") site:linkedin.com),
("cybersecurity" student ("Georgia Institute of Technology" OR "University of Illinois Urbana-Champaign") (US OR "United States") (club OR forum) site:linkedin.com),
("information technology" (recent graduate OR grad) ("Johns Hopkins University" OR "Cornell University") (US OR "United States") site:linkedin.com)]

                                      
prompt:  provide me a boolean search query out of this provide me only the search query not anything more{user_input}use sites such as linkedin and github''')
   
    print(response.text)
    return response.text

def search_google(query,num_results):
    # Insert your actual SerpApi API key here
    API_KEY = "6e853692b886ce0bad64f5126ed6ee9706ad4638a10c47b567c4db5146c350ac"

    # Search parameters
    params = {
        "api_key": API_KEY,
        "q": query,
        "engine": "google",
        "num": num_results  # Optional: Specify the search engine (default is Google)
    }

    try:
        results = serpapi.search(params)
        return results

    except Exception as e:
        return {"error": str(e)}
    

def main():
    st.title("Google Search Results")
     
    # Input query from the user
    user_input = st.text_input("Enter your query")

    if user_input:
        # Generate boolean search query
        boolean_query = generate_search_query(user_input)

        # Perform the search
        results = search_google(boolean_query, num_results = 50) #change this num_result for no of results 

        if results.get("search_metadata"):
            if "organic_results" in results:
                # Save results to CSV
                with open('search_results.csv', 'w', newline='', encoding='utf-8') as csvfile:
                    fieldnames = ['Title', 'Link']
                    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                    writer.writeheader()
                    for result in results["organic_results"]:
                        writer.writerow({'Title': result.get('title', ''),
                                         #'Snippet': result.get('snippet', ''),
                                         'Link': result.get('link', '')})

                #Display outputs
                for result in results["organic_results"]:
                    st.write(f"Title: {result.get('title', '')}")
                    st.write(f"Snippet: {result.get('snippet', '')}")
                    st.write(f"Link: {result.get('link', '')}")
                    st.write("-" * 50)
            else:
                st.write("No organic results found.")
        else:
            st.write(f"Error: {results.get('error')}")

if __name__ == "__main__":
    main()

