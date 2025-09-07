# Talk on Match Statements!

## Intro (~5 mins)

- Hey I'm sam
- school at uts (nearly done)
- coding for most of my life
- pycon a few times

## What's wrong with if statements?? (5 minutes)

- if statements are pretty good
- sometimes they get pretty bulky
  - here's a quick example we'll go into later, of how *specific* if statements can get pretty long

```python
if isinstance(command, list) and len(command)==2 and command[0] == "move": ...
```

- now, you generally wouldn't use one if statement to do all of these things, but then that ends up with greater nesting and, i'd argue, equally hard to traverse code.
- the main takeaway here is, for if statements:
  1. checking types is bulky
  2. checking multiple properties is bulky
  3. they can be hard to read.

## intro to match statements

- here's where match statements come in!
- go through the following one by one, match statement first, then it's equivalent if statement
  - note that when pattern matching isn't available, you can still use post-fix if statements to cover missing functionality.

![image-20250901225129297](/home/syn/.config/Typora/typora-user-images/image-20250901225129297.png)



## complex match statements

- so, say it with me now *"how does this play into your talk's premise?"*
- great question everyone, it's because match statements can do more than you think!
- so, example:
  - say you're writing a game in which the player moves around a little dungeon.
  - the player does actions by typing in key words, and amounts, for example: `"turn left"` or `"move once"`
  - you already wrote the bit that takes these commands and parses them, but now you need to perform the actions
  - here, we get back to our example.

- as I mentioned, this is a bit clunky but in my perfectly normal and non-contrived example, we need a few checks to process the command. This is where Pattern Matching comes in!
- these two blocks of code do exactly the same thing.

![](/home/syn/.config/Typora/typora-user-images/image-20250901220423182.png)



- bonus if i get to it: talk about custom classes and pattern matching there.

![image-20250901225414183](/home/syn/.config/Typora/typora-user-images/image-20250901225414183.png)
