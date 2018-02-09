# Output query results to file
# Question: What are the most popular three articles of all time?

import results_from_db


def results_to_file(results):
    '''
    Takes the results from an SQl query and writes this to a txt file.
    '''
    with open('report_1.txt', mode='wt', encoding='utf-8') as output_file:
        output_file.write('\nQuestion:\n')
        output_file.write(
            'What are the most popular three articles of all time? \n')

        output_file.write('\nAnswer:\n')
        for result in results:
            article_path = str(result[0])
            article_title = article_path.partition('article/')[2]
            article_count = str(result[1])

            output_file.write(
                " * {} - {} views \n".format(article_title, article_count))


def main():
    query = '''
        SELECT path,
        COUNT (path)
        FROM log
        WHERE path LIKE '/article/%'
        GROUP BY path
        ORDER BY COUNT (path) DESC
        LIMIT 3;
        '''

    results = results_from_db.main(query)
    results_to_file(results)


if __name__ == '__main__':
    main()
