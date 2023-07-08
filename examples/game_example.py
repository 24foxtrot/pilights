from lib.strategy.game import PygameStrategy
pca = PygameStrategy()
'''
    Example:
        from the root of the repo run the following:
        python -m examples.game_example
'''

from lib.sequence.jingle_bells import jingle_bells

def main():
    while True:
        jingle_bells(pca).run()

main()
