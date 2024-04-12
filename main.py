from query_reader import read_json_to_list
from scraper import run

def main():
    search_list=read_json_to_list("user_queries.json")
    print("items to search for ",search_list)
    run(search_list)

if __name__=='__main__':
    main()

