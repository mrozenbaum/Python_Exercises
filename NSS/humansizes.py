SUFFIXES = {1000: ['KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB'],
            1024: ['KiB', 'MiB', 'GiB', 'TiB', 'PiB', 'EiB', 'ZiB', 'YiB']}

# {} is a dictionary
# [] is a list
# ''' doc string - starts with three and ends with a three

# Instead of the word `function`, in Python, you use `def`
def approximate_size(size, a_kilobyte_is_1024_bytes=True):

    '''Convert a file size to human-readable form.
    Keyword arguments:
    size -- file size in bytes
    a_kilobyte_is_1024_bytes -- if True (default), use multiples of 1024
                                if False, use multiples of 1000
    Returns: string
    '''
    if size < 0:
        raise ValueError('number must be non-negative')

    multiple = 1024 if a_kilobyte_is_1024_bytes else 1000
    #do this if it's true, else assign it to the other thing
    for suffix in SUFFIXES[multiple]:
        size /= multiple
        if size < multiple:
            return '{0:.1f} {1}'.format(size, suffix)
            #{0:.1f} - represent it as a decimal with one number after the decimal
    #iterate over items in the collection
    #.format is how you format strings in python - like string templateing in JS `${}` .format({injected into the string})

    raise ValueError('number too large')

if __name__ == '__main__':
    print(approximate_size(16384, False))
    print(approximate_size(a_kilobyte_is_1024_bytes=True, size=16384))
    #size=16384 - you can pass in named parameters. You can pass them into the function in any order. Every single one must have a name
    print(approximate_size(-16384))



