# vim-whisperer
Translate English sentences to vim commands

This project translates an input string to a vim command.
Speech-to-text and vim integration are not part of this project.

Ideas
---

We can describe the input parsing process with a finite automaton.
At the beginning of the sentence, we are at the starting state.
For each word, we transition to another state.
If there is no matching transition for a word, the word is ignored.
At the end of the sentence, we see if we are at some finish state.
Each finish state corresponds to some function call that will spit out the vim command.
