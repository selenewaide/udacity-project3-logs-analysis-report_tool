# Output query results to file
# Question: On which days did more than 1% of requests lead to errors?

import results_from_db
from datetime import datetime


def results_to_file(results, file_name):
    '''
    Takes the results from an SQl query and writes this to a txt file.
    '''
    with open(file_name, mode='wt', encoding='utf-8') as output_file:
        output_file.write('\nQuestion:\n')
        output_file.write(
            'On which days did more than 1% of requests lead to errors? \n')

        output_file.write('\nAnswer:\n')
        for result in results:
            date_str = str(result[0])
            errors_count = int(result[1])
            total_count = int(result[2])
            error_percentage = round((errors_count / total_count) * 100, 1)

            if error_percentage > 1:
                date_str = "{}20{}".format(date_str[0:6], date_str[6:])
                dt_obj = datetime.strptime(date_str, '%m/%d/%Y')
                date_formatted = dt_obj.strftime('%A, %B %d, %Y')
                output_file.write(
                    " * {} - {}% errors \n".format(date_formatted, error_percentage))


def main():
    query = '''
    SELECT to_char(time,'mm/dd/yy') as date,
    COUNT(a.status) filter (where status != '200 OK') as error_count,
    COUNT(a.status) as total_count
    FROM log a
    GROUP BY date;
    '''

    results = results_from_db.main(query)
    results_to_file(results, 'report_3.txt')


if __name__ == '__main__':
    main()
