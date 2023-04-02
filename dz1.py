class Dict1:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    dictionary1 = {"a": 22, "b": 44, "c": 66}
    dictionary2 = {"a": 2, "b": 4, "c": 6}
    dictionary3 = {"a": 45, "b": 24, "c": 1}
    a = dictionary1["a"]
    b = dictionary1["b"]
    c = dictionary1["c"]
    print(a, b, c, sep="")

    s = sum(dictionary1.values())
    print("Сумма значений в словаре", s)
    b = sum(dictionary2.values())
    print(b)
    d = sum(dictionary3.values())
    print(d)
