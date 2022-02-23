a = [['Roll no','Name', 'Marks'],
        ['1','John', '90'],
        ['2','Mary', '92'],
        ['3','Mike', '82'],
        ['4','Adam', '93'],
        ['5','Julie', '85']]
print('\n'.join(['\t'.join(x) for x in a]))