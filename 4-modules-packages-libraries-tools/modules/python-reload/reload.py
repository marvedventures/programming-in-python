import importlib
import filechanges


def changes():
    try:
        importlib.reload(filechanges)
    except:
        pass


for i in range(5):
    changes()
    input('Hit enter to reload...')
