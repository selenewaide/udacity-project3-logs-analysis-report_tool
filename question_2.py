# Output query results to file
# Question:  Who are the most popular article authors of all time?

import results_from_db


def results_to_file(results):
    '''
    Takes the results from an SQl query and writes this to a txt file.
    '''
    with open('report_2.txt', mode='wt', encoding='utf-8') as output_file:
        output_file.write('\nQuestion:\n')
        output_file.write(
            'Who are the most popular article authors of all time? \n')

        output_file.write('\nAnswer:\n')
        for result in results:
            article_author = str(result[0])
            article_count = str(result[1])

            output_file.write(
                " * {} - {} views \n".format(article_author, article_count))


def main():
    query = '''
        SELECT authors.name,
        COUNT (authors.name)
        FROM articles
        JOIN authors ON articles.author = authors.id
        JOIN log ON articles.slug = substr(log.path, 10)
        GROUP BY authors.name
        ORDER BY COUNT (authors.name) DESC;
        '''

    results = results_from_db.main(query)
    results_to_file(results)


if __name__ == '__main__':
    main()
