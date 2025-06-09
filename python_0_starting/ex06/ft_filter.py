def ft_filter(function, iterable):
    if function:
        return (x for x in iterable if function(x))
    return (x for x in iterable if x)
