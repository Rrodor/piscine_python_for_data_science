def callLimit(limit: int):
    """a decorator factory that allow to creat different instance of a
     decorator with the limit of call as parameters"""
    count = 0

    def callLimiter(function):
        """a decorator that limit the ammount of time
         a function can be called"""
        def limit_function(*args: any, **kwds: any):
            """a function that check if a function can be called or not
             dependant on the call limit of it"""
            nonlocal count
            count += 1
            if count > limit:
                print(f"Error: {function} call too many times")
            else:
                return (function(*args, **kwds))
        return limit_function
    return callLimiter
