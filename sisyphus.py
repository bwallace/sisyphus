"""
Existential games PRESENTS: Sisyphus
"""

import arcade

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
X_MOVEMENT_SPEED = 3
Y_MOVEMENT_SPEED = 2.5

class Sisyphus(arcade.Window):

    def __init__(self, width, height, title):

        # Call the parent class's init function
        super().__init__(width, height, title)

        # Make the mouse disappear when it is over the window.
        # So we just see our object, not the pointer.
        self.set_mouse_visible(False)

        self.background = None 
        self.player_sprite = None 
        self.starting_x = None
        self.starting_y = None
        self.score = 0
        arcade.set_background_color(arcade.color.ASH_GREY)


    def on_draw(self):
        """ Called whenever we need to draw the window. """
        arcade.start_render()

        arcade.draw_texture_rectangle(SCREEN_WIDTH // 2, (SCREEN_HEIGHT // 2)-5,
                                      SCREEN_WIDTH, SCREEN_HEIGHT, self.background)

        
        score = self.player_sprite.center_y
        BACKGROUND_ADJUSTMENT = 20 
        arcade.draw_text(f"Score: {self.score}".format(score), 10, SCREEN_HEIGHT-BACKGROUND_ADJUSTMENT, arcade.color.WHITE, 14)

        self.player_list.draw()

    def update(self, delta_time):
        if self.player_sprite.center_x >= (SCREEN_WIDTH - self.player_sprite.width // 2) or \
          self.player_sprite.center_y >= (SCREEN_HEIGHT - self.player_sprite.width // 2):
            self.player_sprite.center_x = self.starting_x
            self.player_sprite.center_y = self.starting_y

    def on_key_press(self, key, modifiers):
        """ Called whenever the user presses a key. """
        pass 

    def on_key_release(self, key, modifiers):
        if key == arcade.key.UP:
          self.player_sprite.center_x += X_MOVEMENT_SPEED
          self.player_sprite.center_y += Y_MOVEMENT_SPEED

    def setup(self):
      """ Set up the game and initialize the variables. """
      self.player_sprite = arcade.Sprite("images/sis.png")

      self.starting_x = self.player_sprite.height // 2
      self.starting_y = self.player_sprite.width // 2

      self.player_sprite.center_x = self.starting_x
      self.player_sprite.center_y = self.starting_y

      self.player_list = arcade.SpriteList()
      self.player_list.append(self.player_sprite)

      self.background = arcade.load_texture("images/cliff.png")


def main():
    window = Sisyphus(640, 480, "one must imagine him happy")
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()