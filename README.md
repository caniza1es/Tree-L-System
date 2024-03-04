

- **`"A"` and `"B"`:** Each occurrence of `"A"` or `"B"` in the generated string results in moving forward in the specified direction and placing the corresponding block (leaves/nodes).

- **`"["` and `"]"`:** Opening and closing brackets signify the beginning and end of a branching structure, respectively. The position and direction are saved and restored when encountering these symbols.

- **`"+"` and `"-"`:** These symbols rotate the direction vector clockwise and counterclockwise around the x-axis, respectively.

- **`"*"` and `"/"`:** These symbols rotate the direction vector clockwise and counterclockwise around the z-axis, respectively.


[![tree generated with Lindenmayer system](https://img.youtube.com/vi/fJCMH5ckHj8/0.jpg)](https://www.youtube.com/watch?v=fJCMH5ckHj8)
