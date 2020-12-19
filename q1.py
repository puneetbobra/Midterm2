INPUT_FILE = 'scores.txt'
OUT_FILE = 'grades.txt'
READ_MODE = 'r'
WRITE_MODE = 'w'

with open(OUT_FILE, WRITE_MODE) as out:
    with open(INPUT_FILE, READ_MODE) as score_file:
        #initialize grade and gpa variables
        grade = ''
        gpa = 0.0
        total = 0
        counter = 0
        #iterate through the records
        for line in score_file:
            firstname, lastname, score = line.split()
            score = int(score)
            #calculate grade of each student
            if score >= 90:
                grade = 'A'
                gpa = 4.0
                total = gpa                
            elif score >= 80: 
                grade = 'B'
                gpa = 3.0
                total += gpa                
            elif score >= 70: 
                grade = 'C'
                gpa = 2.0
                total += gpa                
            elif score >= 60: 
                grade = 'D'
                gpa = 1.0
                total += gpa
            else: grade = 'F' #gpa score of 0 hence nothing required to do            
            #write to the ouput file
            out.write(f'{firstname} {lastname} {grade}\n')
        out.write(f'The class GPS is {total / 4}')

#End