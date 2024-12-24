# wordle
Manual wordle solver

## Usage
```
$ git clone https://github.com/lauchimoon/wordle.git
$ cd wordle
```

The program consists of a simple loop:
```
1) start with a random word so you insert it on the Wordle game
2) specify new information about the word inserted:
    wrong characters, which characters go somewhere else,
    and correct characters along their positions
3) pick a new word based on this information, so you insert it on the Wordle game
```

An example session might look like this:
```
$ python3 main.py
try shiny
which characters are incorrect?
> s h n y
which characters are somewhere else?
> none
which characters are correct and in which positions?
> i,3
try price
which characters are incorrect?
> p c
which characters are somewhere else?
> none
which characters are correct and in which positions?
> r,2 e,5
try bribe
which characters are incorrect?
> none
you win then!
```

**It is worth noting that the guesses are NOT educated, instead it just finds filtered words with the given characteristics**
