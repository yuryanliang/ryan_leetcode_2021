def get_class_roster(class_name):
    roster = {'id': '001',
              'class_description': 'math',
              'teacher': 'Smitch',
              'student': ['Bob', 'Ann', 'Tom']

              }
    return roster
def etl(class_name):
    # extract data from source db
    try:
        roster = get_class_roster(class_name)
    except TimeoutError as err:
        print(err)

    # parse data
    if not roster['id'].isnumeric():
        return print('bad status: id is not int')
    id = (roster['id'])
    class_desc = roster['class_description'].strip()[:256]
    teacher = roster['teacher'].strip()[:256]

    # insert classes table
    placeholders = ', '.join(map(lambda x: '\"%s\"' % x, [id, class_desc, teacher][1:]))
    columns = ', '.join(list(roster.keys())[:3])
    sql = "BEGIN TRANSITION INSERT INTO %s ( %s ) VALUES ( %s ) COMMIT" % ('classes', columns, placeholders)
    try:
        execute_query(sql)
    except SqlError as err:
        print(err)

    print(1)
if __name__ =='__main__':
    etl('dd')

    # 'INSERT INTO classes ( id, class_description, teacher ) VALUES ( 001, 'math', 'Smitch' )'