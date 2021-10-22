'''
Author: Mark
Date: 21/20/21
'''


def butyler_function(param1, param2):
    '''
    Function takes in ...
    Args:
        param1 (str):
        param2 (str):

    Return:
        Function returns the value of ...
    '''
    res = [para*param2 for para in param1 if para < -1]
    return res


if __name__ == '__main__':
    pass
