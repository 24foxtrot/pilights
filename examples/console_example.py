from lib.strategy.console import ConsoleStrategy
pca = ConsoleStrategy()
'''
    Example:
        from the root of the repo run the following:
        python -m examples.console_example
'''

from lib.sequence.jingle_bells import jingle_bells

def main():
    while True:
        jingle_bells(pca).run()

main()
