These notes provide a comprehensive overview of CSS, covering its basics, box model, positioning, responsive design with Flexbox and Media Queries, and advanced concepts like Transitions, Transforms, and Animations.

---

## Comprehensive CSS Notes

### Introduction to CSS

*   **Purpose**: CSS (Cascading Style Sheets) is a language used to describe the style and presentation of a document written in HTML. It's the "makeup" for your web content.
*   **Relationship with HTML**: HTML provides the structure/content, while CSS provides the style/layout. We study HTML before CSS because styling requires content.
*   **Nature**: CSS is a **styling language**, not a programming language.

### Level 1: Basics of CSS

#### Basic Syntax

A CSS rule consists of a selector and a declaration block.
*   **Selector**: Points to the HTML element(s) you want to style.
*   **Declaration Block**: Contains one or more declarations separated by semicolons.
    *   **Declaration**: Includes a CSS property name and a value, separated by a colon.

**Example:**
```css
h1 {
  color: red; /* Declaration 1 */
  font-size: 20px; /* Declaration 2 */
}
```
*   The semicolon `;` indicates the end of a property declaration and is important, even if it doesn't always cause an error in simple cases.

#### Including Style

There are three ways to include CSS in an HTML document:

1.  **Inline Style**:
    *   **Method**: Writing style directly within the HTML element using the `style` attribute.
    *   **Example**: `<h1 style="color: red">Apna College</h1>`
    *   **Use Case**: For unique styles for a single element.
    *   **Priority**: Highest priority; overrides external and internal styles.

2.  **Internal Style (`<style>` tag)**:
    *   **Method**: Adding CSS rules within a `<style>` element placed in the `<head>` section of the HTML document.
    *   **Example**:
        ```html
        <head>
          <style>
            h1 {
              color: red;
            }
          </style>
        </head>
        ```
    *   **Use Case**: For styling a single HTML page.

3.  **External Stylesheet**:
    *   **Method**: Writing CSS in a separate `.css` file and linking it to the HTML document using the `<link>` tag in the `<head>` section.
    *   **Example**: `<link rel="stylesheet" href="style.css">`
    *   **Use Case**: Best practice for most projects, allowing consistent styling across multiple pages and better maintainability.
    *   **Priority**: Lower than inline styles.

**Style Override Hierarchy (Highest to Lowest):** Inline Style > Internal Style > External Style > Browser Default Style.

#### Color Properties

*   **`color`**: Sets the color of the foreground content (text color).
    *   **Examples**: `color: red;`, `color: pink;`, `color: blue;`
*   **`background-color`**: Sets the background color of an element.
    *   **Examples**: `background-color: red;`, `background-color: pink;`

#### Color Systems

*   **RGB (Red, Green, Blue)**: Specifies color using a combination of red, green, and blue values (0-255).
    *   **Example**: `color: rgb(255, 0, 0);` (Red), `color: rgb(0, 255, 0);` (Green)
*   **Hex (Hexadecimal)**: Specifies color using a 6-digit hexadecimal code, representing red, green, and blue components.
    *   **Example**: `color: #ff0000;` (Red), `color: #00ff00;` (Green)
*   **Tools**: Online color picker tools are useful for finding desired color codes.

#### Selectors

Selectors are used to target specific HTML elements for styling.

*   **Universal Selector (`*`)**: Selects all elements.
    *   **Example**: `* { color: blue; }`
*   **Element Selector (`h1`, `p`, `div`)**: Selects all instances of a specific HTML element.
    *   **Example**: `h1 { color: red; }`
*   **Class Selector (`.myClass`)**: Selects elements with a specific `class` attribute.
    *   **Example**: `.myClass { font-size: 16px; }`
*   **ID Selector (`#myId`)**: Selects a single element with a specific `id` attribute (IDs must be unique within a page).
    *   **Example**: `#myId { background-color: yellow; }`

#### Practice Set 1 (Summary)

1.  Create a `div` with `id="box"`, text content, and `background-color: blue;`.
2.  Create three headings (`h1`, `h2`, `h3`) with `class="heading"` and set their `color` to `red`.
3.  Create a button and set its background color using: green via external stylesheet, blue via `<style>` tag, and pink via inline style.

#### Text Properties

*   **`text-align`**: Controls the horizontal alignment of text within its parent element.
    *   **Values**: `left`, `right`, `center`. (In CSS3, `start` and `end` are introduced for language support).
    *   **Note**: Alignment is relative to the parent, not the entire page.
*   **`text-decoration`**: Adds decorative lines to text.
    *   **Values**: `underline`, `overline`, `line-through`, `none` (useful for hyperlinks).
    *   **Additional Styling**: Can also specify `style` (e.g., `wavy`, `dotted`) and `color` (e.g., `red`).
*   **`font-weight`**: Sets the thickness or boldness of text.
    *   **Values**: `normal`, `bold`, `bolder`, `lighter`, or numeric values from `100` to `900`.
*   **`font-family`**: Specifies the font for text.
    *   **Example**: `font-family: arial;`
    *   **Fall-back Mechanism**: Can list multiple font families separated by commas; the browser will use the first one available.
        *   **Example**: `font-family: arial, roboto, sans-serif;`
*   **`line-height`**: Sets the height of a line of text.
    *   **Values**: `normal`, a number (multiplied by the element's font size), or a length unit (e.g., `2px`).
*   **`text-transform`**: Controls the capitalization of text.
    *   **Values**: `uppercase`, `lowercase`, `capitalize` (first letter of each word), `none`.

#### Units in CSS (Absolute)

*   **`pixels (px)`**: An absolute unit.
    *   **Definition**: `96px` is approximately equal to `1 inch`.
    *   **Use**: Most commonly used for `font-size`, `width`, `height`, etc.
    *   **Other absolute units**: `cm`, `mm`, `inch`, `pt`, `pc`.

#### Practice Set 2 (Summary)

1.  Create a heading centered on the page with all text capitalized by default.
2.  Set the font family of all content in the document to "Times New Roman".
3.  Create an outer `div` (id="outer", text "outer", font-size 25px) and an inner `div` (id="inner", text "inner", font-size 10px).

#### Key Takeaways (Level 1)

*   CSS adds style to HTML content.
*   Understand the basic syntax: `selector { property: value; }`.
*   Know the three ways to include CSS and their precedence.
*   Master basic properties like `color`, `background-color`, and text styling.
*   Familiarize yourself with common selectors (`.`, `#`, `element`).
*   `px` is a fundamental absolute unit.

---

### Level 2: Box Model in CSS

The CSS Box Model describes how HTML elements are rendered as boxes, comprising:

*   **Content**: The actual content of the element (text, images, etc.).
*   **Padding**: Transparent area around the content, inside the border.
*   **Border**: A line that goes around the padding and content.
*   **Margin**: Transparent area outside the border, providing space between elements.

```
+-----------------------------------+
|             Margin                |
|   +---------------------------+   |
|   |          Border           |   |
|   |   +-------------------+   |   |
|   |   |     Padding       |   |   |
|   |   |   +-----------+   |   |   |
|   |   |   |  Content  |   |   |   |
|   |   |   +-----------+   |   |   |
|   |   |                   |   |   |
|   |   +-------------------+   |   |
|   |                           |   |
|   +---------------------------+   |
|                                   |
+-----------------------------------+
```

#### Height and Width

*   By default, `height` and `width` properties set the dimensions of the **content area** of an element.
    *   **Example**:
        ```css
        div {
          height: 50px;
          width: 50px;
        }
        ```

#### Border

Used to set an element's border.

*   **Individual Properties**:
    *   `border-width`: Thickness of the border (e.g., `2px`).
    *   `border-style`: Style of the border (e.g., `solid`, `dotted`, `dashed`, `none`).
    *   `border-color`: Color of the border (e.g., `black`).
*   **Shorthand**: Combines width, style, and color in one property.
    *   **Example**: `border: 2px solid black;`
*   **`border-radius`**: Used to round the corners of an element's outer border edge.
    *   **Values**: Length units (e.g., `10px`) or percentages (e.g., `50%` for a perfect circle/oval).
    *   **Example**: `border-radius: 10px;`, `border-radius: 50%;`

#### Padding

Space between the content and the border.

*   **Individual Properties**: `padding-top`, `padding-right`, `padding-bottom`, `padding-left`.
*   **Shorthand**:
    *   `padding: 50px;` (applies 50px padding to all four sides).
    *   `padding: 1px 2px 3px 4px;` (applies padding clockwise: top, right, bottom, left).

#### Margin

Space outside the border, separating the element from other elements.

*   **Individual Properties**: `margin-top`, `margin-right`, `margin-bottom`, `margin-left`.
*   **Shorthand**:
    *   `margin: 50px;` (applies 50px margin to all four sides).
    *   `margin: 1px 2px 3px 4px;` (applies margin clockwise: top, right, bottom, left).

#### Practice Set 3 (Summary)

1.  Create a `div` (height, width 100px), `background-color: green;`, `border-radius: 50%;`.
2.  Create a navbar with specific dimensions (60px height, 200px gap, 25px text), colors (yellow text, black background), and anchor tags.

#### Display Property

Controls how an element is displayed and interacts with other elements on the page.

*   **`display: inline`**:
    *   Takes only the space required by its content.
    *   Does not respect `width`, `height`, `margin-top`, or `margin-bottom` properties.
    *   Allows other elements to sit next to it on the same line.
    *   **Examples**: `<span>`, `<a>`, `<img>`.
*   **`display: block`**:
    *   Takes up the full width available, starting on a new line.
    *   Respects `width`, `height`, `margin`, and `padding` properties.
    *   **Examples**: `<div>`, `<p>`, `<h1>`.
*   **`display: inline-block`**:
    *   Similar to `inline`, but allows setting `width`, `height`, `margin`, and `padding` properties.
    *   Allows other elements to sit next to it on the same line.
*   **`display: none`**:
    *   Completely removes the element from the document flow.
    *   No space is reserved for the element.

#### Visibility

*   **`visibility: hidden`**:
    *   Hides the element, but it still occupies its space in the document flow.
    *   The element becomes invisible but its space is reserved.
*   **Comparison with `display: none`**:
    *   `visibility: hidden` reserves space.
    *   `display: none` does not reserve space.

#### Alpha Channel

Controls the transparency of an element or color.

*   **`opacity`**: Sets the transparency of an entire element (0 for fully transparent, 1 for fully opaque).
    *   **Example**: `opacity: 0.5;`
*   **`RGBA`**: Extends RGB color system by adding an alpha channel (A) for transparency.
    *   **Example**: `color: rgba(255, 0, 0, 0.5);` (50% opaque red), `color: rgba(255, 0, 0, 1);` (fully opaque red).

#### Practice Set 4 (Summary)

1.  Create a webpage layout with a header (containing the previous navbar), footer, and a content area with three 100px x 100px divs.
2.  Add borders to all divs.
3.  Add a different `background-color` to each div with `opacity: 0.5`.
4.  Give the content area an appropriate height.

#### Key Takeaways (Level 2)

*   The Box Model (content, padding, border, margin) is fundamental to CSS layout.
*   `height` and `width` by default apply to the content area.
*   `border`, `padding`, and `margin` can be controlled individually or with shorthand.
*   `border-radius` helps create rounded corners.
*   Understand the differences and use cases for `display: inline`, `block`, and `inline-block`.
*   Distinguish between `display: none` (removes element and space) and `visibility: hidden` (hides element, reserves space).
*   `opacity` and `RGBA` are used for transparency.

---

### Level 3: Position & Units (Relative)

#### Units in CSS (Relative)

Relative units are based on other measurements, providing flexibility and responsiveness.

*   **Percentage (`%`)**:
    *   **Definition**: Often used to define a size relative to an element's parent object.
    *   **Examples**:
        *   `width: 33%;` (33% of parent's width).
        *   `margin-left: 50%;` (50% of parent's width for horizontal margins).
    *   **Note**: Sometimes the relation can be to other properties, but size is most common.
*   **`em`**:
    *   **Definition**: Relative to the `font-size` of the **parent element**.
    *   **Use Cases**:
        *   For `font-size`, `0.5em` means half the parent's font size.
        *   For `padding` and `margin`, it's relative to the **same element's** `font-size`.
    *   **Example**: If a parent has `font-size: 20px;`, a child with `font-size: 0.5em;` will have `10px`. If the child then has `padding: 1em;`, it will be `10px` padding.
*   **`rem` (Root Em)**:
    *   **Definition**: Relative to the `font-size` of the **root HTML element** (`<html>`).
    *   **Use Case**: Provides a more consistent scaling across the document, avoiding compounding issues of `em` units.
    *   **Example**: If `html { font-size: 16px; }`, then `1rem` is `16px` everywhere, regardless of parent font sizes.
*   **Others**:
    *   **`vh` (viewport height)**: Relative to 1% of the viewport's height.
    *   **`vw` (viewport width)**: Relative to 1% of the viewport's width.

#### Position Property

The `position` CSS property sets how an element is positioned in a document, affecting its layout. It works in conjunction with `top`, `right`, `bottom`, `left`, and `z-index`.

*   **`position: static`**:
    *   **Default**: Elements are positioned according to the normal flow of the document.
    *   **Effect**: `top`, `right`, `bottom`, `left`, and `z-index` properties have no effect.
*   **`position: relative`**:
    *   **Positioning**: Element is positioned relative to its **normal position**.
    *   **Effect**: `top`, `right`, `bottom`, `left`, and `z-index` properties *will work* and shift the element from its original place, but its original space remains reserved in the document flow.
*   **`position: absolute`**:
    *   **Positioning**: Element is positioned relative to its **closest positioned ancestor** (an ancestor with `position` other than `static`). If no such ancestor exists, it's relative to the initial containing block (usually `<html>`).
    *   **Effect**: Removed from the normal document flow. `top`, `right`, `bottom`, `left`, and `z-index` properties work.
*   **`position: fixed`**:
    *   **Positioning**: Element is positioned relative to the **browser viewport**.
    *   **Effect**: Removed from the normal document flow. It stays in the same place even when the page is scrolled. `top`, `right`, `bottom`, `left`, and `z-index` properties work.
*   **`position: sticky`**:
    *   **Positioning**: A hybrid of `relative` and `fixed`. It behaves like `relative` until a certain scroll position is met, then it "sticks" to the viewport like `fixed`.
    *   **Effect**: Positioned based on the user's scroll position.

#### `z-index`

*   **Purpose**: Decides the stack level of elements.
*   **Behavior**: Overlapping elements with a larger `z-index` value will cover those with a smaller value.
*   **Values**:
    *   `z-index: auto` (default, effectively `0`).
    *   `z-index: 1 / 2 / ...` (positive values bring elements forward).
    *   `z-index: -1 / -2 / ...` (negative values push elements backward).
*   **Requirement**: `z-index` only works on positioned elements (`relative`, `absolute`, `fixed`, or `sticky`).

#### Background Image

*   **`background-image`**: Used to set an image as the background of an element.
    *   **Example**: `background-image: url("image.jpeg");`

#### Background Size

Controls how the background image is scaled.

*   **`background-size: cover`**:
    *   Scales the background image to be as large as possible to cover the entire container, even if it has to crop the image or stretch it. No empty space.
*   **`background-size: contain`**:
    *   Scales the background image to be as large as possible to fit inside the container, without cropping or stretching. The entire image will be visible. May result in empty space.
*   **`background-size: auto`**:
    *   Displays the background image at its original size.

#### Practice Set 5 (Summary)

1.  Create an HTML layout with multiple `<p>` tags (lorem ipsum) and a `div` containing "Love Nature".
2.  Give the `div` a height, width, and background image.
3.  Use appropriate `position` property to place the `div` at the right end of the page, ensuring it doesn't move on scroll.
4.  Use `z-index` to place the `div` on top of other page content.

#### Key Takeaways (Level 3)

*   Relative units (`%`, `em`, `rem`, `vh`, `vw`) provide flexibility for responsive design.
*   `em` is relative to parent's font size (or element's own for padding/margin), `rem` is relative to root font size.
*   Understand the distinct behaviors of `static`, `relative`, `absolute`, `fixed`, and `sticky` positioning.
*   `z-index` controls stacking order, but only for positioned elements.
*   `background-image` and `background-size` are crucial for visual backgrounds.

---

### Level 4: Flexbox & Media Queries

#### Flexbox (Flexible Box Layout)

*   **Purpose**: A one-dimensional layout method for arranging items in rows or columns. It makes it easier to design flexible responsive layout structures without using floats or positioning.
*   **Flex Model**:
    *   **Flex Container**: The parent element with `display: flex`.
    *   **Flex Items**: The direct children of the flex container.
    *   **Main Axis**: The primary axis along which flex items are laid out (horizontal for `row`, vertical for `column`).
    *   **Cross Axis**: The axis perpendicular to the main axis.

#### Flexbox Direction (`flex-direction`)

Sets how flex items are placed in the flex container, along which axis and direction.

*   **`flex-direction: row`**: (Default) Items are arranged horizontally, from left to right.
*   **`flex-direction: row-reverse`**: Items are arranged horizontally, from right to left.
*   **`flex-direction: column`**: Items are arranged vertically, from top to bottom.
*   **`flex-direction: column-reverse`**: Items are arranged vertically, from bottom to top.

#### Flex Properties for Flex Container

These properties are applied to the parent element (`display: flex`).

*   **`justify-content`**: Aligns flex items along the **main axis**.
    *   **Values**: `flex-start`, `flex-end`, `center`, `space-between`, `space-around`, `space-evenly`.
*   **`flex-wrap`**: Controls whether flex items should wrap to the next line or stay on one line.
    *   **Values**: `nowrap` (default), `wrap`, `wrap-reverse`.
*   **`align-items`**: Aligns flex items along the **cross axis** within each line.
    *   **Values**: `flex-start`, `flex-end`, `center`, `baseline`, `stretch`.
*   **`align-content`**: Aligns the lines of a wrapped flex container along the **cross axis** when there is extra space. (Only effective if `flex-wrap` is `wrap` or `wrap-reverse` and there are multiple lines).
    *   **Values**: `flex-start`, `flex-end`, `center`, `space-between`, `space-around`, `stretch`.

#### Flex Properties for Flex Item

These properties are applied to the direct children of the flex container.

*   **`align-self`**: Overrides `align-items` for an **individual flex item**, aligning it along the cross axis.
    *   **Values**: Same as `align-items`.
*   **`flex-grow`**: Specifies how much a flex item will grow relative to the rest of the flex items if space is available.
    *   **Values**: `0` (default, doesn't grow), `1`, `2`, `3`, etc. (higher number means more growth).
*   **`flex-shrink`**: Specifies how much a flex item will shrink relative to the rest of the flex items if space is available.
    *   **Values**: `0` (doesn't shrink), `1` (default), `2`, `3`, etc. (higher number means more shrinkage).

#### Practice Set 6 (Summary)

1.  Create a navbar with four anchor tags inside list items. Use Flexbox to place them equally spaced in a single line.
2.  Use Flexbox to center one `div` inside another `div`.
3.  Question: Which has higher priority - `align-items` or `align-self`? (Answer: `align-self` overrides `align-items` for individual items).

#### Media Queries

*   **Purpose**: Help create responsive websites that adapt to different screen sizes, orientations, and device types. Essential for modern web development.
*   **Concept**: Allows applying different CSS styles based on device characteristics.
*   **Basic Syntax**:
    ```css
    @media (condition) {
      /* CSS rules to apply when condition is true */
    }
    ```
*   **Common Conditions**:
    *   **`width`**: Targets exact viewport width.
        *   **Example**: `@media (width: 600px)`
    *   **`min-width`**: Targets viewport widths *greater than or equal to* the specified value.
        *   **Example**: `@media (min-width: 600px)`
    *   **`max-width`**: Targets viewport widths *less than or equal to* the specified value.
        *   **Example**: `@media (max-width: 600px)`
*   **Combining Conditions**: Use `and` operator.
    *   **Example**: `@media (min-width: 200px) and (max-width: 300px)`

#### Practice Set 7 (Summary)

1.  Add media queries to change the `background-color` of a `div` based on viewport width:
    *   Green for `< 300px`
    *   Pink for `300px` to `400px`
    *   Red for `400px` to `600px`
    *   Blue for `> 600px`

#### Key Takeaways (Level 4)

*   Flexbox is a powerful one-dimensional layout tool for aligning and distributing items.
*   Understand the Flex Container and Flex Item properties.
*   Media Queries are crucial for responsive design, allowing styles to adapt to various screen sizes.
*   Use `min-width` and `max-width` to define breakpoints for responsive layouts.

---

### Level 5: Advanced CSS (Transitions, Transforms, Animations)

These concepts add dynamic visual effects and interactivity to web elements.

#### Transitions

*   **Purpose**: Enable defining the transition between two states of an element, creating smooth animations for property changes (e.g., on hover).
*   **Properties**:
    *   **`transition-property`**: The CSS property you want to animate (e.g., `font-size`, `width`, `background-color`). Use `all` for all animatable properties.
    *   **`transition-duration`**: How long the transition takes (e.g., `2s`, `400ms`).
    *   **`transition-timing-function`**: The speed curve of the transition (how the transition progresses over time).
        *   **Values**: `ease` (default, slow start, fast, slow end), `linear` (constant speed), `ease-in` (slow start), `ease-out` (slow end), `ease-in-out` (slow start and end), `steps(n, direction)`.
    *   **`transition-delay`**: How long to wait before starting the transition (e.g., `2s`, `400ms`).
*   **Shorthand**: `transition: [property] [duration] [timing-function] [delay];`
    *   **Example**: `transition: font-size 2s ease-in-out 0.2s;`

#### CSS Transform

*   **Purpose**: Used to apply 2D and 3D transformations to an element, altering its shape, size, or position without affecting the document flow.
*   **Common Transform Functions**:
    *   **`rotate()`**: Rotates an element around its central point.
        *   **Example**: `transform: rotate(45deg);` (rotates 45 degrees clockwise). Negative values for counter-clockwise.
    *   **`scale()`**: Changes the size of an element.
        *   **Example**:
            *   `transform: scale(2);` (scales to twice the size equally on X and Y axes).
            *   `transform: scale(0.5);` (scales to half the size).
            *   `transform: scale(1, 2);` (scales X by 1, Y by 2).
            *   `transform: scaleX(0.5);`, `transform: scaleY(0.5);` (scales only on X or Y axis).
    *   **`translate()`**: Moves an element from its original position.
        *   **Example**:
            *   `transform: translate(20px);` (moves 20px right on X-axis).
            *   `transform: translate(20px, 50px);` (moves 20px right, 50px down).
            *   `transform: translateX(20px);`, `transform: translateY(20px);` (moves only on X or Y axis).
        *   **Units**: Can use `px`, `%`, `em`, `rem`, etc.
    *   **`skew()`**: Skews an element along the X and/or Y axis.
        *   **Example**: `transform: skew(30deg);` (skews 30 degrees on X-axis).
*   **Note**: Transforms apply to all content inside the element.

#### Animation

*   **Purpose**: To animate CSS elements through multiple keyframes, creating more complex and continuous motion.
*   **`@keyframes` Rule**: Defines the animation sequence.
    *   **Syntax**:
        ```css
        @keyframes myName {
          from { /* starting styles */ } /* or 0% */
          to { /* ending styles */ }   /* or 100% */
        }
        ```
    *   **Percentage-based Keyframes**: Allows defining styles at various points in the animation.
        ```css
        @keyframes myName {
          0%   { font-size: 20px; }
          50%  { font-size: 30px; }
          100% { font-size: 40px; }
        }
        ```
*   **Animation Properties (applied to the element to be animated)**:
    *   **`animation-name`**: Name of the `@keyframes` rule to bind to the element.
    *   **`animation-duration`**: How long the animation takes to complete one cycle (e.g., `2s`).
    *   **`animation-timing-function`**: Speed curve of the animation (same values as `transition-timing-function`).
    *   **`animation-delay`**: Delay before the animation starts.
    *   **`animation-iteration-count`**: Number of times the animation should play (`infinite` for continuous loop).
    *   **`animation-direction`**: Whether the animation should play forwards, backwards, or alternate.
        *   **Values**: `normal`, `reverse`, `alternate`, `alternate-reverse`.
    *   **`animation-fill-mode`**: How styles are applied before/after animation.
    *   **`animation-play-state`**: Pause or play the animation.
*   **Animation Shorthand**: `animation: [name] [duration] [timing-function] [delay] [iteration-count] [direction];`
    *   **Example**: `animation: myName 2s linear 3s infinite normal;`

#### Practice Set 8 (Summary)

1.  Create a simple loader using CSS:
    *   Step 1: Create a `div` with a circular shape and a thick border from one end (e.g., top).
    *   Step 2: Create an animation (`@keyframes`) that transforms the `div` from `0deg` to `360deg` rotation.
    *   Step 3: Apply the animation property to the loader `div` with `infinite` duration.

#### Key Takeaways (Level 5)

*   Transitions provide smooth changes between element states, often triggered by user interaction (like hover).
*   Transforms allow 2D/3D manipulation (rotate, scale, translate, skew) of elements.
*   Animations, defined with `@keyframes`, enable complex, multi-step visual sequences.
*   Understanding the individual properties and shorthand for transitions and animations is key to creating dynamic web interfaces.