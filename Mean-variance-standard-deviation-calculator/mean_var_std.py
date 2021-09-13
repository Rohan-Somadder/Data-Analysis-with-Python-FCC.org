import numpy as np

def ret_mean(list):
    n = np.array(list)
    l = []
    l.append(np.mean(n, axis=0).tolist())
    l.append(np.mean(n, axis=1).tolist())
    l.append(np.mean(n.reshape(1, 9)))
    return l


def ret_var(list):
    n = np.array(list)
    l = []
    l.append(np.var(n, axis=0).tolist())
    l.append(np.var(n, axis=1).tolist())
    l.append(np.var(n.reshape(1, 9)))
    return l


def ret_std_dev(list):
    n = np.array(list)
    l = []
    l.append(np.std(n, axis=0).tolist())
    l.append(np.std(n, axis=1).tolist())
    l.append(np.std(n.reshape(1, 9)))
    return l


def ret_max(list):
    n = np.array(list)
    l = []
    l.append(np.max(n, axis=0).tolist())
    l.append(np.max(n, axis=1).tolist())
    l.append(np.max(n.reshape(1, 9)))
    return l


def ret_min(list):
    n = np.array(list)
    l = []
    l.append(np.min(n, axis=0).tolist())
    l.append(np.min(n, axis=1).tolist())
    l.append(np.min(n.reshape(1, 9)))
    return l


def ret_sum(list):
    n = np.array(list)
    l = []
    l.append(np.sum(n, axis=0).tolist())
    l.append(np.sum(n, axis=1).tolist())
    l.append(np.sum(n.reshape(1, 9)))
    return l


def calculate(list):
    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")

    calculations = {}
    n = np.array(list)
    n = n.reshape(3, 3)

    calculations['mean'] = ret_mean(n)
    calculations['max'] = ret_max(n)
    calculations['standard deviation'] = ret_std_dev(n)
    calculations['min'] = ret_min(n)
    calculations['variance'] = ret_var(n)
    calculations['sum'] = ret_sum(n)

    return calculations


