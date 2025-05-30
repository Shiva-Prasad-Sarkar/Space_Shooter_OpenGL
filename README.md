# 3D Space Shooter

**GamePlay :**
**`https://youtu.be/vgER14iH06I?si=oGVXR6EZqdvhbzqT`**

**Overview**  
3D Space Shooter is an arcade-style game where you control a fighter spaceship in a 3D space environment. Dodge enemy fire, shoot down alien ships, and collect bonus power-ups while your score climbs. This game is built in Python using OpenGL and GLUT, featuring dynamic backgrounds, moving stars, and engaging gameplay mechanics that blend action with strategy.

---

**Gameplay**  
- The game starts with a welcome screen offering options like starting a game or viewing the controls.
- Once the game begins, you’ll pilot a spaceship through a space environment filled with enemies.
- Your goal is to survive by avoiding collisions and enemy bullets while shooting and destroying enemy ships.
- Along the way, you can activate a shield for extra protection and use bombs to clear multiple enemies.
- Bonus items randomly appear, giving you extra ammunition or restoring your defenses.

---

**Game Controls**

- **Movement:**
  - **`w`** – Move Up
  - **`s`** – Move Down
  - **`a`** – Move Left
  - **`d`** – Move Right

- **Rotation:**
  - **`x`** – Rotate on the X-axis
  - **`y`** – Rotate on the Y-axis
  - **`z`** – Rotate on the Z-axis

- **Actions and Weapons:**
  - **Mouse Left Button:** Fire a Bullet
  - **Mouse Right Button:** Deploy a Bomb (if available)
  - **`h`:** Activate the Shield (if you have enough score)
  - **`l`:** Load Extra Bullets when running low

- **View and Interface:**
  - **`f`:** Toggle First-Person View to switch perspectives
  - **`g`:** Start the game from the welcome screen
  - **`c`:** Display game controls on screen
  - **`m`:** Return to the Main Menu
  - **`q`:** Quit the game
  - **Spacebar:** Pause or Resume the game
  - **Arrow Keys:** Move the camera when not in first-person view

---

**Code and Game Components**

- **Graphics and Environment:**  
  The game creates a space scene that includes a grid-style background (“space()”), a star field (“draw_star()”), and a bordered play area (“space_boarder()”). These elements work together to set the stage for the action.

- **Player’s Spaceship:**  
  Your spaceship is drawn with basic 3D shapes (cubes, cylinders, and spheres) using the function “fighter_spaceship()”. The design allows for smooth movements, rotations, and even a shield effect when activated.

- **Enemies and Their Weapons:**  
  - **Enemy Generation:** Enemies are generated at random positions on the grid by the “pos_maker()” function.
  - **Enemy Appearance:** The function “draw_enemy()” is in charge of rendering these alien ships.
  - **Enemy Attacks:** Enemies fire bullets towards your spaceship. Their projectiles and positions are continuously updated in the game loop.

- **Weapon Systems:**  
  - **Player Bullets:** Fired using the mouse left button, these are managed by the “shottt()” function.
  - **Bombs:** Activated with the mouse right button, bombs clear groups of aliens and are handled by “shot_bomb()”.

- **Game Mechanics:**  
  The game uses several functions for the core interactions:
  - **Collision Detection:** “ship_crash()” and “enemy_bullet()” detect when enemy fire or collisions occur.
  - **Enemy Destruction:** “kill_alliens()” processes successful hits on enemies and updates your score.
  - **Bonus System:** Random bonuses appear and can be picked up using functions like “random_bonus()” and “get_bonus()” to restore ammunition or protect your ship.

- **User Input and Game Loop:**  
  A set of keyboard and mouse listener functions (like “keyboardListener()” and “mouseListener()”) capture your actions. The idle function continually refreshes the game state—moving bullets, toggling animations, and checking for collisions—to ensure smooth, ongoing gameplay.

---

**Gameplay Strategy**  
Success in 3D Space Shooter comes down to quick reflexes and smart tactics. Focus on:
- **Maneuvering:** Avoid enemy bullets and collisions by continually adjusting your ship’s position.
- **Timing Your Attacks:** Use the correct mix of bullets and bombs to take down enemy clusters.
- **Defensive Play:** Don’t hesitate to activate your shield when surrounded.
- **Collecting Bonuses:** Keep an eye out for bonus power-ups that can boost your ammunition and defenses.

Each round is a test of precision and timing, challenging you to balance offensive play with staying safe in a constantly shifting battlefield.

---

