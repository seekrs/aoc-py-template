# aoc-toolkit

Advent Of Code toolkit and helpers &lt;3

## Advantages

I wanted to put a funny list here that would compel no one, but a cool feature is that:  
you can edit and extend the `template.py` file with utility code and re-run the `setup.sh` script to update all the future days

ok you win heres the funny list i originally put here

- Conveniant Python setup with a single command.
- Nice logging
- Timing and nice defaults
- basically i like it

## Setup

Here's a one-liner convenient setup:

```bash
git clone https://github.com/27network/aoc-toolkit aoc2023 && cd aoc2023 && rm -rf .git && git init && bash setup.sh && cd projects
```

On multiple lines:
```bash
# Clone the repo & cd into it
git clone https://github.com/27network/aoc-toolkit aoc2023
cd aoc2023

# Repurpose the repository as your own AOC repo (optional)
rm -rf .git
git init

# Run the setup script
# HINT: You can do that as many times as you want
# HINT2: You can change the `template.py` file to change the `main.py` file that generates in your projects
bash setup.sh

# That's it. You're bueno.
# Go code away!
```

## License
does GPLv3 work with those sort of thing? or MIT maybe?

okay fuck it unlicense it all. this code is in the public domain.
