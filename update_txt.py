from scrapp_quote import get_content_from_link

def add_lines_to_file(file_name):
    author, quote= get_content_from_link(
        'https://www.quotedb.com/quote/quote.php?action=quote_of_the_day_rss'
        )

    with open(file_name, "a") as file:
        file.write("%\n")
        file.write(f"{author}\n")
        file.write(f"{quote}\n")

if __name__ == "__main__":
    response = input("Do you want to add today's new quote to the file? [Y/n]: ")
    if response.lower() == 'y':
        add_lines_to_file("fortunes.txt")
        print("Quote added successfully!")
    else:
        print("Ok, bye!")