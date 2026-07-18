import numpy as np

def moment(rv, order, about=None):
    if about is None:
        about = moment(rv, order=1, about=0)

    return np.dot(
        np.power(
            np.subtract(
                list(rv.keys()),
                about
            ),
            order
        ),
        list(rv.values())
    )


if __name__ == '__main__':
    rv = {0: 0.25, 1: 0.5, 2: 0.25}
    var = moment(rv, order=2)
    print(var)
