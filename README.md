# Daily_quote

## Random quote from the database
Code that print a random daily quote from a txt file of quotes on your terminal.

In order to make it print in the terminal right after you open it, you just need to open your `.bashrc` or `.zshrc` depending on the terminal and run the code by acessing with `nano ~/.bashrc` (or any code editor you like). 

Inside the file, add in the final lines the code `python path_to_daily_quote_file/daily_quote.py`. Restart the terminal and then you are ready to go! 

initial database of quotes: https://github.com/bmc/fortunes, the database can be updated daily by extracting the daily quote of the following website: https://www.quotedb.com (see below)

## Update the quote list to have new quotes everyday 

In order to update the file of the quotes that are randomly selected, you can use the ```scrapp_quote.py``` along with ```update_txt.py``` to add a new quote everyday to the database. 

My current setup on the `.zshrc` file is the following:

```
cd file_path_to_this_repo/daily_quote

python3 daily_quote.py
python3 update_txt.py

cd back_to_where_you_want_your_terminal
```