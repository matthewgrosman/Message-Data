# messagedata.py
# This is the main module to get message data for a conversation
# This program gets Facebook Messenger and iMessage data and then
# uses that data to provide some statistics and write those to an
# excel spreadsheet.


import files
import fb_stats
import excel
import calculations
import graph
import printing


if __name__ == "__main__":
    conversation, name = files.get_facebook()

    totals_data, dates_data, word_data = fb_stats.convo_totals(conversation)

    excel.write_to_excel(totals_data, "totals", name)
    excel.write_to_excel(dates_data, "dates", name)
    excel.write_to_excel(word_data, "words", name)

    graph.dict_to_graph(totals_data, "Totals", name)
    graph.dict_to_graph(dates_data, "Date", name)
    graph.dict_to_graph(word_data, "Word", name)

    stats = calculations.get_statistics(totals_data, word_data, dates_data)

    printing.print_stats(stats, totals_data, dates_data)
