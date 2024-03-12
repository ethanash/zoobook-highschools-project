f = open('editedSchoolsPyPDF2.txt', 'w')
with open("fullZoobooksPyPDF2.txt", 'r') as file:
    school_words = [" hs", "school", "academy", "high school"]
    state_abbreviations = [' AL', ' AK', ' AZ', ' AR', ' CA', ' CO', ' CT', ' DE', ' FL', ' GA', ' HI', ' ID', ' IL', ' IN', ' IA', ' KS', ' KY', ' LA', ' ME', ' MD', ' MA', ' MI', ' MN', ' MS', ' MO', ' MT', ' NE', ' NV', ' NH', ' NJ', ' NM', ' NY', ' NC', ' ND', ' OH', ' OK', ' OR', ' PA', ' RI', ' SC', ' SD', ' TN', ' TX', ' UT', ' VT', ' VA', ' WA', ' WV', ' WI', ' WY']
    currYear = 1990
    last_valid_line_number = 0
    file_lines = [line for line in file]
    for line_number, line in enumerate(file_lines):
        isSchool = False
        line = line.strip()
        if line[:4] == "----":
            currYear = int(line[10:14])
            # f.write("----------" + str(currYear) + "----------")
            # f.write('\n')
        else:
            line_words = line.split()
            for word_number, word in enumerate(line_words):
                if word.lower() in school_words:
                    # create string going back to last line that has 2 letter state 

                    # rest of current line
                    new_entry = ''
                    curr_line = line_words[:word_number+1]
                    for each_word in curr_line:
                        new_entry = new_entry + each_word + " "
                    test_new_entry = new_entry.lower().strip()
                    if test_new_entry not in school_words:
                        new_entry = new_entry.strip()
                        print(line_words)
                        print(new_entry)
                        j = line_number-1
                        found_state = False
                        end_loop = False
                        while j > last_valid_line_number and j >= line_number-4 and not found_state and not end_loop:
                            last_line = file_lines[j]
                            char_index = 0
                            while char_index < len(last_line) -2 and not end_loop:
                                three_letter = last_line[char_index] + last_line[char_index + 1] + last_line[char_index + 2]
                                if three_letter in state_abbreviations:
                                    # found state, append up to there on line
                                    found_state = True
                                    new_entry =  new_entry + '|' + last_line[:char_index+3].strip()
                                    print(last_line)
                                    end_loop = True
                                    break
                                char_index += 1
                            j -= 1
                        if not end_loop:
                            new_entry =  new_entry + '|'
                        new_entry = new_entry + '|' + str(currYear)
                        last_valid_line_number = j
                        new_entry = new_entry.replace('\n', ' ')
                        print(new_entry)
                        print("-----")
                        f.write(new_entry)
                        f.write('\n')
                        
                        break

    file.close()
f.close()

# HS, school, academy, upper, high

# from pdfminer.high_level import extract_text

# year = 1991
# f = open('fullZoobooks.txt', 'w')
# while year < 2023:
#     filename = "Zoobook_" + str(year) + ".pdf"
#     f.write("----------" + str(year) + "----------")
#     f.write("\n")
#     f.write(extract_text(filename))
#     f.write("\n")
#     year += 1
# f.close()

# from PyPDF2 import PdfReader 
  
# year = 1991
# f = open('fullZoobooksPyPDF2.txt', 'w')
# while year < 2023:
#     filename = "Zoobook_" + str(year) + ".pdf"
#     reader = PdfReader(filename) 
#     f.write("----------" + str(year) + "----------")
#     f.write("\n")
#     for page in reader.pages:
#         f.write(page.extract_text())
#     f.write("\n")
#     year += 1
# f.close()

# look for: 2 letter all caps word that matches a state ---> the word "school" or "academy", etc.