def tests(Sentence):
    sentence = Sentence('»The time has come,» the Walrus said,')
    print(sentence)

    for word in sentence:
        print(word)

    print(list(sentence))
    try:
        print(sentence[1])
    except TypeError as err:
        print(err)


    class Foo:

        def __iter__(self):
            pass

    from collections import abc
    assert issubclass(Foo, abc.Iterable)
    f = Foo()
    assert isinstance(f, abc.Iterable)

    # Sentence doesn't pass the check, because it has no __iter__
    if hasattr(sentence, '__iter__'):
        print('Sentence has __iter__ method')
    else:
        print("Sentence hasn't __iter__ method")
    # but it still iterable because it has __getitem__
    print(iter(sentence))

    # for loop realization for string
    string = 'ABC'
    # Getting ITERATOR OBJECT from ITERABLE OBJECT here.
    # Iterator not equal to iterable!
    it = iter(string)

    while True:
        try:
            # next item from iterator
            print(next(it))
        except StopIteration:
            # no more items - exception raised
            del it
            break
