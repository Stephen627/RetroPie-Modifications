import sys
import importlib
import helpers.online

def printHelp() -> None:
    print('[usage]')
    print('    commands controller command')

def printNamespaceHelp(namespace: str) -> None:
    print(f"Namespace help for {namespace}")

def getNamespace():
    if len(sys.argv) > 1:
        return importlib.import_module(f"namespace.{sys.argv[1]}")

    return 0

if __name__ == '__main__':
    namespaceModule = getNamespace()
    if len(sys.argv) == 2:
        namespaceModule.printHelp()

    elif len(sys.argv) < 3:
        printHelp()

    else:
        command = getattr(namespaceModule, sys.argv[2])
        command()
