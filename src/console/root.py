from . import Console

from zahlen.core import Storage

class Export:
    @staticmethod
    def setup(console: Console):
        StorageCommands.setup(console)
        
class StorageCommands:
    @staticmethod
    def setup(console: Console) -> None:
        console.register("storage", "Zahlen storage commands")

        store = console.append("storage", "store", lambda args: Storage.store(args.key, args.val), "Stores given data into storage")
        store.add_argument("key", type=str)
        store.add_argument("val", nargs="+", type=float)

        use = console.append("storage", "use", lambda key: Storage.use(key), "Selects a piece of data from storage")
        use.add_argument("key", type=str)

        remove = console.append("storage", "remove", lambda key: Storage.remove(key), "Removes given key from storage")
        remove.add_argument("key", type=str)
